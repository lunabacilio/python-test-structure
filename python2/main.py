import os
from filter2 import *

JIRA_USR='josea.luna@softtek.com'
JIRA_TOKEN=os.getenv('JIRA_TKN')
url = 'https://devopsdemoj.atlassian.net'
filter='filter=10005'

readInfo2(JIRA_USR, JIRA_TOKEN, url, filter)