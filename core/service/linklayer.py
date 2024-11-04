
from enum import Enum
from io import TextIOWrapper
import signal
import subprocess
from typing import IO
from entity.linklayer import Config
import jsons
import os
import threading
class Linklayer_status(Enum):
    OFF = "off"
    STARTING = "starting"
    ON = "on"

class LinkLayer:
    

    def __init__(self):
        self.status = Linklayer_status.OFF
        self.process:subprocess.Popen = None

    def discard(self,io:IO):
        while True:
            algo = io.readline().decode("utf-8").strip()
            if algo == "":
                break

    def get_service_status(self) -> Enum:
        return  self.status

    async def start_service(self,service_config:Config)-> bool:
        try:
            self.status = Linklayer_status.STARTING
            linklayer_binary = os.path.abspath("binary")
            raw =jsons.dumps(service_config.__dict__)
            log_file = open("log.txt","w")
            f = open(linklayer_binary+"/cfg/config.json","w")
            f.write(raw)
            f.close()
            started_service = False
            
            self.process = subprocess.Popen([linklayer_binary+"/server","-cfg",linklayer_binary+"/cfg/config.json"]
                                            ,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=linklayer_binary)
            while True:
                line = self.process.stdout.readline().decode("utf-8").strip()
                if line == "":
                    break
                log_file.write(line+"\n")
                log_file.flush()
                if "Server started :D" in line:
                    started_service = True
                    break

            #if fail and cant start server, read stderr 
            if not started_service:
                while True:
                    line = self.process.stderr.readline().decode("utf-8").strip()
                    if line == "":
                        break
                    log_file.write(line+"\n")
                    log_file.flush()

            log_file.close()        
            if started_service:
                t1 = threading.Thread(target=self.discard,args=(self.process.stdout))
                t2 = threading.Thread(target=self.discard,args=(self.process.stderr))
                t1.start()
                t2.start()
                self.status = Linklayer_status.ON
            else:
                self.status = Linklayer_status.OFF    
            return started_service
        except Exception as e:
            print(e)
            return False
        
        

    def stop_service(self):
        if not self.process == None:
            self.process.kill()
            self.process.wait()
            self.process = None
        
        
        self.status = Linklayer_status.OFF
        