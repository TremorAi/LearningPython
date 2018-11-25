import asyncio
import websockets as ws
from typing import List


from websockets import WebSocketServerProtocol

clients: List[WebSocketServerProtocol] = []


async def handle_client(socket: WebSocketServerProtocol, ignored):
    clients.append(socket)

    # print('connection', socket.remote_address)
    # await send_message("hello world! again!")

    while socket.open:
        await asyncio.sleep(1)
        # await send_message("hello world! again!")

    clients.remove(socket)


async def _socket_server_main():
    server = await ws.serve(handle_client, 'localhost', 9999, )
    await server.wait_closed()


async def send_message(msg):
    while not clients:
        print('wait')
        await asyncio.sleep(1)

    await clients[0].send(msg)
