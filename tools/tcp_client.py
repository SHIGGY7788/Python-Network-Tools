import socket

def init():
    ##TCP CLIENT

    HOST = str(input("Please enter host IP: "))
    PORT = int(input("Please enter host port: "))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client.sendto(b"Message to server", (HOST, PORT))

    client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
    response = client.recv(1024)
    print(response.decode('utf-8'))

    print("Process finished, closing client.")
    client.close()
