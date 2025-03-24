import asyncio
import websockets
from websockets.asyncio.server import serve

connected_clients = {}

async def echo(websocket):
    try:
        name = await websocket.recv()
        connected_clients[websocket] = name
        print(f"{name} s-a conectat.")

        async for message in websocket:
            broadcast_message = f"< ({name}) {message}"
            for client_ws in connected_clients:
                if client_ws != websocket:
                    await client_ws.send(broadcast_message)

    except websockets.ConnectionClosed:
        print(f"{connected_clients.get(websocket, 'Unknown')} s-a deconectat.")
    finally:
        connected_clients.pop(websocket, None)

async def main():
    async with websockets.serve(echo, "localhost", 12346) as server:
        print("Serverul rulează pe ws://localhost:12346...")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
