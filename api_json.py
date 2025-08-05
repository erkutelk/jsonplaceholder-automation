import requests

class ApiResponse():
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    def __init__(self, url):
        self.url = url
        self.full_url = self.BASE_URL + self.url 
        self.response = requests.get(self.full_url)

    def get_status(self):
        return self.response.status_code

    def get_json(self):
        return self.response.json()

    def post(self, data):
        response = requests.post(self.full_url, json=data)
        return response
    
    def put(self,data):
        respone=requests.put(self.full_url,json=data)
        return respone
