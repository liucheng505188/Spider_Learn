
# 01
# import  urllib.request
# response=urllib.request.urlopen("https://www.baidu.com")
# print(response.read().decode('utf-8'))


# 02

# import urllib.parse
# import urllib.request
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
# print( data)
#
# response=urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())


# 03
import  socket
import urllib.request
import  urllib.error

try:
    response=urllib.request.urlopen('http://httpbin.org/get', timeout=1)

except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME is OUT')
