
import requests
import json
from config import config as cfg

filename = "repos-private.json"


url = 'https://api.github.com/repos/Tanjasta/aprivateone'
apikey = cfg["githubkey"]


apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)

