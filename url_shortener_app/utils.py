from random import choice, random
from string import ascii_letters, digits

BASE_URL = "http://localhost:8000/"

def create_random_sequence_string(chars=ascii_letters+digits):
    return "".join([choice(chars) for x in range(10)])


def generate_sequence_for_short_url(instance):
    random_sequence = create_random_sequence_string()
    model = instance.__class__
    
    # if short url hash has already been used, run again to create a new one to use
    if model.objects.filter(short_url=f"{BASE_URL}{random_sequence}").exists():
        return generate_sequence_for_short_url(instance)
    
    return random_sequence