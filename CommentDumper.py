# -*- coding: utf-8 -*-
# For Windows OS Only....

import sys
import os
import json
import time
from urllib.request import *

out=open("listV.csv","w",1,"UTF-16")
count=1
out.write("序号\t用户名\t楼层\t时间\t评论\n")
for page in range(1,10000):
    url="https://api.bilibili.com/x/v2/reply?type=1&oid=47457833&pn="+str(page)
    res=urlopen(url)
    '''
    try:
        res=urlopen(url)
    except:
        print(page)
        break
    '''
    html=res.read().decode('utf-8')
    j=json.loads(html)

    for i in range(20):
        comment = j['data']['replies'][i]
        '''
        try:
            comment = j['data']['replies'][i]
        except:
            print(i)
            break
        '''
        floor = comment['floor']
        username = comment['member']['uname']
        sex = comment['member']['sex']
        ctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(comment['ctime']))
        content = comment['content']['message']
        likes = comment['like']
        rcounts = comment['rcount']
        '''
        print('--'+str(floor) + ':' + username + '('+sex+')' + ':'+ctime)
        print(content)
        print('like : '+ str(likes) + '      ' + 'replies : ' + str(rcounts))
        '''
        
        #out.write(str(count)+"\t"+username+"\t"+str(floor)+"\t"+ctime+"\t"+content.replace("\n","[r]").replace("\t","")+"\n")
        out.write(str(count)+"\t"+username+"\t"+str(floor)+"\t"+ctime+"\n")
        count+=1
        
        if floor==1:
            break
        
    if page%100==0:
        print(str(page)+" page")
        time.sleep(60)
