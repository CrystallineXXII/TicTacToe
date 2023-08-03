import socket
import threading

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 5555
SERVER = '192.168.29.33'


board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# Bind the socket to the port
server.bind((SERVER, PORT))

def check_if_valid(move):
    if move [0] in ['1', '2', '3'] and move[1] in ['1', '2', '3']:
        if board[int(move[0])-1][int(move[1])-1] == 0:
            return True
        else:
            return False
    else:
        return False
    
def check_if_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return True
        elif board[0][i] == board[1][i] == board[2][i] != 0:
            return True
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    return False

def check_if_tie():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True

def print_board():
    for i in range(3):
        print(board[i])

def handle_client(conn, addr, player):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        move = conn.recv(1024).decode()
        if move == 'quit':
            connected = False
            break
        if check_if_valid(move):
            board[int(move[0])-1][int(move[1])-1] = player
            if check_if_win():

                break
            elif check_if_tie():

                break



        print_board()
        conn.send(str.encode(str(board)))
          
    conn.close()