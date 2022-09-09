from socket import *
import sys

if __name__ == "__main__":
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.connect((sys.argv[1], int(sys.argv[2])))
        while(1):
            value = input("Please enter a string:\n") + "\n"
            s.sendall(value.encode())
            #data = s.recv(1024)

    print(f"Received {data!r}")
