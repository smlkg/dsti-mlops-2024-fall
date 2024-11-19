import re

def validate_username(username: str) -> bool:
    """Validate username is not empty and has no spaces."""
    return bool(username) and ' ' not in username

def validate_password(password: str) -> bool:
    """Validate password meets complexity requirements."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_+=<>?/\\|{}[]:;" for char in password):
        return False
    return True

def validate_email(email: str) -> bool:
    """Validate email contains a proper format."""
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))