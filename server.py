from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OLLAMA_CHAT = "http://127.0.0.1:11434/api/chat"

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_POST(self):
        if self.path != "/api/chat":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = self.rfile.read(length)
            request = Request(OLLAMA_CHAT, data=payload, headers={"Content-Type": "application/json"}, method="POST")
            with urlopen(request, timeout=300) as response:
                body = response.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except HTTPError as exc:
            body = json.dumps({"error": exc.read().decode("utf-8", "replace")}).encode()
            self.send_response(exc.code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except (URLError, TimeoutError, OSError) as exc:
            body = json.dumps({"error": "Cannot connect to Ollama at 127.0.0.1:11434. Start Ollama and try again. " + str(exc)}).encode()
            self.send_response(502)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print(f"Morrow is ready at http://{address[0]}:{address[1]}")
    print("Keep this window open. Ollama must also be running.")
    ThreadingHTTPServer(address, Handler).serve_forever()
