import requests

class ApiResponse():
    BASE_URL='https://jsonplaceholder.typicode.com/'
    def __init__(self,url):
        self.url=url
        self.response=requests.get(self.BASE_URL+self.url)

    def get_status(self):
        return self.response.status_code
    
    def get_json(self):
        print(self.response.json())
        return self.response.json()

    





    