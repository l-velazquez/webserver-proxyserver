#-------------------------------------------------------------------------
#   Course: CCOM 4105
#   Profesor: Jose Ortiz
#   Programmer: Luis F. Velazquez Sosa
#   Student Number: 801-18-8580
#   Discription:
#         
#          
#-------------------------------------------------------------------------
from socket import *
#import sys


'''if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)'''

ADDRESS = "localhost"
PORT = 12001
lenx = 70
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((ADDRESS,PORT))
tcpSerSock.listen(5)

while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)

    message = tcpCliSock.recv(2048)
    # Fill in end.
    print(message)
    print("-" * lenx)
    print("\n")
    # Extract the filename from the given message

    print(message.split()[1])
    filename = (str(message.split()[1]).partition("/")[2]).split("'")[0]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        # Fill in start.
        # Fill in end.
        print('Read from cache')
        # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            port = 80
            c = socket()
            host = gethostbyname(filename)
            c.connect((host,port))
            # Fill in end.
            hostn = filename.replace("www.","",1)
            print(hostn)
            try:
                # Connect to the socket to port 80
                # Fill in start.
                # Fill in end.
                print("Searching for host:",host)
                print("The host name is:",hostn)
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = open(hostn,"w")
                fileobj.write("GET"+"http://"+filename+"HTTP/1.0\n\n")
                outdata = fileobj.read()

                print("File object", fileobj)
                print("Sending output:", outdata)

                c.send(outdata)
                # Read the response into buffer
                msg = c.recv(10000)
                print("The message of the website is", msg)
                fread = fileobj.read()
                buffer = []  
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename,"wb")
                # Fill in start.
                # Fill in end.
            except:
                print("Illegal request\n\n")
                print("-"*lenx)
        else:
            c.send('HTTP/1.0 404 Not Found\r\n'.encode())
            c.close()

            # HTTP response message for file not found
            # Fill in start.
            # Fill in end.
    # Close the client and the server sockets
    tcpCliSock.close()
# Fill in start.
# Fill in end.
