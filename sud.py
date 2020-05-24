from z3 import *

vmat = [ [Int('x_%s_%s' % (i,j)) for j in range(9)] for i in range(9) ]

file = open('in.txt','r')

mat = []
for line in file:
    li = [c for c in line]
    mat.append(li)

s = Solver()

for i in range(9):
    for j in range(9):
        if mat[i][j] != '.':
            s.add(vmat[i][j] == mat[i][j])

for i in range(9):
    s.add(Distinct([vmat[i][j] for j in range(9)]))

for j in range(9):
    s.add(Distinct([vmat[i][j] for i in range(9)]))

for i in range(9):
    for j in range(9):
        s.add(And(vmat[i][j] >= 1, vmat[i][j] <= 9))

for k in range(9):
    i = k // 3
    j = k % 3
    s.add(Distinct(vmat[3*i][3*j],vmat[3*i][3*j+1],vmat[3*i][3*j+2],vmat[3*i+1][3*j],vmat[3*i+1][3*j+1],vmat[3*i+1][3*j+2],vmat[3*i+2][3*j],vmat[3*i+2][3*j+1],vmat[3*i+2][3*j+2]))

if s.check() == sat:
    m = s.model()
    for i in range(9):
        for j in range(9):
            print(m.eval(vmat[i][j]),end='')
        print() 
else:
    print('Not Satisfiable...')
