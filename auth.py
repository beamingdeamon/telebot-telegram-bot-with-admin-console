def login (users, email, password):
    for user in users:
        if user[0] == email and user[1] == password:
            return False
        else:
            return True