#!/usr/bin/env python
 
import asyncio
import websockets
import datetime
 
async def show_time(websocket):
    while True:
        message = datetime.datetime.utcnow().isoformat() + "Z"
        # print("tick")
        try:
            await websocket.send(message)
            await asyncio.sleep(1)
        except websockets.ConnectionClosedOK:
            print("Conn closed (time sock)")
            break    


async def send_echo(websocket):
    while True:
        try:
            received = await websocket.recv()
            print(f"received {received}")
            
            send = f"echo {received}"
            await websocket.send(send)
            print(f"send {send}")

        except websockets.ConnectionClosedOK:
            print("Conn closed")
            break  

async def main2():
    async with websockets.serve(show_time, "localhost", 8765):
        await asyncio.Future()  # run forever

async def main1():
    async with websockets.serve(send_echo, "localhost", 8764):
        await asyncio.Future()  # run forever


import os

if __name__ == "__main__":
    pid = os.fork()

    if pid > 0 :
        asyncio.run(main1())      
    else:    
        asyncio.run(main2())
        