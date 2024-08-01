import os,wx,warnings,requests
from tkinter import messagebox
warnings.filterwarnings('ignore')

def urldownload(url,filename):#下载文件
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)

def Download(num):#下载
    filename = filelist[num].strip('\n')
    os.makedirs(filename)
    messagebox.showinfo('提示','下载中……')
    os.system(('start python Downloadfile.py '+filename))

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
        for i in range(len(filelist)-1):
            if i < 20:
                buttonlist.append(wx.Button(panel, label=filelist[i], pos=(0,0+i*30)))
                buttonlist[i].Bind(wx.EVT_BUTTON,lambda e,mark=i:self.OnButton(e, mark))
            else:
                buttonlist.append(wx.Button(panel, label=filelist[i], pos=(50,i-20*30)))
                buttonlist[i].Bind(wx.EVT_BUTTON,lambda e,mark=i:self.OnButton(e, mark))
        self.Centre()
    def OnButton(self,e,num):
        self.Destroy()
        Download(num)

if not os.path.isfile('Downloadfile.py'):
    with open('Downloadfile.py','w') as file:
        file.write('''import requests,warnings,sys,os                   
filename = sys.argv[1]
warnings.filterwarnings('ignore')
down_res = requests.get(url=url,verify=False)
if not os.path.exists(filename):
    file = open(filename,'a')
    file.close()
with open(filename,'wb') as file:
    file.write(down_res.content)''')
        
if not os.path.isfile('Downloadbs.py'):
    with open('Downloadbs.py','w') as file:
        file.write('''import requests,warnings,sys,os
url = sys.argv[1]                   
filename = sys.argv[2]
warnings.filterwarnings('ignore')
def urldownload(url,filename):
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)
urldownload(('http://github.com/huangzherui/Download/raw/main/zip/'+filename+'.7z.001'),('./'+filename+'/'+'.7z.001'))
urldownload(('http://github.com/huangzherui/Download/raw/main/zip/'+filename+'.7z.002'),('./'+filename+'/'+'.7z.002'))
urldownload('http://github.com/huangzherui/Download/raw/main/zip/7z.dll',('./'+filename+'/'+'7z.dll'))
urldownload('http://github.com/huangzherui/Download/raw/main/zip/7z.exe',('./'+filename+'/'+'7z.exe'))
os.system(('cd '+filename+'&&copy /b '+filename+'.7z.00* '+filename+'.7z&&7z x '+filename+'.7z'))''')

versions = '1.0'#版本1.0

#打开Download.txt
urldownload('http://github.com/huangzherui/Download/raw/main/Download.txt','./Download.txt')
with open('Download.txt','r',encoding='utf8') as file:
    filelist = file.readlines()

#检测版本
if not filelist[len(filelist)-1].strip('\n') == versions:
    with open('DownloadDownload.py','w') as file:
        file.write('''import requests,os,warnings
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
quit()''')
    os.system("start python DownloadDownload.py")
    quit()

#运行图形程序
app = wx.App()
sample = MainWindow(None)
sample.Show()
app.MainLoop()
