from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.
    """
    hashed = hash_password(password_to_check)
    return stored_logins.get(email) == hashed


def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    """
    return sha256(password.encode()).hexdigest()


def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # 123!456?789
    }

    # Try logins with various credentials
    print("Login attempt 1:", login("example@gmail.com", stored_logins, "word"))
    print("Login attempt 2:", login("example@gmail.com", stored_logins, "password"))

    print("Login attempt 3:", login("code_in_placer@cip.org", stored_logins, "Karel"))
    print("Login attempt 4:", login("code_in_placer@cip.org", stored_logins, "karel"))

    print("Login attempt 5:", login("student@stanford.edu", stored_logins, "password"))
    print("Login attempt 6:", login("student@stanford.edu", stored_logins, "123!456?789"))


if __name__ == '__main__':
    main()
