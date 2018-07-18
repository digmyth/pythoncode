# 没有找到正确批量下载rpm包的命令，自己写了一段代码实现

# 方法一：   自己写了一个包列表，可以基于这个包列表批量wget

# download_rpm.py
import requests
import re,os
from bs4 import BeautifulSoup
save_file = 'pk.txt'

if os.path.exists(save_file):
    os.remove(save_file)

url = 'http://mirrors.163.com/centos/7.4.1708/os/x86_64/Packages/'
rep = re.compile('^\w')
r1 = requests.get(url=url)
obj = BeautifulSoup(r1.text,'html.parser')
tag_a = obj.find_all(name='a',text=rep)

f = open(save_file,'a')
for i in tag_a:
    half_pk = i.attrs.get('href')
    pk = url + half_pk + "\n"
    f.write(pk)
f.close()


# 方法二：requests完全实现下载

import requests 
import re,os
from bs4 import BeautifulSoup

def download(full_url,half_pk):
    import requests
    resource = requests.get(url=full_url, stream=True)
    if os.path.exists(half_pk):
        os.remove(half_pk)
    with open(half_pk, mode="wb") as f:
       for chunk in resource.iter_content(chunk_size=10240): # 10KB
           f.write(chunk)
    return None

url = 'http://mirrors.163.com/centos/7.4.1708/os/x86_64/Packages/'
rep = re.compile('^\w')
r1 = requests.get(url=url,)

obj = BeautifulSoup(r1.text,'html.parser')
tag_a = obj.find_all(name='a',text=rep)

for i in tag_a:
    half_pk = i.attrs.get('href')  # 取属性才对
    full_url = url + half_pk
    download(full_url,half_pk)
    
# 有一些想法，想对上面代码优化，然后代码就这样了
import requests  # 代码未验证
import re,os 
from bs4 import BeautifulSoup
url = 'http://mirrors.163.com/centos/7.4.1708/os/x86_64/Packages/'

def download(full_url,half_pk):
    import requests
    resource = requests.get(url=full_url, stream=True)
    if os.path.exists(half_pk):
        os.remove(half_pk)
    with open(half_pk, mode="wb") as f:
       for chunk in resource.iter_content(chunk_size=10240): # 10KB
           f.write(chunk)
    return None

def getall_tag_a():
    rep = re.compile('^\w')
    r1 = requests.get(url=url,)
    obj = BeautifulSoup(r1.text,'html.parser')
    tag_a = obj.find_all(name='a',text=rep)
    # return tag_a
    for x in tag_a:
        yield x

for a in getall_tag_a():
    half_pk = a.attrs.get('href')  # 取属性才对
    full_url = url + half_pk
    download(full_url,half_pk)
    
    
    
#!/usr/bin/env python3  # 代码经验证完好
import threading
import requests
import re,os
from bs4 import BeautifulSoup
url = 'http://mirrors.163.com/centos/7.4.1708/os/x86_64/Packages/'

def download(full_url,half_pk):
    import requests
    if os.path.exists(half_pk):
        os.remove(half_pk)
    resource = requests.get(url=full_url, )
    resource.raise_for_status()
    with open(half_pk, mode="wb") as f:
           f.write(resource.content)
    print('download ok %s' %  half_pk)
    return None

def getall_tag_a():
    rep = re.compile('^\w')
    r1 = requests.get(url=url,)
    obj = BeautifulSoup(r1.text,'html.parser')
    tag_a = obj.find_all(name='a',text=rep)
#    return tag_a
    for x in tag_a:
        yield x

for a in getall_tag_a():
    half_pk = a.attrs.get('href')
    full_url = url + half_pk
    download(full_url,half_pk)
    
    
    
