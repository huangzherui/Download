import requests,warnings,sys,os                 
filename = sys.argv[1]
warnings.filterwarnings('ignore')
def urldownload(url,filename):
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)
urldownload(('http://github.com/huangzherui/Download/raw/zbhedit/zip/'+filename+'.7z.001'),('./'+filename+'/'+filename+'.7z.001'))
urldownload(('http://github.com/huangzherui/Download/raw/zbhedit/zip/'+filename+'.7z.002'),('./'+filename+'/'+filename+'.7z.002'))
urldownload('http://github.com/huangzherui/Download/raw/zbhedit/zip/7z.dll',('./'+filename+'/'+'7z.dll'))
urldownload('http://github.com/huangzherui/Download/raw/zbhedit/zip/7z.exe',('./'+filename+'/'+'7z.exe'))
os.system(('cd '+filename+'&&copy /b '+filename+'.7z.00* '+filename+'.7z&&7z x '+filename+'.7z'))
