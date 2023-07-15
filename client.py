import socket
import os
import shutil
from Crypto.Cipher import AES
key=b"OppenHeimer"
indila=b"CilianMurphy"

cipher=AES.new(key, AES.MODE_EAX,indila)

IP = socket.gethostbyname(socket.gethostname())
PORT = 9991
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024000

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    while True:
        message=client.recv(SIZE).decode(FORMAT)
        username=input(message)
        client.send(username.encode(FORMAT))
        message=client.recv(SIZE).decode(FORMAT)
        client.send(input(message).encode(FORMAT))
        text=client.recv(SIZE).decode(FORMAT)
        if text == "LOGIN SUCCESSFULL":
            print(text)
            ch=input("MENU:1.upload\n2.download\n3./quit)")
            client.send(ch.encode(FORMAT))
            msg1=client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg1}")
            if ch == "upload":
                print("\n available files in your directory ")
                print(os.listdir('client_files/'))
                fname=input("Enter file Name")
                filepath=os.path.join("client_files", fname)
                file = open(filepath, "rb")
                data = file.read()
                client.send(fname.encode(FORMAT))
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER]: {msg}")

                """ Sending  file data to  server. """
                encrypted=cipher.encrypt(data)
                client.send(encrypted)
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER]: {msg}")
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER]: File stored as {msg}")
                file.close()
                os.remove(filepath)
                break
            elif ch == "download":
                fname1=input("Enter file to be extracted (zip format)")
                """Sending  filename to server"""
                client.send(fname1.encode(FORMAT))
                msg2=client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER]: {msg2}")
                
                filename1=client.recv(SIZE).decode(FORMAT)
                client.send("Decompressed file name ".encode(FORMAT))

                # print(filename1)

                act2_file_path=os.path.join("client_files", filename1)
                file2 = open(act2_file_path, "wb")

                data = client.recv(SIZE)
                file2.write(cipher.decrypt(data))
                client.send("received file data".encode(FORMAT))
                file2.close()
                break
            elif ch == "quit":
                break
            else:
                print("Invalid Choice")
                break
                
        else:
            print(text)
            break

    client.close()


if __name__ == "__main__":
    main()