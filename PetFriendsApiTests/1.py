from api import PetFriends
from settings import *

pf = PetFriends()
result = pf.get_api_key(valid_email, valid_password)
print(result[1]["key"])