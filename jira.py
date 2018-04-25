import requests
from requests.auth import HTTPBasicAuth
import re

username = 'your email'
token = 'your jira api token'

def getByKey(key):
	url = 'https://agoraio.atlassian.net/rest/api/2/issue/CSD-' + str(key)

	response = requests.get(url, auth=(username,token))
	contents = response.json()

	print 'key:\n' + contents['key']
	print 'summary:\n' + contents['fields']['summary']
	print 'status:\n' + contents['fields']['status']['statusCategory']['name']
	print 'repoter:\n' + contents['fields']['reporter']['emailAddress']
	print 'description:\n' + re.sub('[\r\n]+','\r\n', contents['fields']['description'])
	for i in range(0, contents['fields']['comment']['total']):
		print 'comments:\n' + contents['fields']['comment']['comments'][i]['body']

while True:
	key = input('Type your jira number:')
	if type(key)==int:
		getByKey(key)
	else:
		key = input('Type your jira number:')
