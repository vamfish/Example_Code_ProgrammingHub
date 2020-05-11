import urllib.request
import urllib.parse

try:
    # opens bing.com # and passes test as an argument
    x = urllib.request.urlopen('https://www.bing.com/search?q=test')
    print(x.read())
except Exception as e:
    # If the request fails the exception is printed
    print(str(e))

try:
    url = 'https://www.bing.com/search?q=test'
    # The only values passing now is q=test
    values = {'q': 'python'}
    reqdData = urllib.parse.urlencode(values)
    # data should be bytes
    reqData = reqdData.encode('utf-8')
    # Requests the page
    request = urllib.request.Request(url, reqData)
    # Gets the response
    response = urllib.request.urlopen(request)
    # The response data is read in readable forms
    responseData = response.read()
except Exception as e:
    print(str(e))
