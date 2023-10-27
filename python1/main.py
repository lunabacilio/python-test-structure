import os
from filter import *

JIRA_USR='josea.luna@softtek.com'
JIRA_TOKEN=os.getenv('JIRA_TKN')
url = 'https://devopsdemoj.atlassian.net'
filter='filter=10005'

readInfo(JIRA_USR, JIRA_TOKEN, url, filter)