#!/usr/bin/python3
#By purplet
import requests
import threading
def ipScanner(ip,payloads):
    try:
        url = "http://"+ip+payloads
        res = requests.get(url,timeout=6).status_code
        if res == 200:
            if int(choose) == 3:
                if url == self_url.rstrip('/')+':'+self_port:
                    url = url.replace(url,'').strip()
                print(url)
                file = open("ip.txt",'a')
                file.write(url+"\n")
                file.close()
            else:
                print(url)
                file = open("ip.txt",'a')
                file.write(url+"\n")
                file.close()
    except:
        pass
def C_Scan(ips,payloads):
    for c in range(1,256):
        ipt = ips+str(c)
        t = threading.Thread(target=ipScanner,args=(ipt,payloads))
        t.start()
def B_Scan(ips,payloads):
    for b in range(1,256):
        ipt = ips.split('.')
        ipt[2] = b
        ip = str(ipt[0])+'.'+str(ipt[1])+'.'+str(ipt[2])+'.'+str(ipt[3])
        t = threading.Thread(target=ipScanner,args=(ip,payloads))
        t.start()
def Port_Scan(ips,ports):
    ports = ports.split('-')
    for p in range(int(ports[0]),int(ports[1])):
        p = ':'+str(p)
        t = threading.Thread(target=ipScanner,args=(ips,p))
        t.start()
if __name__ == '__main__':
    print('该脚本运行完会在当前目录下生成ip.txt保存目标机器IP')
    global self_url
    self_url = input("请输入自己网站的IP,Input example:http://192.168.194.147/\n")
    choose = input('请选择扫描方式：1.C段扫描 2.B段扫描 3.端口扫描\n')
    if(int(choose) == 1):
        ip = str(str(self_url.split('.')[0]).split('//')[1])+'.'+str(self_url.split('.')[1])+'.'+str(self_url.split('.')[2])+'.'
        print(ip)
        payloads = ':80'
        C_Scan(ip, payloads)  # C段IP使用
    if (int(choose) == 2):
        ip = str(str(self_url.split('.')[0]).split('//')[1])+'.'+str(self_url.split('.')[1])+'..'+str(self_url.split('.')[3]).rstrip('/')
        print(ip)
        payloads = ':80'
        B_Scan(ip, payloads)  # B段IP使用
    if (int(choose) == 3):
        ip = str(str(self_url.split('.')[0]).split('//')[1])+'.'+str(self_url.split('.')[1])+'.'+str(self_url.split('.')[2])+'.'+str(self_url.split('.')[3]).rstrip('/')
        ports = input('请选择端口范围Input example:8801-8850\n')
        global self_port
        self_port = input("请输入自己网站端口\n")
        Port_Scan(ip,ports)