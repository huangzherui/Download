import requests,warnings,sys,os
with open('marketmain.cfg','r',encoding='utf8') as file:
    programlistraw = file.read()
    programlist = eval(programlistraw)
filename = str(programlist[int(sys.argv[1])]["name"])
if not os.path.exists('C:/Program Files/Download'):
    os.makedirs('C:/Program Files/Download')
path = 'C:/Program Files/Download'+filename
if not os.path.exists(path):
    os.makedirs(path) 
           

warnings.filterwarnings('ignore')
def urldownload(url,filename):
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)
urldownload('http://github.com/huangzherui/Download/raw/zbhedit/zip/7z.dll',(path+'/7z.dll'))
urldownload('http://github.com/huangzherui/Download/raw/zbhedit/zip/7z.exe',(path+'/7z.exe'))
for i in range(programlist[int(sys.argv[1])]["spilttotal"]):
    s = '%03d' % int(i+1)
    down_url = programlist[int(sys.argv[1])]["downloadurl"]
    down_url = down_url.replace('$Appname',filename)
    down_url = down_url.replace('$spiltnum',s)
    urldownload(down_url,(path+filename+'.7z.'+s))
os.system(('cd '+path+'&&copy /b '+filename+'.7z.00* '+filename+'.7z&&7z x '+filename+'.7z'))
