import ecc

SENDER_PRIVATE_KEY =  13
RECEIVER_PRIVATE_KEY = 15

EEC_COMMON_POINT = 8
ELLIPTIC_CURVE = ecc.EC(1,18,19)

ORIGINAL_IMAGE = './data/1.jpg'
SECRET_IMAGE = './data/secret.png'
OUTPUT_IMAGE = './output/new1.png'
RECOVERED_IMAGE = './output/new2.png'

INPUT_MESSAGE = input('Enter Message to Hide: ')
