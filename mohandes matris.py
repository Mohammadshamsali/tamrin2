m =  3
n = 10
code=["0150263864","1234567891","5464569257"]

a=[]
for i in range (m):
    row = [0]*n
    a+=[row]
a[1][2]=1
c=0
for c in range(0,3): 
 b=0 
 for i in code[c]:
   a[c][b]=i
   b+=1

print(a)
print(a[0][1])
print(a[1][8])
