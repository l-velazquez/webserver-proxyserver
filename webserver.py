from email import message
from socket import *
import sys # In order to terminate the program

debug = 0
PORT = 12001

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('',PORT))
serverSocket.listen(5)

while True:
#Establish the connection
     print('\n\nWeb server activated') 
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
               message = client.recv(2048)
               print("message:",message)
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


