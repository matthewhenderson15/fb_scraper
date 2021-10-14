import requests
import re
import json
import selenium

if __name__ == "__main__":
    # Set base url and create session object that will make the request
    url = 'https://www.facebook.com'
    new_session = requests.session()
     
# Convert credentials as json to object 
def create_obj_from_json(json_file):
    new_obj = None

    # Open file and set as new object
    with open(json_file) as f:
        new_obj = json.loads(f.read())
    return new_obj

