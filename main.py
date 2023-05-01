import socket
from threading import Thread

from server.server_architecture import *


if __name__ == '__main__':
    HOST, PORT = 'localhost', 8080

    server = ThreadedTCPServer((HOST, PORT), WebServer)

    print('Starting web server on {}:{}...'.format(HOST, PORT))

    # Run the server forever
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f'Web server was stopped.')
        server.shutdown()
    except Exception as e:
        server.shutdown()
