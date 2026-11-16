"""Versão corrigida do login de laboratório, com consulta parametrizada.

Corrige apenas a SQL injection. Hash de senha, logs, rate limiting e CSRF
ficam fora do escopo deste laboratório. Uso apenas educacional, em 127.0.0.1.
"""

import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs

LOGIN_PAGE = """<!doctype html>
<html lang="pt-BR">
<head><meta charset="utf-8"><title>GuardAI Lab</title></head>
<body>
  <h1>GuardAI Lab: login</h1>
  <form method="post" action="/login">
    <label>Usuário <input name="username"></label>
    <label>Senha <input name="password" type="password"></label>
    <button type="submit">Entrar</button>
  </form>
</body>
</html>
"""

DB = sqlite3.connect(":memory:", check_same_thread=False)
DB.execute("CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT NOT NULL)")
DB.execute("INSERT INTO users VALUES ('admin', 's3nh4-forte')")
DB.commit()


def authenticate(username, password):
    query = "SELECT username FROM users WHERE username = ? AND password = ?"
    return DB.execute(query, (username, password)).fetchone() is not None


class LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.respond(200, LOGIN_PAGE)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        fields = parse_qs(self.rfile.read(length).decode())
        username = fields.get("username", [""])[0]
        password = fields.get("password", [""])[0]
        if authenticate(username, password):
            self.respond(200, "<h1>Login OK</h1>")
        else:
            self.respond(401, "<h1>Credenciais inválidas</h1>")

    def respond(self, status, content):
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode())

    def log_message(self, format, *args):
        pass


def create_server(port=8000):
    return ThreadingHTTPServer(("127.0.0.1", port), LoginHandler)


if __name__ == "__main__":
    server = create_server()
    print("Laboratório corrigido em http://127.0.0.1:8000")
    server.serve_forever()
