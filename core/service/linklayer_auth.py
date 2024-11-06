import os
import socket
import threading
import duckdb
import time
class Authenticator:

    def __init__(self,path:str,conn:duckdb.DuckDBPyConnection):
        self.path = path
        self.conn:duckdb.DuckDBPyConnection = conn

    def handle_connn(self,sockClient:socket.socket):
        try:
            reader = sockClient.makefile()
            username = reader.readline()
            password = reader.readline()
            username = username.strip()
            password = password.strip()
            
            exists =self.conn.execute("select expdisable,expire from users where username=? and password=?",(username,password)).fetchall()
            if len(exists) == 0:
                sockClient.sendall(bytes([0]))
            else:
                expdisable = exists[0][0]
                expire = exists[0][1]
                now = int(time.time())
                if not expdisable and now > expire:
                    sockClient.sendall(bytes([0]))
                else:
                    sockClient.sendall(bytes([1]))
            sockClient.close()
            print("no problem")
        except Exception as e:
            print(e)

    def start_server(self):
        if os.path.exists(self.path):
            os.remove(self.path)
        sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
        sock.bind(self.path)
        os.chmod(self.path,777)
        sock.listen(1)
        print("unix auth on "+self.path)
        while True:
            (sockClient,addr) = sock.accept()
            t = threading.Thread(target=self.handle_connn,args=(sockClient,))
            t.start()

