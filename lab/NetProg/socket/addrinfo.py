import sys, socket

result = socket.getaddrinfo("www.unipr.it", None, 0, socket.SOCK_STREAM)

for item in result:
#    print (item)
    print (item[4][0])
