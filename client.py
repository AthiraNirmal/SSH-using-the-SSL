import socket
import ssl
import sys
from iplookup import iplookup

hostname = sys.argv[1]
ip_addr = socket.gethostbyname(hostname)
server_sni_hostname = 'Athira'

server_cert = 'server.crt'
client_cert = 'client.crt'
client_key = 'client.key'

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)
context.load_cert_chain(certfile=client_cert, keyfile=client_key)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(s, server_side=False, server_hostname=server_sni_hostname)
conn.connect((ip_addr, int(sys.argv[2])))

while True :
    command = input("ssh>")
    conn.write(command.encode())
    data = conn.read()
    print (data.decode())
