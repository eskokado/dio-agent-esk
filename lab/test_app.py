"""Prova que o bypass por SQL injection funciona no app.py e falha no app_fixed.py."""

import importlib.util
import threading
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PAYLOAD = "' OR '1'='1' --"
VALID_PASSWORD = "s3nh4-forte"


def load_module(name, filename):
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def post(port, username, password):
    data = urllib.parse.urlencode({"username": username, "password": password}).encode()
    request = urllib.request.Request(
        f"http://127.0.0.1:{port}/login", data=data, method="POST"
    )
    try:
        with urllib.request.urlopen(request) as response:
            return response.status, response.read().decode()
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode()


def main():
    vulnerable = load_module("vulnerable_app", "app.py")
    fixed = load_module("fixed_app", "app_fixed.py")
    servers = [vulnerable.create_server(0), fixed.create_server(0)]
    vulnerable_port = servers[0].server_address[1]
    fixed_port = servers[1].server_address[1]

    for server in servers:
        threading.Thread(target=server.serve_forever, daemon=True).start()

    try:
        checks = [
            (
                "login legítimo funciona no app.py",
                post(vulnerable_port, "admin", VALID_PASSWORD),
                200,
                "Login OK",
            ),
            (
                "login legítimo funciona no app_fixed.py",
                post(fixed_port, "admin", VALID_PASSWORD),
                200,
                "Login OK",
            ),
            (
                "bypass com SQL injection funciona no app.py",
                post(vulnerable_port, PAYLOAD, "x"),
                200,
                "Login OK",
            ),
            (
                "bypass com SQL injection no campo de senha funciona no app.py",
                post(vulnerable_port, "admin", PAYLOAD),
                200,
                "Login OK",
            ),
            (
                "bypass com SQL injection falha no app_fixed.py",
                post(fixed_port, PAYLOAD, "x"),
                401,
                "Credenciais inválidas",
            ),
            (
                "bypass com SQL injection no campo de senha falha no app_fixed.py",
                post(fixed_port, "admin", PAYLOAD),
                401,
                "Credenciais inválidas",
            ),
            (
                "credencial inválida falha no app_fixed.py",
                post(fixed_port, "admin", "errada"),
                401,
                "Credenciais inválidas",
            ),
            (
                "apóstrofo legítimo não quebra o app_fixed.py",
                post(fixed_port, "O'Brien", "x"),
                401,
                "Credenciais inválidas",
            ),
        ]
    finally:
        for server in servers:
            server.shutdown()
            server.server_close()

    failed = False
    for name, (status, body), expected_status, expected_text in checks:
        ok = status == expected_status and expected_text in body
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        failed = failed or not ok

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
