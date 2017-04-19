import re,urllib.parse,urllib.request,http.cookiejar,base64,binascii,rsa

cj      = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener  = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

def getData(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    text = response.read().decode('UTF-8')
    return text

def getPost(url, data):
    headers = {
        'User-Agent' :'Mozilla/5.0(compatible;MSIE 9.0;windows NT 6.1;WOW64;Trident/5.0)'
    }
    data  = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url,data, headers)
    response = urllib.request.urlopen(request)
    text = response.read().decode('gbk')
    return text

def login_weibo(nick,pwd):
    prelogin_url = ''
    preLogin = getData(prelogin_url)

    servertime = re.findall('"servertime":(.*?),',preLogin)[0]
    pubkey = re.findall('"pubkey":"(.*?)",',preLogin)[0]
    rsakv = re.findall('"rsakv":"(.*?)",',preLogin)[0]
    nonce = re.findall('"nonce":"(.*?)",',preLogin)[0]

    su = base64.b64encode(bytyes(urllib.request.quote(nick),encoding='utf-8'))
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey,65537)
    message = bytes(str(servertime) + '\t' + str(nonce) + '\n' + str(pwd) , encoding = 'utf-8')
    sp = binascii.b2a_hex(rsa.encrypt(message , key))

    param = {
            'emtry':'weibo',
            'gateway':1,
            'form':'',
            'savesstate':7,
            'userticket':1,
            'pagerefer':'http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D',
            'vsnf':1,
            'su':su,
            'service':miniblog,
            'servertime':servertime,
            'nonce':nonce,
            'pwencode':'rsa2',
            'rsakv':rsakv,
            'sp':sp,
            'sr':'1680*1050',
            'encoding':'UTF-8',
            'prelt':961,
            'url':'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack'
        }
    
    post_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15'
    ret_post_url = postData(post_url,param)

    get_url = re.findall("location.replace\(\'(.*?)\'\);",ret_post_url)[0]
    getData(get_url)

text = getData('http://weibo.com/527891819/home?wvr=5&lf=reg')
fp  = open('ok.txt','w',encoding='utf-8')
fp.write(txt)
fp.close()
login_weibo('nickname', 'password')
