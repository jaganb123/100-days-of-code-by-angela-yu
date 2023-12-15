import _thread
import socket

IPADDR = socket.gethostbyname(f"{socket.gethostname()}.local")
PORT = 5050
print(f"[SERVER] IPADDR is {IPADDR}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((IPADDR, PORT))

except socket.error as e:
    str(e)

server.listen(2)

def handle_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()

def connection():
    while True:
        conn, addr = server.accept()
        print("Connected to:", addr)
        _thread.start_new_thread(handle_client, (conn,))

connection()