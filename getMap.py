#高德地图离线瓦片下载(电子地图)
#作者：wangjd

from urllib.request import urlretrieve
import os

#url="http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x=215762&y=99298&z=18"

LeftTop=[215760,99295]
RightBottom=[215762,99298]
z=18
#url = 'http://www.sina.com.cn'
for x in range(LeftTop[0], RightBottom[0]):
    for y in range(LeftTop[1], RightBottom[1]):
        url="http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x="+str(x)+"&y="+str(y)+"&z=18"
        #local='d:\\18\\'+str(x)+"\\"+str(y)+".png"
        local = 'd:\\'+str(z)+'\\' + str(x) + "\\" + str(y) + ".png"
        path='d:\\'+str(z)+'\\'+str(x)
        if not os.path.exists(path):
            os.makedirs(path)
        urlretrieve(url,local)
