My microservice translates English sentences to Spanish.

Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.
- First, install zeroMQ to send the request. For python, you can use "pip install pyzmq".
- When server program runs, it waits for a request from client server to be sent. 
- When client server runs the client server will show a message "Connect to server..." 
- Then, it is going to ask the client server to enter a message to send it to my microserive server. 
- For example, when the client program asks "Enter your message here", the client can type "Hello" and press enter to request. 
- When a client enters "Hello", a message "sending request Hello ..." will show. 
- To request a differnt Spanish word, both server and client programs need to stop and modify the word in server program
and run it again to receive the differnt word in Spanish (ex. Thank you).

Clear instructions for how to RECEIVE data from the microservice you implemented
- First, install zeroMQ to receive the request. For python, you can use "pip install pyzmq".
- My server program imports Translator from googletrans to translate the requsted English text to Spanish.  
- When client program sends a request, my server program will translate the reqeusted text. 
- Then, my client program receives the translated word and prints in on the screen. 
- For example, when my client program requests "Hello", my client program will show a message "Received reply Hello in Spanish [b "Hola"].
- When a client enters "Hello" and my server program has "Hello" data in a prgram, it will translate the word to Spanish.
- To receive a differnt Spanish word, both server and client programs need to stop and modify the word in server program
and run it again to show the differnt word in Spanish (ex. Thank you).


UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand
![uml](https://user-images.githubusercontent.com/86205051/180896491-fc3189dc-44ab-46db-85f7-2d3db1735616.jpg)
 
