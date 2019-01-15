import requests as req

resp = req.get("https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&jscmd=data&format=json")

print(resp.json())
