import requests,warnings,sys,os
with open('marketmain.cfg','r',encoding='utf8') as file:
    programlistraw = file.read()
    programlist = eval(programlistraw)
filename = programlist[sys.argv[1]]["version"]
os.makedirs(filename)            

warnings.filterwarnings('ignore')
def urldownload(url,filename):
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)
urldownload('http://github.com/huangzherui/Download/raw/zbhedit/zip/7z.dll',('./'+filename+'/'+'7z.dll'))
urldownload('http://github.com/huangzherui/Download/raw/zbhedit/zip/7z.exe',('./'+filename+'/'+'7z.exe'))
for i in range(programlist[sys.argv[1]]["spilttotal"]):
    s = '%03d' % i+1
    down_url = programlist[sys.argv[1]]["downloadurl"]
    down_url.replace('$Appname',filename)
    down_url.replace('$spiltnum',s)
    urldownload(down_url,('./'+filename+'/'+filename+'.7z.'+s))
os.system(('cd '+filename+'&&copy /b '+filename+'.7z.00* '+filename+'.7z&&7z x '+filename+'.7z'))
