import os,wx,warnings,requests
from tkinter import messagebox
warnings.filterwarnings('ignore')
isupdate = False

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
    os.system(('start python Downloadbs.py '+str(num))

def update():
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
            if i < 19:
                if 0 == len(programlist):
                    if isupdate:
                        updatebutton = wx.Button(panel, label='有新版本，点我更新', pos=(0,0+i*30))
                        updatebutton.Bind(wx.EVT_BUTTON,lambda e,mark='update':self.OnButton(e, mark))
                else:
                    buttonlist.append(wx.Button(panel, label=programlist[i]["name"], pos=(0,0+i*30)))
                    buttonlist[i].Bind(wx.EVT_BUTTON,lambda e,mark=i:self.OnButton(e, mark))
            else:
                if 0 == len(programlist):
                    if isupdate:
                        updatebutton = wx.Button(panel, label='有新版本，点我更新', pos=(50,i-20*30))
                        updatebutton.Bind(wx.EVT_BUTTON,lambda e,mark='update':self.OnButton(e, mark))
                else:
                    buttonlist.append(wx.Button(panel, label=programlist[i]["name"], pos=(50,i-20*30)))
                    buttonlist[i].Bind(wx.EVT_BUTTON,lambda e,mark=i:self.OnButton(e, mark))
        self.Centre()
    def OnButton(self,e,num):
        self.Destroy()
        if num == 'update':
            update()
        else:
            Download(num)
        
if not os.path.isfile('Downloadbs.py'):
    urldownload('http://github.com/huangzherui/Download/raw/zbhedit/py/Downloadbs.py','./Downloadbs.py')

versions = '1.0'#版本1.0

#打开marketmain.cfg
urldownload('https://github.com/huangzherui/Download/raw/zbhedit/marketmain.cfg','./marketmain.cfg')
with open('marketmain.cfg','r',encoding='utf8') as file:
    programlistraw = file.read()
    programlist = eval(programlistraw)


#检测版本
if programlist[0]["version"]  == versions:
    isupdate = True

#运行图形程序
app = wx.App()
sample = MainWindow(None)
sample.Show()
app.MainLoop()
