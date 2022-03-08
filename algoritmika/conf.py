config = [
    # method, endpoint
    ("GET", '/notes/*'),
    ("GET", '/notes'),
]

jwt_skip_rules = [
    # method, endpoint
    ("POST", '/login/'),
    ("PUT", '/login/'),
]

JWT_PARAMETERS = {
    "lifetime": {'seconds': 30},
    "key_refresh_token": "refresh_token",
    "key_access_token": "access_token",
    "algorithms": ["HS256"],
}