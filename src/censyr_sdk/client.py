import requests
import websockets
import asyncio

class CensyrClient:
    """
    Basic client for interacting with the Censyr API.
    """

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def get_status(self):
        """Check API status"""
        resp = self.session.get(f"{self.base_url}/status")
        resp.raise_for_status()
        return resp.json()

    async def connect_websocket(self, ws_url: str):
        """Example WebSocket connection"""
        async with websockets.connect(ws_url, extra_headers={"Authorization": f"Bearer {self.api_key}"}) as ws:
            await ws.send("ping")
            return await ws.recv()
