import socket, ssl
import sys
import subprocess
import threading 


server_cert = 'server.crt'
server_key = 'server.key'
client_certs = 'client.crt'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.load_verify_locations(cafile=client_certs)

bindsocket = socket.socket()
bindsocket.bind(('', int(sys.argv[1])))
bindsocket.listen()


newsocket, fromaddr = bindsocket.accept()
conn = context.wrap_socket(newsocket, server_side=True)

while True:
    command = conn.read()
    if command.decode() in ["exit"]:
        conn.write("Closing connection".encode())
        subprocess.run("exit 1", shell=True, check=True)
    elif command.decode() in ["ls"] or command.decode() in ["pwd"]:
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output= proc.stdout.read()+proc.stderr.read()
        conn.write(output)
    else:
        message="Invalid Command"
        conn.write(message.encode())
    
