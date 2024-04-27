import http.server, socketserver
from urllib.parse import urlparse, parse_qs
import subprocess
from subprocess import Popen, PIPE, STDOUT
from pathlib import Path

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("anfrage")
        if self.path.startswith("/tasks"):
            output = subprocess.Popen([r"C:\Program Files (x86)\bin\bash.exe", '-c', '. /etc/profile; task export'], stdout=PIPE, stderr=STDOUT).communicate()[0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(output)
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)


PORT = 9001
handler = Handler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    print(http.server.__file__)
    httpd.serve_forever()