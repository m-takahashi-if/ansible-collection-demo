#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import parse_qs
from urllib.parse import urlparse

class CalcHandler(BaseHTTPRequestHandler):

    numbers = list()

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        if 'command' in params:
            for command in params.get('command'):
                if command == 'clear':
                    self.numbers.clear()

        if 'value' in params:
            for value in params.get('value'):
                self.numbers.append(int(value))

        expression = ''
        operator = ''
        for number in self.numbers:
            expression += operator + str(number)
            operator = ' + '

        expression += (' = ' if expression else '') + str(sum(self.numbers)) + '\n\n'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(expression.encode('utf-8'))


httpd = HTTPServer(('0.0.0.0', 8080), CalcHandler)
httpd.serve_forever()
