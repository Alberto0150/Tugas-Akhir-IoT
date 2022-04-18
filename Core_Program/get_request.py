import requests

def sending_get_request(IP_ESP,type_send):
    url ="http://"
    url += IP_ESP
    url += "/action?command="
    
    if type_send == 1:
        url += "OFF"
    elif type_send == 0:
        url += "ON"
    
    print(url)
    requests.get(url)

if __name__ == '__main__':
    sending_get_request(1)