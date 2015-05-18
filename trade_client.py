import json
import socket


from orderbook import create_confirm


def send_msg(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "Received: {}".format(response)
    finally:
        sock.close()
    return response


def send_offer(ip, port, offer):
    message = json.dumps(offer)
    return send_msg(ip, port, message)


def handle_response(response):
    response = json.loads(response)
    if response:
        if response['type'] == 'trade':
            return handle_trade(response)
    return "Nothing"


def handle_trade(trade):
    id = trade['trade-id'].split(';')[0]

    return create_confirm(
        id = id,
        trade_id = trade['trade-id']
    )
