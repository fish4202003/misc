# -*- coding:utf-8 -*-  
import re
import urllib2

#从百度网页获取双色球的当日开奖信息
def get_ssq() :
    req = urllib2.Request(url='http://baidu.lecai.com/lottery/draw/')
    f = urllib2.urlopen(req)
    page = f.read()
    f.close()

    pattern = re.compile(r'<div\s+class=\"ballbg\"\s*>.*?lottery_type=ssq#prize.*?<\/div>', re.M | re.I )
    m = pattern.findall(page)
    
    if len(m) != 1 :
        print "网站已经改版"
        return None

    pattern = re.compile( r'<span class="ball_1">(\d*)</span>' )
    result = pattern.findall(m[0])
    # 双色球是6个普通数+ 1个特别数
    if len(result) != 6 :
        print "网站已经改版"
        return None

    # 获取特码
    pattern = re.compile( r'<span class="ball_2">(\d*)</span>' )
    te_ma = pattern.findall(m[0])
    if len(te_ma) != 1 :
        print "网站已经改版"
        return None
    result.append( te_ma[0] )
    return result

ssq = get_ssq()
print ssq
