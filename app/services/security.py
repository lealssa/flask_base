import bcrypt
from urllib.parse import urlparse, urljoin
from flask import request

def create_password_hash(plain_text_password: bytes) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_text_password, salt)

def check_password_hash(plain_text_password: bytes, hashed_password: bytes, ) -> bytes:
    return bcrypt.checkpw(plain_text_password, hashed_password)

# def is_safe_url(target):
#     ref_url = urlparse(request.host_url)
#     test_url = urlparse(urljoin(request.host_url, target))
#     return test_url.scheme in ('http', 'https') and \
#            ref_url.netloc == test_url.netloc    

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc