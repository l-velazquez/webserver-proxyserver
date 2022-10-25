#Web server and Proxy server

Course: CCOM 4105
Profesor: Jose Ortiz
Programmer: Luis F. Velazquez Sosa
Student Number: 801-18-8580

Discription: This program will create a web server and a proxy server. The file index.html is what the client will see. If you want to change of the html file that will be displayed to the client (browser). The proxy server is meant to be the caching part that will halp with the speed of accessing the web pages.



Run the file webserver.py in the termainal 

    python3 webserver.py

You can access the webserver by using the broweser client by writing in the web browser 

    localhost:12000 or ip-address-of-server:12000

To connect to the server just put the ip address of the server into the  browser or if running in the same machine you are runnging the server just put localhost as the ip.


For the proxy server you should run the server:it in you browser by writing:

    python ProxyServer_Skel.py <ip-address> <port>

To access the proxy server you write in your browser:

    localhost:<port>/httpforever.com

Bugs-------------------------------------------------------------------------------------------
There are still bug with the code, the page is cached but can't be sent to the client. Blank page appears.
Also cache files are created in the same directory as the code. This will need to be fix for better organization when accessing the files.