import requests
from settings import valid_email, valid_password

class PetFriends:
    def __init__(self):
        self.base_url="http://petfriends1.herokuapp.com/"
    def get_api_key(self, email, password):
        headers={
            'email': valid_email,
            'password': valid_password
        }
        res=requests.get(self.base_url+'api/key', headers=headers)
        status=res.status_code
        result=""
        try:
            result=res.json()
        except:
            result=res.text
        return status, result
    def get_list_of_pets(self, auth_key, filter):
        headers={'auth_key': auth_key}
        filter={'filter': filter}
        res=requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status=res.status_code
        result=""
        try:
            result=res.json()
        except:
            result=res.text
        return status, result