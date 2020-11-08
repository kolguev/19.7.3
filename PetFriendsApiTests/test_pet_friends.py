from api import PetFriends
from settings import *

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key['key'], filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_post_pet_simple(name=name, age=age, animal_type=animal_type):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_pet_simple(auth_key['key'], name, age, animal_type)
    assert status == 200
    assert result['name'] == name