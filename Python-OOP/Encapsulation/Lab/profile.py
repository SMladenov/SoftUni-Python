import re

class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username (self):
        return self.__username
    
    @username.setter
    def username (self, username):
        if 5 <= len(username) <= 15:
            self.__username = username
        else:
            raise ValueError ("The username must be between 5 and 15 characters.")
    

    @property
    def password (self):
        return self.__password
    
    @password.setter
    def password (self, password):
        pattern = r"^(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{8,}$"
        reMatch = re.match(pattern, password)

        if reMatch is None:
            raise ValueError ("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        else:
            self.__password = reMatch.group()


    def __str__ (self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
    
# profile_with_invalid_password = Profile('My_username', 'My-password')
    
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
    
# correct_profile = Profile("Username", "Passw0rd")

# print(correct_profile)


