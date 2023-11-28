import re

names = '<li>John</li> <li>Paul</li> <li>George</li> <li> Ringo</li>'
namesList = names.split(" ")
for name in namesList:
  result = re.search('<li>(.*)</li>', name)
  print(result.group(1))
