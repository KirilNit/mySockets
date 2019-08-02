import socket
import sys
import time
import  logging

logger = logging.getLogger("API")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def client_connection():
    sockett = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_address = ('localhost', 10000)
    server_address = ('10.0.1.105', 10002)

    # sockett.bind(('10.0.1.105', 10005))
    # sockett.listen(5)
    # c
    # print(sys.stderr, 'starting server on ', server_address)

    # wanted_address = ''
    # while wanted_address == '':
    #     wanted_address = input('Please input IPv4 address: ')
    #     port = int(input("Port"))
    #     server_address = (wanted_address, port)
    # print(sys.stderr, ' Connecting to {0}'.format(server_address))
    stoped = 'false'
    sockett.connect(server_address)

    # try:
    #     sockett.connect(server_address)
    # except:
    #     time.sleep(10)
    #     sockett.connect(server_address)
    #     logger.info('Connection established to the {0}'.format(server_address))
    # finally:
    #     logger.info('Connection failed')

    try:
        message = 'This message will be redirected back!!!!!'[::-1]
        logger.info('Sending to {0}'.format(server_address))
        # sockett.sendall(message)
        sockett.sendall(message.encode('ascii'))
        # # sockett.sendall(''.join(format(ord(x), 'b') for x in message))

        # Locking for response
        amount_expected= len(message)
        amount_recived = 0
        while amount_recived < amount_expected:
            data = sockett.recv(128)
            amount_recived += len(data)
            logger.info('Recived {0}'.format(data))
        while stoped != 'exit':
            stoped = input("Input the data or input `exit`  for close connection: ")
            sockett.sendall(stoped.encode('ascii'))
            amount_recived1 = 0
            amount_expected1 = len(stoped)
            while amount_recived1 < amount_expected1 and amount_recived1 == 0:
                data = sockett.recv(64)
                amount_recived1 += len(data)
                # logger.info('Recived back: {0}'.format(data))
                print('Recived back: {0}'.format(data))
                amount_recived1 = 1

    finally:
        logger.info(' Closing connection')
        sockett.close()


if __name__ == '__main__':
    client_connection()