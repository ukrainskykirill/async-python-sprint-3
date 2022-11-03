import asyncio
from server import Server
from client import Client

class TestServer:
    def setup(self) -> None:
        self.server = Server()
        self.client = Client()

    def test_start_server(self):
        asyncio.run(self.server.start_server())
        assert self.server.host == '127.0.0.1'









