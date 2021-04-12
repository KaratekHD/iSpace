class IservError(BaseException):
    # This is just there for the code to follow the Python best practices
    pass


class LoginError(IservError):
    # This is thrown when the login fails
    pass