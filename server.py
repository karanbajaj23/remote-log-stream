import asyncio
import websockets
import argparse

import logging
import functools
from urllib.parse import urlparse, parse_qs

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 5555
DEFAULT_N_LINES = 1

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

async def tail_log(websocket, path, param):
	try:
		parse_result = urlparse(path)
	except Exception:
		raise ValueError('Error parsing URI')
	query = parse_qs(parse_result.query)
	if query and query['lines'] and query['lines'][0]:
		n_lines = int(query['lines'][0])
	else:
		n_lines = DEFAULT_N_LINES
	if param and param[0]:
		log_file = param[0]
		with open(log_file) as f:
			lines = f.readlines()
			last_lines = lines[-n_lines:]
			await websocket.send(last_lines)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--h', default=DEFAULT_HOST)
	parser.add_argument('--p', type=int, default=DEFAULT_PORT)
	parser.add_argument('--l', required=True, action='append', help='Log file')
	args = parser.parse_args()

	start_server = websockets.serve(functools.partial(tail_log, param=args.l), args.h, args.p)
	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
	main()