import socket

PORT = 5555
SERVER = '192.168.29.33'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def print_board(board):
    for i in range(3):
        print(board[i])

def send(msg):
    message = msg.encode('utf-8')
    client.send(message)

def receive():
    msg = client.recv(1024).decode('utf-8')
    return msg

def main():
    move = input("Enter your move: ")
    send(move)
    print(receive())
    
