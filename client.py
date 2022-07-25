# import zmq

# context = zmq.Context()
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://127.0.0.1:5555")

# while True:
#     msg = input('enter your msg here: ')
#     socket.send(b"{msg}")
#     print('sending to server: ', msg)
#     print('From server : ', socket.recv())
#     print('')



#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")

#  Do 10 requests, waiting each time for a response
while True:
    request = input('Enter your message here: ')
    print(f"Sending request {request} …")
    socket.send_string(request)

    #  Get the reply.
    message = socket.recv()
    message = str(message)
    print(f"Received reply {request} in Spanish [{message}] ")

