A. The message_microservice receives a request for a message that confirms a user is correct or incorrect. The microservice does not compute if the user
is correct or incorrect, that is the responsibility of the caller. The service only returns a message to the requesting program.

B. To request a message from the microservice, the calling program should use ZeroMQ to establish a communication pipeline and send '1' for a message
confirming a user is correct, '0' for a message confirming the user is wrong, or 'Q' to close communications. 
For example:

import zmq 
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://flip4.engr.oregonstate.edu:5555")

sets up the environment specifically on port 5555 on the engineering flip server 4. "tcp://flip4.engr.oregonstate.edu:5555" can alternatively be replaced
with a user's local host. Then, to request data for a correct answer, socket.send_string("1") is used. The "1" can be replaced with "0" or "Q" 
appropriately. 

C. To receive the data, the caller must use socket.recv(). For example, message = socket.recv() stores the encrypted data in the variable "message."
To use the data, the caller uses variable_name.decode() or, in line with the example, message.decode().

D.  ![UML Diagram](../UML_diagram.png "UML Diagram image")
