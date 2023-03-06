# SSH-using-the-SSL
Implementing a simple secure socket shell (SSH) using the Secure Socket Layer (SSL). SSL is used to establish a secure connection between the server and the client.

Upon connecting to the server, the client prints ssh >, which allows the user to execute the following commands.
ssh > ls //list files and sub-directories under the current directory
ssh > pwd //print the working directory of the server
ssh > exit // ends the SSH session
If a user enters a command other than the above, then print “Invalid Command”.

First generate a public key certificate in order to establish the ssl connection!

Create server certificate:
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt

Create client certificate:
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout client.key -out client.crt

Install iplookup: pip install iplookup
