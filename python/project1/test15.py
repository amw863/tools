#-------------coding=utf-8------------------------
import optparse,socket

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print('[+]%d/tcp open!' % tgtPort)
        connSkt.close()
    except:
         print('[-]%/tcp closd' % tgtPort)
def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print('[-] cannot resolve %s: unknown host' % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIp)
        print('\n[+]Scan Result for:'+ tgtName[0])
    except:
        print('\n[+]Scan Result for:' + tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('scanning port:' + str(tgtPort))
        connScan(tgtHost, int(tgtPort))
portScan('www.baidu.com', [80,23,443,23,445])
