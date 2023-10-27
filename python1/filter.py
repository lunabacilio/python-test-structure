import requests
from requests.auth import HTTPBasicAuth
import json

def readInfo(usr, tkn, url, jira_filter):

    total = 1
    startAt = 0
    while startAt <= total:

        jira_url = url + "rest/api/3/search?jql=" + jira_filter + '&startAt=' + str(startAt)

        auth = HTTPBasicAuth(usr, tkn)

        headers = {
        "Accept": "application/json"
        }

        response = requests.request(
            "GET",
            jira_url,
            headers=headers,
            #params=query,
            auth=auth
        )

        #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
        filter_response = json.loads(response.text)
        for issue in filter_response['issues']:
            issuekey = issue['key']
            print(issuekey)
        
        startAt += 50
        total = filter_response['total']

    print('task finished')