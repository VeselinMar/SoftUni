class Profile:

    def __init__(self, username, password):

        if not self._is_valid_username(username):
            raise ValueError("The username must be between 5 and 15 characters.")

        if not self._is_valid_password(password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self._username = username
        self._password = password

    def get_username(self):
        return self._username

    def set_username(self, new_username):
        if not self._is_valid_username(new_username):
            raise ValueError("The username must be between 5 and 15 characters.")
        self._username = new_username

    def get_password(self):
        return self._password

    def set_password(self, new_password):
        if not self._is_valid_password(new_password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self._password = new_password

    def _is_valid_username(self, username):
        return 5 <= len(username) <= 15

    def _is_valid_password(self, password):
        if len(password) < 8:
            return False

        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)

        return has_digit and has_upper

    def __str__(self):
        return f'You have a profile with username: "{self._username}" and password: {"*" * len(self._password) }'

