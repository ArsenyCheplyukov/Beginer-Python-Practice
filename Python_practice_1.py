import sys

fname = sys.argv[1]
inputF = open("INPUT.txt")
data = open.read(inputF)
output = open("OUTPUT.txt", "w")
output.write(data)
inputF.close()
output.close()
