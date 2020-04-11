#!usr/bin/python

import json

print ("this is new de")
print ("11111111111111111")
print ("22222222222222222")

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

print (type(data))

json1 = json.dumps(data)
print (type(json1))

print (json1)



jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
print (type(jsonData))

text = json.loads(jsonData)

print (type(text))


print (text)
