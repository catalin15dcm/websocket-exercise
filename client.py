import asyncio
import websockets
import argparse
import sys
from colorama import init, Fore
init(autoreset=True)

async def send_messages(ws):
    while True:
        message = await asyncio.get_event_loop().run_in_executor(None, input, "> ")
        await ws.send(message)

async def receive_messages(ws):
    async for message in ws:
        print(Fore.GREEN + message)

async def main(name):
    uri = "ws://localhost:12346"
    async with websockets.connect(uri) as websocket:
        await websocket.send(name)
        await asyncio.gather(
            send_messages(websocket),
            receive_messages(websocket),
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WebSocket Chat Client")
    parser.add_argument("--name", required=True, help="Numele clientului")
    args = parser.parse_args()

    try:
        asyncio.run(main(args.name))
    except KeyboardInterrupt:
        print("\nIeșire...")
        sys.exit()
