import requests,warnings,sys,os
warnings.filterwarnings('ignore')

def urldownload(url,filename):#下载文件
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)

#打开marketmain.cfg
with open('marketmain.cfg','r',encoding='utf8') as file:
    programlistraw = file.read()
    programlist = eval(programlistraw)

#变量设置
mode = sys.argv[1]
AID = int(sys.argv[2])
username = os.getenv('username')
filename = str(programlist[AID]["name"])
path = ('C:/Users/'+username+'/AppData/Local/ZHMarketDownload/')+filename+'/'

if not mode == 'open':
    #打开zhmarket.db
    with open('zhmarket.db','r',encoding='utf8') as file:
        alreadyprogramraw = file.read()
        if alreadyprogramraw == '':
            alreadyprogram = []
        else:
            alreadyprogram = eval(alreadyprogramraw)

        if mode == 'update':
            for i in range(len(alreadyprogram)):
                if int(alreadyprogram[i]['AID']) == AID:
                    alreadyprogram[i]['version'] = programlist[AID]['version']
                    break
        elif mode == 'download':
            alreadyprogram.append({'AID':('%04d' % AID),'version':programlist[AID]['version']})
    with open('zhmarket.db','w',encoding='utf8') as file:
        file.write(str(alreadyprogram))

    #检测文件夹
    if not os.path.exists(('C:/Users/'+username+'/AppData/Local/ZHMarketDownload')):
        os.makedirs(('C:/Users/'+username+'/AppData/Local/ZHMarketDownload'))
    if not os.path.exists(path):
        os.makedirs(path) 

    urldownload('http://github.com/huangzherui/Download/raw/zbhedit/zip/7z.dll',(path+'7z.dll'))
    urldownload('http://github.com/huangzherui/Download/raw/zbhedit/zip/7z.exe',(path+'7z.exe'))

    for i in range(programlist[AID]["spilttotal"]):
        s = '%03d' % int(i+1)
        down_url = programlist[AID]["downloadurl"]
        down_url = down_url.replace('$Appname',filename)
        down_url = down_url.replace('$spiltnum',s)
        urldownload(down_url,(path+filename+'.7z.'+s))
    os.system(('powershell cd '+path+';./7z.exe x '+filename+'.7z.001'))
    for i in range(programlist[AID]["spilttotal"]):
        s = '%03d' % int(i+1)
        os.system(('powershell del '+path+filename+'.7z.'+s))
os.system(('powershell cd '+path+';start '+path+filename+'.exe'))