import re

def Main():
  line = "I think I understand regular expressions"
  print (line)

  matchResult = re.match('think', line, re.M|re.I)
  if matchResult:
    print("Match Found: "+matchResult.group())
  else:
    print("Match Not Found")

  searchResult = re.search('think', line, re.M|re.I)
  if searchResult:
    print("Search Found: "+searchResult.group())
  else:
    print("Search Not Found")

if __name__ == "__main__":
    Main()
