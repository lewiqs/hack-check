import requests # cd */python/ --> python pip -m install requests
import json # cd */python/ --> python pip -m install json

def basic(): # Will return basic results.

    email = input('What is your email: ')
    
    he = requests.get('https://hacked-emails.com/api?q=' + email)
    t = json.loads(he.text)
    data = t['status']
    if data == 'found':
        print('[X] Your email was found in the Hacked-Emails API, please see:',he.url,'for more information')
    else:
        print('[!] Nothing Found [!] Running Next Test')

    hibp = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/' + email)
    data = hibp.status_code
    if data == 404:
        print('[!] Nothing Found [!] Running Next Test')
    else:
        print('[X] Your email was found in the HaveIBeenPwned API, please see:',hibp.url,'for more information')

    lpgm = requests.get('https://lastpass.com/gmail/index.php?cmd=check&email=' + email)
    print ('[!] Testing last source (LastPass Gmail)')
    data = json.loads(lpgm.text)
    data = data['hacked']
    data = str(data)

    if data == 'True':
        print('[X] Your email was found in the LastPass Gmail Lookup, please see https://lastpass.com/gmail/index.php or', lpgm.url,'for more information')
    else:
        print('[!] Nothing Found [!] Ending... ')

def full(): # Will return basic results and specific sites your emails been found in.


    email = input('What is your email: ')
    he = requests.get('https://hacked-emails.com/api?q=' + email)
    t = json.loads(he.text)
    data = t['status']
    if data == 'found':
        print('[X] Your email was found in the Hacked-Emails API, please see:',he.url,'for more information.\n')
        number = t['results']
        print ("Returning found in Databases:\n")
        for i in range (number):
            data = t['data'][i]['title']
            print (data + '\n')
    else:
        print('[!] Nothing Found [!] Running Next Test\n')

    site = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/' + email)
    hibp = json.loads(site.text)

    data = site.status_code
    if data == 404:
        print('[!] Nothing Found [!] Running Next Test\n')
    else:
        print('[X] Your email was found in the HaveIBeenPwned API, please see:',site.url,'for more information.\n')
        print ("Returning found in Databases:\n")

        try:
            
            for i in range (3):
                
                data = hibp[i]['Title']
                includes = str(hibp[i]['DataClasses'])
                data = data + ' Includes this data: ' + includes
                print (data + '\n')

        except IndexError:
            pass
        
    lpgm = requests.get('https://lastpass.com/gmail/index.php?cmd=check&email=' + email)
    print ('[!] Testing last source (LastPass Gmail)\n')
    data = json.loads(lpgm.text)
    data = data['hacked']
    data = str(data)

    if data == 'True':
        print('[X] Your email was found in the LastPass Gmail Lookup, please see https://lastpass.com/gmail/index.php or', lpgm.url,'for more information')
    else:
        print('[!] Nothing Found [!] Ending... ')

    


types = input('Would you like to use the Basic [B] or Advanced [A] Version. NOT CASE SENSITIVE: ')
types = types.lower()

if types == "b":
    basic()
elif types == "a":
    full()
else:
    print ("Failed, press enter to quit")
    input()


    
