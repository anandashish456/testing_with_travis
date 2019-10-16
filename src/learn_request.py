import requests
import json


def get_param():
    inputs = {'name': 'Ashish'}
    r = requests.get('http://httpbin.org/get', params=inputs)
    print(r.text)


def post_data():
    inputs = {'name': 'Ashish'}
    r = requests.post('http://httpbin.org/post', data=json.dumps(inputs), headers={'content-type': 'application/json'})
    print(r.text)


if __name__ == '__main__':
    #get_param()
    post_data()

