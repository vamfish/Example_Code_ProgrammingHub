import urllib.parse
import urllib.request

url = 'https://www.bing.com'
values = {'d':'python'}

reqData = urllib.parse.urlencode(values)
reqbData = reqData.encode('utf-8') # data should be bytes
request = urllib.request.Request(url, reqbData)
response = urllib.request.urlopen(request)
respData = response.read()
print(respData)
