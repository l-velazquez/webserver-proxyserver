#Run code using Python 2.7.18



from distutils.log import debug
from socket import *
import os
import sys

if len(sys.argv) <= 1:
	print 'Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server'
	sys.exit(2)

ADDRESS = sys.argv[1]
PORT = int(sys.argv[2])
lenx = 70
debug = 0


print "-"*lenx
print "Server address at",ADDRESS
print "Port:", PORT
print "-"*lenx
print "*"*lenx
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((ADDRESS,PORT))
tcpSerSock.listen(5)

while 1:

	# Start receiving data from the client
	print "-"*lenx
	print '\nReady to serve...'
	tcpCliSock, addr = tcpSerSock.accept()
	print 'Received a connection from:', addr
	message = tcpCliSock.recv(4096) 			# Fill in end.
	

	# Extract the filename and hostname from the given message
	filename1 = message.split()[1].partition("/")[2]
	filename2 = filename1.split("/")[0]
	hostname = filename2[0]
	if len(filename2) > len(hostname):
		hostname = filename2	
	
	#filename = "/".join(filename[1:])
	if debug:
		print message
		print message.split()[1]
		print "filename1", filename1
		print "filename2", filename2
		print "Filename", filename2
		print "Hostname", hostname
	fileExist = "false"

	# File to use in cache
	filetouse = filename2

	# Check if filename is a directory
	if filename2[-1] == "/":
		filetouse += "index.html"

	try:
		# Check wether the file exist in the cache
		f = open(filetouse, "r")
		outputdata = f.readlines()
		fileExist = "true"
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send("HTTP/1.0 200 OK\r\n")
		# You might want to play with this part.  It is not always html in the cache
		tcpCliSock.send("Content-Type:text/html\r\n")

		# Fill in start.

		# Fill in end.

		print 'Read from cache'
	# Error handling for file not found in cache
	except IOError:
		if fileExist == "false":
			# Create a socket on the proxyserver
			c = socket()# Fill in start. 			# Fill in end.
			port = 80
			host = gethostbyname(hostname)
			c.connect((host,port))
			try:
				# Create a temporary file on this socket and ask port 80 for the file requested by the client
				#fileobj = c.makefile('r', 0)
				#fileobj.write("GET "+"http://" + filename2 + " HTTP/1.0\nHost: "+hostname+ "\n\n")
				c.sendall(("GET "+"http://" + filename2 + " HTTP/1.0\nHost: "+hostname+ "\n\n").encode())
				#outfile = fileobj.read()
				#print "Output data is:\n","-"*lenx,"\n",outfile
				# Read the response into buffer
				while 1:
					out = c.recv(4096)
					print "Output: ",out
					if len(out) > 0:
						tcpCliSock.send(out.encode())
					else:
						break
				# Fill in start.

				# Fill in end.

				# Create a new file in the cache for the requested file.
				# Create the directory structure if necessary.
				# Also send the response in the buffer to client socket and the corresponding file in the cache
				'''if not os.path.exists(filename):
   					os.makedirs(os.path.dirname(filename))

				tmpFile = open("./" + filetouse,"wb")'''
				# Fill in start.

				# Fill in end.
				c.close()

			except:
				print "Illegal request"
		else:
			# HTTP response message for file not found
			tcpCliSock.send("HTTP/1.0 404 sendErrorErrorError\r\n")
			# Fill in start.

			# Fill in end.

	# Close the client and the server sockets
	tcpCliSock.close()

tcpSerSock.close()
