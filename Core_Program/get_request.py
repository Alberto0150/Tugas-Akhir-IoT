import requests

def sending_get_request(IP_ESP,type_send):
    # url = 'https://w3schools.com/python/demopage.php'
    url ="http://"
    url += IP_ESP
    url += "/action?command="
    
    if type_send == 1:
        url += "OFF"
    elif type_send == 0:
        url += "ON"
    
    print(url)
    x = requests.get(url)

    #print the response (the content of the requested file):
    # print(x.text)
    # print(x.status_code)
    # print(type_send)

if __name__ == '__main__':
    sending_get_request(1)