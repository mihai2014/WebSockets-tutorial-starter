#!/usr/bin/env python

import asyncio
import websockets

async def get_time():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            received = await websocket.recv()
            print(f"Received: {received}")

#terminal connenction: python -m websockets ws://localhost:8765/
async def get_echo():
    uri = "ws://localhost:8764"
    async with websockets.connect(uri) as websocket:
        #send = input("Send: ")
        send = "testing1"

        await websocket.send(send)
        print(f"send {send}")

        receive = await websocket.recv()
        print(f"receive {receive}")
        
        send = "testing2"
        await websocket.send(send)
        print(f"send {send}")

        receive = await websocket.recv()
        print(f"receive {receive}")


import sys

if __name__ == "__main__":

    try:
        option = sys.argv[1]
    except:
        print("Use option: echo/time")
        sys.exit(1)

    if not (sys.argv[1] in ["echo","time"]):
        print("Use option: echo/time")
        sys.exit(1)


    if(option == "echo"):
        asyncio.run(get_echo())
    
    if(option == "time"):
        asyncio.run(get_time())