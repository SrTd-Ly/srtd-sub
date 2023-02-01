#/usr/bin/python
#/Codede by SrTd_Ly
#

from termcolor import colored
import requests
import sys

print("""
        ███████████████████████████████████████████████████
        █─▄▄▄▄█▄─▄▄▀█─▄─▄─█▄─▄▄▀█▀▀▀▀▀██─▄▄▄▄█▄─██─▄█▄─▄─▀█
        █▄▄▄▄─██─▄─▄███─████─██─████████▄▄▄▄─██─██─███─▄─▀█
        ▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀
                      
                     ▄▄ Codede by SrTd_Ly 
                     ▄▄ facebook.com/SrTd.Ly1
                     ▄▄ insta:@srtd_ly 
                        """)
print()
print ('Ex: site.com')
host = str(input("~$ Enter the Domain ~ : "))

f = open("list.txt","r")
r = f.read()
subdomains = r.splitlines()

for sub in subdomains:

    domain = "http://"+ sub + "." + host
    
    try:
        req = requests.get(domain,"html.parser")

        
        if req.status_code == 200:
            print(colored('[+] Discovered Subdomain -->', 'red'), colored(domain, 'green'))
          
            

    except requests.ConnectionError:
        pass
    except KeyboardInterrupt:
        print("\n EXIT..! ")
        sys.exit()
