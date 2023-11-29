import socket


def init():
    HOST = str(input("Please enter HOST IP: "))
    PORT = int(input("Please enter the hosts PORT: "))

    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send sample data
    client.sendto(b"AAABBBCCC", (HOST, PORT))

    # Receive some data
    data, address = client.recvfrom(4096)
    print(data.decode('utf-8'))
    print(address.decode('utf-8'))

    print("Data received, closing")
    client.close()
