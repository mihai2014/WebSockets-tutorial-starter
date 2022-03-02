# from channels.consumer import SyncConsumer

# class EchoConsumer(SyncConsumer):

#     def websocket_connect(self, event):
#         self.send({
#             "type": "websocket.accept",
#         })

#     def websocket_receive(self, event):
#         self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })


# from channels.consumer import AsyncConsumer

# class EchoConsumer(AsyncConsumer):

#     async def websocket_connect(self, event):
#         await self.send({
#             "type": "websocket.accept",
#         })

#     async def websocket_receive(self, event):
#         await self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })

from channels.generic.websocket import AsyncWebsocketConsumer
import time

class EchoConsumer(AsyncWebsocketConsumer):   
    async def connect(self):

        await self.accept()

    async def receive(self, text_data):

        await self.send(text_data="echo " +  text_data)


import asyncio
import datetime

class TimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        await self.accept()

        while True:
            timeStr = datetime.datetime.utcnow().isoformat() + "Z"
            await self.send(text_data=timeStr)
            print("tick")
            await asyncio.sleep(1)
        
