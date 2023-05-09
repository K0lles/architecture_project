import socketserver

from server.server_architecture import *


if __name__ == '__main__':
    HOST, PORT = 'localhost', 8080

    socketserver.TCPServer.allow_reuse_address = True

    server = ThreadedTCPServer((HOST, PORT), WebServer)

    print('Starting web server on {}:{}...'.format(HOST, PORT))

    # Run the server forever
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        print(f'Web server was stopped.')
    except Exception as e:
        server.shutdown()

    server.shutdown()
