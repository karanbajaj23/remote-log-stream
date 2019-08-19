# remote-log-stream

Socket based server-client utility which can be used to tail server logs realtime.

## Setup

sh setup.sh

## Server

python3 server.py --l <log-file>

Ex:
python3 server.py --l test.log

## Client

python3 client.py --n <number-of-lines>

Ex:
python3 client.py --n 5