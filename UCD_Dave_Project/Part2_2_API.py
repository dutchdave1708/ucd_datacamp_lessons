# 1. Download via an API

import rebrick
import json

# init rebrick module for general reading
rebrick.init("your_API_KEY_here")

# get set info
response = rebrick.lego.get_set(6608)
print(json.loads(response.read()))

# init rebrick module including user reading
rebrick.init("your_API_KEY_here", "your_USER_TOKEN_here")

# if you don't know the user token you can use your login credentials
rebrick.init("your_API_KEY_here", "your_username_here", "your_password_here")

# get user partlists
response = rebrick.users.get_partlists()
print(json.loads(response.read()))