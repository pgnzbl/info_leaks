#!/usr/bin/env python3

import threading
import requests
import time
import os
# import fcntl

os.chdir(os.path.dirname(os.path.realpath(__file__)))
requests.adapters.DEFAULT_RETRIES = 2

def exploit(dic):
    with open(r'd.txt', "r") as f:
        for domain in f:
            domain = domain.strip()
            url = 'http://'+domain+'/'+dic
            url = url.strip()
            try:
                header = {
                    'User-Agent':'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
                }
                r = requests.get(url = url, headers = header, timeout = 3,allow_redirects=False)
            except Exception as e:
                print(e.args)
            else:
                with open(r'results.txt', "a+") as w:
                    if dic in ("phpinfo.php", "info.php", "test.php", "1.php"):
                        if r.status_code == 200:
                            resText = r.text
                            if 'disable_functions' in resText:
                                print(url)
                                w.write(url + "\n")
                    elif dic == 'druid/index.html':
                        if r.status_code == 200:
                            resText = r.text
                            if 'druid.index' in resText:
                                print(url)
                                w.write(url + "\n")


def main():
    if os.path.exists('results.txt'):
        os.remove('results.txt')
    print("please waiting!!!!")
    dics = ("info.php","phpinfo.php","test.php","1.php","druid/index.html")
    for dic in dics:
        dic = dic.strip()
        t = threading.Thread(target=exploit, args=(dic,))
        t.start()
        time.sleep(0.2)

if __name__ == '__main__':
    main()