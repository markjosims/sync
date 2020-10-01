import requests

def main():
    print( get_zomato_response('https://developers.zomato.com/api/v2.1/categories') )

def get_zomato_response(url):
    headers = {"Accept": "application/json", "user-key": '8e884c077f71f6ba3ca447301a8b3019'}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == '__main__':
    main()