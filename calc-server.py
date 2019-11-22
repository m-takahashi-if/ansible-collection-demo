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
        commands = params.get('command')

        if commands:
            command = commands[0]

            if command == 'clear':
                self.numbers.clear()
            else:
                self.numbers.append(int(command))

        expression = ''
        operator = ''
        for number in self.numbers:
            expression += operator + str(number)
            operator = ' + '

        expression += (' = ' if expression else '') + str(sum(self.numbers))

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(expression.encode('utf-8'))


httpd = HTTPServer(('0.0.0.0', 8080), CalcHandler)
httpd.serve_forever()
