from socket import *
import sys # In order to terminate the program

debug = 0
PORT = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('',PORT))
serverSocket.listen(5)

while True:
#Establish the connection
     print('Web server activated') 
     client, addr = serverSocket.accept()
     try:
          if debug:
               client.send('HTTP/1.0 200 OK\r\n'.encode())
               client.send("Content-Type: text/html\r\n\r\n".encode())
               client.send('<html><body><h1>Hello World</body></html>'.encode())
               client.close()
          #Need to send the index.html file in different parts
          #filename is an array that will have all the elements
          #of the html file that will be sent to the sockets 
          filename = "index.html"
          f = open(filename)
          output = f.read()
          client.send(('HTTP/1.0 200 OK\n\n' + output).encode())
          client.close()

     except IOError:
          print("Error!, 404 ERROR")
          client.send('HTTP/1.0 404 Not Found\r\n'.encode())
          client.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data


