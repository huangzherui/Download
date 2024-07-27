import requests,os
def urldownload(url,filename):#下载文件
    down_res = requests.get(url)
    try:
        with open(filename,'wb') as file:
            file.write(down_res.content)
    except:
        file = open(filename,'a')
        file.close()
        with open(filename,'wb') as file:
            file.write(down_res.content)
urldownload('https://github.com/huangzherui/Download/raw/main/py/Download.py','Download.py')
os.system("python Download.py")
