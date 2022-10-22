from requests import get, status_codes
from sys import argv

command = argv
command.remove("main.py")
message = " ".join(command[1:])

if command[0] == "movie":
    movie = message
    response = get(f"http://www.omdbapi.com/?t={movie}&apikey=a2b01adf")
    print(response.status_code)
    response_json = response.json()
    print("---------------------------------------------")
    print("Title:", response_json["Title"])
    print("Year:", response_json["Year"])
    print("Released:", response_json["Released"])
    print("Genre:", response_json["Genre"])
    print("Director:", response_json["Director"])
    print("---------------------------------------------")