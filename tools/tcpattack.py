from tcping import Ping
from threading import Thread


def init():
    def create_threads():
        openThreads = []
        for i in range(0, threadCount):
            th = Thread(target=ping_server)
            openThreads.append(th)
            th.start()
        print('Threads Created: ' + str(len(openThreads)))
        return openThreads

    def ping_server():
        runCount = 0
        while runCount < runtime:
            ping = Ping(HOST, PORT, 60)
            ping.ping(1)
            runCount += 1

    threadCount = int(input("Thread count: "))
    runtime = int(input("Runtime: "))
    HOST = str(input("Host IP: "))
    PORT = int(input('Host Port: '))
    create_threads()
