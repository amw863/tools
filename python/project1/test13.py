import os,sys

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
def checkVulns(banner, filename):
    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print('[+] Sever is vulnerable:%s' % banner.strip('\n'))
def main():
    if len(sys.argv) == 2:
        filename=sys.argv[1]
    if not os.path.isfile(filename):
        print('[-] %s does not exist' % filename)
        exit(0)
    if not os.access(filename, os.R_OK):
        print('[-] %s access denied' % filename)
        exit(0)
    else :
        print('[-] Usage: %s <vuln filename>' % filename)
        exit(0)

portlist = [21,22,25,80,110,443]
for x in range(147, 150):
    ip = '192.168.95.' + str(x)
    for port in portlist:
        banner = retBanner(ip, port)
        if banner:
            print('[+] %s : %s' % (ip, banner))
if __name__=='__main__':
    main()






import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dicfile = open('dictionary.txt', 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        if cryptPass==cryptWord:
            print("Found passes:", word)
            return
        print("Password not found")
        return
def main():
    passfile = open('password.txt', 'r')
    for line in passfile.readlines():
        user = line.split(':')[0]
        cryptPass = line.split(':')[1].strip('')
        print("Cracking Password for:", user)
        testPass(cryptPasss)

if __main__=='__mian__':
    main()





import zipfile
import threading

def exteactFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('Found password:%', password)
        return password
    except:
        pass
def main():
    zFile=zipflie.ZipFile('unzip.zip')
    passFile=open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = threading.Thread(target, args=(zFile, password))
        t.start()
