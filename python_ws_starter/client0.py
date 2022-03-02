#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        send = input("send ")

        await websocket.send(send)
        print(f"send {send}")

        receive = await websocket.recv()
        print(f"receive {receive}")

if __name__ == "__main__":
    asyncio.run(hello())