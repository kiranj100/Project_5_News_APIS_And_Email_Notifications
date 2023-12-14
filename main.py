import requests

# Import send_mail.py file and under that python file we \
    # Import send_mail_user function
from send_mail import send_mail_user
api = "e206eb1ef45147b5bdbe78ce94b2be5b"
url = "https://newsapi.org/v2/everything?q=apple&from=2023-12-13&to=2023-12-13"\
      "&sortBy=popularity&apiKey=e206eb1ef45147b5bdbe78ce94b2be5b"

# Make the request
link_request = requests.get(url)

# Get the dictionary with data
content = link_request.json()

# Access articles, title and descriptions

body = " "
for articlas in content["articles"]:
    if articlas["title"] is not None:
     body = body + articlas["title"] + "\n " + articlas["description"] + 2*"\n"

body = body.encode("utf-8")
send_mail_user(message=body)


