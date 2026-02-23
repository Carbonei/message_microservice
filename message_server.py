import time
import zmq 
import json
import random
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
message_num = random.randint(1, 55)

while True:
    correct = socket.recv()
   
    if len(correct) > 0:
        if correct.decode() == 'Q': 
            break

    if correct.decode() == '1':
        
        message_num = random.randint(1, 55)

        with open('positive.json', 'r') as pos_file:
            data = json.load(pos_file)
            print(type(data))
            message = data[message_num]
            
        
    elif correct.decode() == '0':
        message_num = random.randint(1, 55)

        with open('negative.json', 'r') as neg_file:
            data = json.load(neg_file)
            print(type(data))
            print(data)
          
            message = data[message_num]
            
        
    time.sleep(0.5)
    
    mes = message["message"]
    print(type(mes))
    mes = str(mes)
    socket.send_string(mes)

context.destroy()