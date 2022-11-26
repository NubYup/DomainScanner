import string
import itertools
import requests as r
letters = string.ascii_lowercase
for I in range(len(letters) + 1):
    for subset in itertools.combinations(letters, I):
        site = f'http://{"".join(subset)}.com'
        try:
        	status = r.get(site)
        	status = "200"
        except r.exceptions.RequestException as e:
        	status = 404
        if status == '200':
        	status = f"\033[92m200"
        else:
        	status = f"\033[91m{status}"
        pos = f'\033[96m\033[1m{site}: {status}'
        print(pos)