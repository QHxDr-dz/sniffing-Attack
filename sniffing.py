from scapy.all import *
def main(hdr):
    if hdr.haslayer(TCP):
        print("tcp pocket...")
        src=hdr[IP].src
        dest=hdr[IP].dst
        dst=hdr.src
        sr=hdr.dst
        src_port=hdr.sport
        dest_port=hdr.dport
        print("SRC IP : "+src)
        print("DST IP : "+dest)
        print("SRC MSC : "+sr)
        print("DST MAC : "+dst)
        print("SRC PORT: "+str(src_port))
        print("DST PORT: "+str(dest_port))
        if hdr.haslayer(Raw):
            print(len(hdr[Raw].load))





data='POST /search.php?test=query HTTP/1.1\r\nHost: testphp.vulnweb.com\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 27\r\nOrigin: http://testphp.vulnweb.com\r\nConnection: keep-alive\r\nReferer: http://testphp.vulnweb.com/search.php?test=query\r\nUpgrade-Insecure-Requests: 1\r\nPriority: u=0, i\r\n\r\nsearchFor=hhhhh&goButton=go'
sniff(iface="wlp3s0" ,prn=main)
import pprint
