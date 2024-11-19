import sys
import os
import pytest

# Add the src directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from register import validate_username, validate_password, validate_email

# Test cases for username validation
@pytest.mark.parametrize("username,expected", [
    ("user123", True),
    ("", False),
    ("user name", False),
    ("user_name", True)
])
def test_validate_username(username, expected):
    assert validate_username(username) == expected

# Test cases for password validation
@pytest.mark.parametrize("password,expected", [
    ("Pass123!", True),
    ("1234567", False),  # Too short
    ("password", False),  # No number
    ("12345678", False),  # No letter
    ("Passwrd1", False),  # No special character
    ("P@ss1234", True)
])
def test_validate_password(password, expected):
    assert validate_password(password) == expected

# Test cases for email validation
@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),
    ("userexample.com", False),  # Missing @
    ("user@com", False),  # Missing .
    ("user@example.co.uk", True),
    ("@example.com", False),  # Missing local part
])
def test_validate_email(email, expected):
    assert validate_email(email) == expected
