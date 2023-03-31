
Kis123mas
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-higher_level_programming/0x11-python-network_1/8-json_api.py
@Kis123mas
Kis123mas python networking
 1 contributor
Executable File  26 lines (23 sloc)  607 Bytes
#!/usr/bin/python3
"""
given letter as param, POST to http://0.0.0.0:5000/search_user
usage: ./8-json_api.py [letter only]
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    r = requests.post(url, data=payload)

    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
