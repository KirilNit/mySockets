import socket
import sys
import logging
import  logging

logger = logging.getLogger("API")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def server():
    # creating a TCP/IP socket

    sockett = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.socketpair()

    # binding socket to the port
    server_address = ('10.0.1.105', 10002)
    # server_address = ('localhost', 10000)
    sockett.bind(server_address)
    logger.info('Starting server on {0}'.format(server_address))
    # print('Starting server on {0}'.format(server_address))

    # listen to incoming connections
    sockett.listen(5)

    while True:
        logger.info("Waiting for connections")
        connection, client_address = sockett.accept()

        try:
            # print('Connection with ', client_address, ' established')
            answer = 'I\'m gonna reverse Your data'
            connection.send(answer.encode('ascii'))

            while True:
               data = connection.recv(128)
               logger.info('Recived data from ',  client_address)
               logger.info('Message in recived data is ', data)

               if data:
                   try:
                       logger.info('Resending data to {0}'.format(client_address))
                       connection.sendall(data[::-1])
                       payload = 'And now let\'s interact a little bit)'
                       connection.sendall(payload.encode('ascii'))
                   except Exception as e:
                       logger.info(e)
                       #
                       # connection.sendall(e)
               else:
                   logger.info('No data recieved from ', client_address)
                   break
        finally:
            # cleaning up connection
            logger.info('++++++Closing connection!!!++++++')
            connection.close()

if __name__ == "__main__":
    server()