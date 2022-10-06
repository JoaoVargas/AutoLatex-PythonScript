from sys import argv

#Ler uma linha e se for uma func retorna o nome da func formatado
def checkFunc(line):
    if "def" in line and "test" not in line and "main" not in line:
        title = line.split()[1].split("(")[0].replace("_"," ").capitalize()
        return title

#Ler uma linha e se for um coment retorna True
def checkComment(line):
    if "\"\"\"" in line :
        return True

#Abre a file dada ao chamar o script, tlvz verificação???
with open(argv[1:][0], "r") as pythonList:
    lines = pythonList.readlines()

#Cria lista de titulos percorrendo linhas 
titles = []
for line in lines:
    if checkFunc(line):
        titles.append(checkFunc(line))

#Cria lista da posição onde tem coments
placeCom = []
num = 0
for line in lines:
    if checkComment(line):
        placeCom.append(num)
    num += 1


#Cria lista de coments usando lista de posiçoes
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


#Formata a lista bruta de coments em outra lista
coments=[]
for comB in comentsBrute:     
    coments.append(comB
                   .replace("\"", "").replace("        ", " ")
                   .replace("    ", " ").replace("  ", "")
                   .replace("\n\n","\par").replace("\n","")
                   .replace("_","\_").replace("$","\$").replace("%","\%"))   

pythonList.close()

#abre o pre e o pos para leitura e o full para escrita
with open("pre.txt","r") as fpre:
    pre = fpre.read()
with open("pos.txt","r") as fpos:
    pos = fpos.read()
with open("full.txt","w") as ffull:
    ffull.write(pre)

    #escreve no full formatado para latex
    i = 0
    while i < len(titles):
        ffull.write("%%--Problema " + str(i + 1) + "--%%\n")
        ffull.write("\problem " + titles[i] + "\\\\" + coments[i] + "\n\n")
        i += 1

    ffull.write(pos)
        

    
#Fechatudo,se pa n precisa
fpre.close()
fpos.close()
ffull.close()