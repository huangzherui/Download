import os,wx,warnings,requests
from tkinter import messagebox
warnings.filterwarnings('ignore')
isupdate = False
def webdbget(user,password,tag):
    import requests
    postdata = {'user':user,'secret':password,'action':'get','tag':tag}
    r = requests.post('http://tinywebdb.appinventor.space/api',data=postdata)
    temp = r.text
    temp1 = eval(temp)[tag]
    return temp1
def urldownload(url,filename):#下载文件
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)

def Download(num):#下载
    #os.makedirs(filename)
    messagebox.showinfo('提示','下载中……')
    os.system(('start python Downloadbs.py '+str(num)))

def update():#更新
    urldownload('http://github.com/huangzherui/Download/raw/zbhedit/py/DownloadDownload.py','./DownloadDownload.py')
    os.system("start python DownloadDownload.py")
    quit()

#图形化类
class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)
        self.InitUi()
    def InitUi(self):
        self.SetTitle("下载")
        self.SetSize(400, 600)
        panel = wx.Panel(self)
        buttonlist = []
        for i in range(len(programlist)):
            if i == 0:
                if isupdate:
                    buttonlist.append(wx.Button(panel, label='有新版本，点我更新', pos=(0,0)))
                    buttonlist[i].Bind(wx.EVT_BUTTON,lambda e,mark='update':self.OnButton(e, mark))
                else:
                    buttonlist.append(wx.Button(panel, label=programlist[i+1]["name"], pos=(0,0)))
                    buttonlist[i].Bind(wx.EVT_BUTTON,lambda e,mark=i+1:self.OnButton(e, mark))
            else:
                try:
                    buttonlist.append(wx.Button(panel, label=programlist[i+(0 if isupdate else 1)]["name"], pos=(0,0+i*30)))
                except:
                    break
                if i < 19:#第一列
                    buttonlist[i].Bind(wx.EVT_BUTTON,lambda e,mark=i+(0 if isupdate else 1):self.OnButton(e, mark))
                else:#第二列
                    buttonlist[i].Bind(wx.EVT_BUTTON,lambda e,mark=i:self.OnButton(e, mark))
        self.Centre()
    def OnButton(self,e,name):
        self.Destroy()
        if name == 'update':
            update()
        else:
            Download(name)
        
if not os.path.isfile('Downloadbs.py'):
    urldownload('http://github.com/huangzherui/Download/raw/zbhedit/py/Downloadbs.py','./Downloadbs.py')

versions = 1.0#版本1.0

#打开marketmain.cfg
#urldownload('https://github.com/huangzherui/Download/raw/zbhedit/marketmain.cfg','./marketmain.cfg')
with open('marketmain.cfg','w',encoding='utf8') as file:
    programlist = webdbget('zhmarket','9d6ef697','marketapps')
    file.write(str(programlist))


#检测版本
if programlist[0]["version"] > versions:
    isupdate = True
    print(isupdate)

#运行图形程序
app = wx.App()
sample = MainWindow(None)
sample.Show()
app.MainLoop()
