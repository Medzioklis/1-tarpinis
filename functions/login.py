def check_login_user(username, password):
    bibl_login = {
        "admin": "pass",
    }
    return bibl_login.get(username) == password

