import requests
import os
os.system("") 

def sending_get_request(IP_ESP,type_send):
    url ="http://"
    url += IP_ESP
    url += "/action?command="
    
    if type_send == 1:
        url += "OFF"
    elif type_send == 0:
        url += "ON"
    
    
    print('\033[32m' + url + '\033[0m')
    requests.get(url)

if __name__ == '__main__':
    sending_get_request('sample.com', 1)