#!/usr/bin/env python3
"""Server tĩnh cho lúc phát triển: như `python3 -m http.server` nhưng gửi
Cache-Control: no-store, để Chrome luôn tải CSS/font mới (không giữ bản cũ).

  python3 dev/serve.py [cổng]     # mặc định 3000, phục vụ thư mục gốc project
"""
import http.server, os, sys
from functools import partial

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000


class NoStore(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


http.server.ThreadingHTTPServer(("", PORT), partial(NoStore, directory=ROOT)).serve_forever()
