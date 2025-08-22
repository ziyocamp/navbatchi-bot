import json


def add_user(telegram_id, first_name, last_name, username):
    with open('data.json') as jsonfile:
        try:
            data = json.load(jsonfile)
        except:
            data = {"users": {}, "duties": {}}

    data['users'][str(telegram_id)] = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username
    }

    with open('data.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
