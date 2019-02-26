
# we can store test data in this module like users

users = [
    {"username": "testusername1", "email": "test1@test.com", "birthday": "2001-09-03", "address": "Turkey İstanbul Bakırköy 344252"},
	{"username": "testusername2", "email": "test2@test.com", "birthday": "2000-09-03", "address": "Studio 103 Wellfield Road Roath Cardiff"},
]

def get_user(name):
    try:
        return (user for user in users if user["username"] == name).__next__()
    except Exception as e:
        print(e)
