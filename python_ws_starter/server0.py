#!/usr/bin/env python
 
import asyncio
import websockets
 
async def hello(websocket):
    received = await websocket.recv()
    print(f"received {received}")
    
    send = f"echo {received}"
    await websocket.send(send)
    print(f"send {send}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())