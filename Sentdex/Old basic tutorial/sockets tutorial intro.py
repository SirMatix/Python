import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#who we wanna communicate with
server = 'pythonprogramming.net'

#which port we wanna communicate through
port = 80

#get server ip

server_ip = socket.gethostbyname(server)


print(s)
print(server_ip)

request = "GET / HTTP/1.1\nHost: " +server+"\n\n"
s.connect((server,port))
s.send(request.encode())
result = s.recv(4096) #buffer

#print(result)

#print buffering
while (len(result) > 0):
    print(result)
    result = s.recv(1024)
