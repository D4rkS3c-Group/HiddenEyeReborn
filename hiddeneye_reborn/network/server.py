import os
import http.server
import socketserver
from threading import Thread


class WebServer:
    def __init__(self, port: int = 8080, host: str = "localhost"):
        self.port = port
        self.host = host
        self.server = None
        self.thread = None
        self.directory = None

    def start(self):
      if not self.server:
          os.chdir(self.directory)
          handler = http.server.SimpleHTTPRequestHandler
          self.server = socketserver.TCPServer((self.host, self.port), handler)
          self.thread = Thread(target=self.server.serve_forever)
          self.thread.start()
      else:
          print('Server already started')

    def stop(self):
      if self.server:
          self.server.shutdown()
          self.server = None
          self.thread = None
      else:
          print('No server to stop')

    def serve(self, directory: str):
        self.directory = directory
        self.start()