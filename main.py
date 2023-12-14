import requests

api = "e206eb1ef45147b5bdbe78ce94b2be5b"
url = "https://newsapi.org/v2/everything" \
    "?q=tesla&from=2023-11-14&sortBy=publishedAt&"\
    "apiKey=e206eb1ef45147b5bdbe78ce94b2be5b"

# Make the request
link_request = requests.get(url)

# Get the dictionary with data
content = link_request.json()

# Access articles, title and descriptions
for articlas in content["articles"]:
    print(articlas["title"])
    print(articlas["description"])


