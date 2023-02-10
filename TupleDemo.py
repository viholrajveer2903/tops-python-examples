t=(1,2,1.1,"tops",[10,20,30],True,1,10)

print(t)
print(t.count(1))
print(t.index(2))

for i in t:
    print(i)

print(1 in t)
print(len(t))
print(t[4])
t[4].append(40)
print(t[4])
