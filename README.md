# remote-log-stream

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