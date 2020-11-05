def nonRepeating(s,k):
  myDict={}
  count=1
  for letter in s:
    if letter not in myDict:
      myDict[letter]=1
    else:
      myDict[letter]+=1
  print(myDict)
  for letters in myDict:
    if myDict[letters]==1:
      if count==k:
        return letters
      else:
        count+=1
  return "Exceeded"
print(nonRepeating("geeksforgeeks",2))
