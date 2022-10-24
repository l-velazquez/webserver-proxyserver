#-------------------------------------------------------------------------
#    Program: webserver.py
#    Programmer: Luis F. Velázquez Sosa
#    Discription:
#         This program is meant to cache the web pages that the client 
#         request to send. I uses the localhost ip and the port given 
#         in the command line. 
#-------------------------------------------------------------------------
from socket import *
import os
import sys

#from proxy-server import ADDRESS

'''if len(sys.argv) <= 1:
	print ('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)'''

ADDRESS = "localhost"
PORT = 12001
lenx = 70

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((ADDRESS,PORT))
tcpSerSock.listen(5)
#
while 1:

	# Start receiving data from the client
	print ('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print ('Received a connection from:', addr)
	#---------------------------------------------------------------------
#Recieving the message

	message = tcpCliSock.recv(2048)
	print("-"*lenx)
	print(message)
	# Extract the filename and hostname from the given message
	print (message.split()[1])
	filename = str(str(message.split()[1]).partition("/")[2]).split("'")[0]
	print("-"*lenx)
	print("filename 1",filename)
	print("filename.split('/')",filename.split("/"))
	filename = filename.split("/")[0]
	print("filename 2",filename)
	hostname = filename[0]
	#---------------------------------------------------------------------
	if len(filename) > len(hostname):
		hostname = filename		
	#no entiendo porque hace esto?
	#filename = "/".join(filename[1:])
	#--------------------------------------------------------------------
	print("-"*lenx)
	print ("Filename", filename)
	print ("Hostname", hostname)
	fileExist = "false"

	# File to use in cache
	filetouse = filename

	# Check if filename is a directory
	if filename[-1] == "/":
		filetouse += "index.html"

	try:
		# Check wether the file exist in the cache
		f = open(filetouse, "r")
		outputdata = f.readlines()
		fileExist = "true"
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send("HTTP/1.0 200 OK\r\n")

		# You might want to play with this part.  
		# It is not always html in the cache
		tcpCliSock.send("Content-Type:text/html\r\n")

		# Fill in start.

		# Fill in end.

		print('Read from cache')
	#---------------------------------------------------------------------
	# Error handling for file not found in cache
	except IOError:
		if fileExist == "false":
			# Create a socket on the proxyserver
			port = 80
			c = socket()
			host = gethostbyname(filename)
			c.connect((host,port)) 
			
			try:
				# Connect to the socket to port 80
				# Fill in start.
				print("Searching for host:",host)
				c.connect((host,port))
				# Fill in end.

				# Create a temporary file on this socket and ask port 80 for the file requested by the client
				fileobj = c.makefile('r', 0)
				print("File obj", fileobj)
				#write send to the server
				fileobj.write("GET "+"http://" + filename + " HTTP/1.0\nHost: "+hostname+ "\n\n")
				# Read the response into buffer
				msg = c.recv(10000)
				fread = fileobj.readlines()
				print(fread)
				# Fill in start.

				# Fill in end.

				# Create a new file in the cache for the requested file.
				# Create the directory structure if necessary.
				# Also send the response in the buffer to client socket and the corresponding file in the cache
				if not os.path.exists(filename):
					tmpFile = open("./" + filetouse,"wb")
				# Fill in start.

				# Fill in end.

			except:
				print ("Illegal request\n\n")
		else:
			# HTTP response message for file not found
			tcpCliSock.send("HTTP/1.0 404 sendErrorErrorError\r\n")
			tcpCliSock.close()
			# Fill in start.

			# Fill in end.

	# Close the client and the server sockets
	tcpCliSock.close()

tcpSerSock.close()
