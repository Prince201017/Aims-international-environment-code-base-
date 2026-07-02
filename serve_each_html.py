import os
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler


def make_handler(filename):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            try:
                with open(filename, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            except FileNotFoundError:
                self.send_error(404, 'File not found')

        def log_message(self, format, *args):
            return

    return Handler


def serve_file_on_port(filename, port):
    server = HTTPServer(('0.0.0.0', port), make_handler(filename))
    print(f"Serving {filename} on http://0.0.0.0:{port}/")
    server.serve_forever()


if __name__ == '__main__':
    base_port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    if not html_files:
        print('No HTML files found in current directory.')
        sys.exit(1)

    threads = []
    for i, fn in enumerate(sorted(html_files)):
        port = base_port + i
        t = threading.Thread(target=serve_file_on_port, args=(fn, port), daemon=True)
        t.start()
        threads.append((fn, port))

    print('Started servers:')
    for fn, port in threads:
        print(f"{fn}: http://localhost:{port}/")

    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        print('Shutting down.')
