#-------------------------------------------------------------------------
#    Program: webserver.py
#    Programmer: Luis F. Velázquez Sosa
#    Discription:
#         This program is to demostrate how a web server function 
#         using sockets. It a simple web server that uses HTTP 1.0
#         to send to the browser client of your choice. Tested to
#         function with Chrome, Edge and Firefox. 
#
#    
#-------------------------------------------------------------------------
from socket import *
import sys # In order to terminate the program

debug = 1
PORT = 8000

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('',PORT))
serverSocket.listen(5)

while True:
#Establish the connection
     print('\n\nWeb server activated on port:', PORT) 
     client, addr = serverSocket.accept()
     print("Connected to the client",addr)
     try:
          if debug:
               #this is to see if the webserver funtions
               #simply sends the basic elements to create a website using 
               #html file
               client.send('HTTP/1.0 200 OK\r\n'.encode())
               client.send("Content-Type: text/html\r\n\r\n".encode())
               client.send('<html><body><h1>Hello World</body></html>'.encode())
               client.close()

          #Need to send the index.html file in different parts
          #filename is an array that will have all the elements
          #of the html file that will be sent to the sockets 
          if not debug:
               #test code to observe what the client sends (helped to make the proxy)
               '''message = client.recv(2048)
               print("message:",message)
               print (str(message.split()[1]).partition("/")[2])
               msg2 = message.split()[1]
               print(type(msg2))
               print ((str(msg2).split("/")[1]).split("'")[0])
               msg3 = str(msg2).split("/")[1].split("'")[0]
               print(msg3)
               print(len(msg3))
               #-----------------------------------
               if len(msg3) > 1:
                    hostname = msg3[1]
               else:
                    hostname = msg3
               msg3 = "/".join(msg3[1:])
               #-----------------------------------
               hostname = msg3[1]
               #filename = "/".join(msg3[1:])
               if len(msg3)>len(hostname):
                    hostname = msg3

               print("Hostname:",hostname)
               print("Filename",msg3)
               print(filename)

               filetouse = msg3
               print(msg3[-1])
               if msg3[-1] == "/":
                    filetouse += "index.html"
               print(filetouse)'''
               print("-"*70)
               filename = "index.html"
               print("Opening ",filename,"...")
               f = open(filename)
               output = f.read()
               print("Sending the message to client...")
               client.send(('HTTP/1.0 200 OK\r\n' + output).encode())
               client.close()

     except IOError:
          #if the file is not found then send a 404 error to the browser
          print("Error!, 404 ERROR")
          client.send('HTTP/1.0 404 Not Found\r\n'.encode())
          client.close()

serverSocket.close()

sys.exit()#Terminate the program after sending the corresponding data


