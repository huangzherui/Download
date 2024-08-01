import requests,warnings,sys,os                   
filename = sys.argv[1]
warnings.filterwarnings('ignore')
down_res = requests.get(url=url,verify=False)
if not os.path.exists(filename):
    file = open(filename,'a')
    file.close()
with open(filename,'wb') as file:
    file.write(down_res.content)