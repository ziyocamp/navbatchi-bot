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


def add_duty(telegram_id, day):
    with open('data.json') as jsonfile:
        try:
            data = json.load(jsonfile)
        except:
            data = {"users": {}, "duties": {}}

    data['duties'][day] = str(telegram_id)

    with open('data.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def get_dities_dict():
    with open('data.json') as jsonfile:
        try:
            data = json.load(jsonfile)
        except:
            data = {"users": {}, "duties": {}}

    return data['duties']


def get_user(tg_id):
    with open('data.json') as jsonfile:
        try:
            data = json.load(jsonfile)
        except:
            data = {"users": {}, "duties": {}}

    return data['users'].get(str(tg_id))

