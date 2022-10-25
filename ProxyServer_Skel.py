#Run code using Python 2.7.18


from socket import *
import os
import sys
import tempfile

if len(sys.argv) <= 1:
	print 'Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server'
	sys.exit(2)

ADDRESS = sys.argv[1]
PORT = int(sys.argv[2])
lenx = 75
debug = 0 #meant to debug the code

#formating for the terminal

print("\nProgram by: Luis Fernando Javier Velazquez Sosa")
print "-"*lenx
print "\t\t\tProxy server address at:",ADDRESS
print "\t\t\tPort:", PORT
print "\t\t\t",ADDRESS,":",PORT
print "-"*lenx
print "|"*lenx

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((ADDRESS,PORT))
tcpSerSock.listen(5)

while 1:

	# Start receiving data from the client
	print "-"*lenx
	print '\nReady to serve...\a'
	tcpCliSock, addr = tcpSerSock.accept()
	print 'Received a connection from:', addr
	message = tcpCliSock.recv(4096) 			# Fill in end.
	

	# Extract the filename and hostname from the given message
	filename1 = message.split()[1].partition("/")[2]
	filename2 = filename1.split("/")[0]
	hostname = filename2[0]
	if len(filename2) > len(hostname):
		hostname = filename2	
	fileExist = "false"
	if filename2.split(".")[0]=="www":
		filetouse = filename2.split(".")[1]
	else:
		filetouse = filename2.split(".")[0]
	#filename = "/".join(filename[1:])
	if debug:
		print message
		print message.split()[1]
		print "filename1", filename1
		print "filename2", filename2
		print "Filename", filename2
		print "Hostname", hostname
		print "file to use:",filetouse
	

	# File to use in cache
	

	# Check if filename is a directory
	if filename2[-1] == "/":
		filetouse += "index.html"

	try:
		# Check wether the file exist in the cache
		f = open(filetouse, "r")
		outputdata = f.readlines()
		print"Reading the file",filetouse 
		fileExist = "true"
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send("HTTP/1.0 200 OK\r\n")
		# You might want to play with this part.  It is not always html in the cache
		tcpCliSock.send("Content-Type:text/html\r\n")
		for line in f:
			tcpCliSock.send(line)

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
			if debug:
				print("Host info:",host)
			c.connect((host,port))

			try:
				# Create a temporary file on this socket and ask port 80 for the file requested by the client
				#fileobj = c.makefile('r', 0)
				#fileobj.write("GET "+"http://" + filename2 + " HTTP/1.0\nHost: "+hostname+ "\n\n")
				c.sendall(("GET "+"http://" + filename2 + " HTTP/1.0\nHost: "+hostname+ "\n\n").encode())
				#outfile = fileobj.read()
				#print "Output data is:\n","-"*lenx,"\n",outfile
				# Read the response into buffer
				fileobj = open("tmpfile","w")
				out = None
				while 1:
					out = c.recv(4096)
						
					if len(out) > 0:
						tcpCliSock.send(out.encode())#sending to the client
						fileobj.write(out)
					else:
						fileobj.write(out)#writes out the last bytes of information
						fileobj.close #closes file
						break #breaks while loop
				
				if debug: #to view out put
					print "The output is: ", out				# Fill in end.

				# Create a new file in the cache for the requested file.
				# Create the directory structure if necessary.
				# Also send the response in the buffer to client socket and the corresponding file in the cache
				#'''
				

				if os.path.isdir(filename2):
					os.makedirs(os.path.dirname(filename2))

				fileobj2 = open("tmpfile","r")
				tmpFile = open(filetouse,"w")
				
				for line in fileobj2:
					tmpFile.write(line)
				
				
				#'''
				tmpFile.close()
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
