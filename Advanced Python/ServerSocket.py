import socket


def server_program():
    # get the hostname
    host = socket.gethostname()#192.136.127.0 127.0.0.1
    port = 5000

    server_socket = socket.socket()  # get instance
    
    server_socket.bind((host, port))  # bind host address and port together

    
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()#base64 encoded
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()