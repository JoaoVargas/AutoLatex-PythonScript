from sys import argv
from tokenize import Comment


def checkFunc(line):
    if "def" in line:
        return True
def checkComment(line):
    if "\"\"\"" in line:
        return True
    
num = 0
titles = []
coments = []
placeCom = []

with open(argv[1:][0], "r") as f:
    lines = f.readlines()


for line in lines:
    if checkFunc(line):
        title = line.split()[1].split("(")[0].replace("_"," ").capitalize()
        titles.append(title)
    if checkComment(line):
        placeCom.append(num)
    num+= 1
num = 0

while num < len(placeCom):
  while placeCom[num] < placeCom[num+1]:
        coments.append(lines[placeCom[num]])
        placeCom[num] += 1
  num += 2
    
list(map(lambda x:x.strip(),coments))
        
print(titles)
print(coments)
    