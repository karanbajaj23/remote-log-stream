import asyncio
import websockets
import argparse

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 5555

async def tail(uri):
	if uri:
		async with websockets.connect(uri) as websocket:
			log_lines = await websocket.recv()
			print(log_lines)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--h', default=DEFAULT_HOST)
	parser.add_argument('--p', type=int, default=DEFAULT_PORT)
	parser.add_argument('--n', required=True, help='Number of lines')
	args = parser.parse_args()
	uri = 'ws://'+str(args.h)+':'+str(args.p)+'?lines='+str(args.n)
	asyncio.get_event_loop().run_until_complete(tail(uri))

if __name__ == '__main__':
	main()