from sys import argv
from tokenize import Comment


def checkFunc(line):
    if "def" in line and "test" not in line and "main" not in line:
        title = line.split()[1].split("(")[0].replace("_"," ").capitalize()
        return title
    
def checkComment(line):
    if "\"\"\"" in line :
        return True


with open(argv[1:][0], "r") as pythonList:
    lines = pythonList.readlines()

titles = []
for line in lines:
    if checkFunc(line):
        titles.append(checkFunc(line))
        
placeCom = []
num = 0
for line in lines:
    if checkComment(line):
        placeCom.append(num)
    num += 1
 
comentsBrute = []   
comentsTemp = ""
num = 0
while num < len(placeCom):
    i = placeCom[num]
    j = placeCom[num+1]
    while i < j:
        comentsTemp = comentsTemp + lines[i]
        i += 1
    comentsBrute.append(comentsTemp)
    comentsTemp = ""
    num += 2

coments=[]
for comB in comentsBrute:     
    coments.append(comB
                   .replace("\"", "").replace("        ", " ")
                   .replace("    ", " ").replace("  ", "")
                   .replace("\n\n","\par").replace("\n","")
                   .replace("_","\_").replace("$","\$").replace("%","\%"))   

pythonList.close()

    
with open("antes.txt","r") as fantes:
    antes = fantes.read()
with open("depois.txt","r") as fdepois:
    depois = fdepois.read()
with open("full.txt","w") as ffull:
    ffull.write(antes)
    
    i = 0
    while i < len(titles):
        ffull.write("%%--Problema " + str(i + 1) + "--%%\n")
        ffull.write("\problem " + titles[i] + "\\\\" + coments[i] + "\n\n")
        i += 1
    
    ffull.write(depois)
        

    
    
fantes.close()
fdepois.close()
ffull.close()