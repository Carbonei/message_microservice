import time
import zmq 
import json
import random

#set up communication
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#intialize message index with random number
message_num = random.randint(1, 55)
#loop for communication
while True:
    #get communication
    correct = socket.recv()
   
   #quit at 'Q'
    if len(correct) > 0:
        if correct.decode() == 'Q': 
            break
    #Get Positive message
    if correct.decode() == '1':
        
        message_num = random.randint(1, 55)

        with open('positive.json', 'r') as pos_file:
            data = json.load(pos_file)
            print(type(data))
            message = data[message_num]
            
    #get negative message
    elif correct.decode() == '0':
        message_num = random.randint(1, 55)

        with open('negative.json', 'r') as neg_file:
            data = json.load(neg_file)
            print(type(data))
            print(data)
          
            message = data[message_num]
            
        
    time.sleep(0.5)
    #Prepare and send message
    mes = message["message"]
    print(type(mes))
    mes = str(mes)
    socket.send_string(mes)
#end communication
context.destroy()