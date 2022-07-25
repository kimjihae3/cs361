#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

# import zmq
# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://127.0.0.1:5555")

# while True:
#     msg = socket.recv()
#     print('From client : ',  {msg})
#     serverMsg = input('enter your msg here to client: ')
#     socket.send({b"{serverMsg}"})
#     print('')


import time
import zmq
from googletrans import Translator

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5555")  # bind it to local port 5000

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request from client: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    translator = Translator()
    serverMessage = input("copy the clint's message here: ")
    trans = translator.translate("Thank you", dest='es')
    print(f"Sending response in Spanish: {trans.text}...")
    socket.send_string(trans.text)
