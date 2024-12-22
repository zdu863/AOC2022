from z3 import Int, Optimize, sat

with open('input.txt') as f:
    data = f.read().splitlines()

file1 = open('myfile.txt', 'w')
L = []

for line in data:
    l=line.replace(':','=')
    L.append(l+' ,\n')
file1.writelines(L)
  
# Closing file
file1.close()
  
# Checking if the data is
# written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()
