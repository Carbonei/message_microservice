import zmq 
context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://flip4.engr.oregonstate.edu:5555")

print("What is 2 + 2?\n")
answer = input()
if answer == '4':
    socket.send_string("1")
else:
    socket.send_string("0")
message = socket.recv()
print(message.decode())
socket.send_string("Q") 