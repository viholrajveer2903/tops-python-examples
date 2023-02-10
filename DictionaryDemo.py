d={1:"Rajveer",2:"Bhavesh",3:"Jay",4:"Vipul",5:"Bhavdeep",6:"Manav"}

print(d[3])
d1=d.copy()
print(d1)
d1[7]="Rignesh"
print(d1)
print(d)
d2=d
d2[8]="Arti"
print(d2)
print(d)
print(d.get(4))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(3))
print(d)
print(d.popitem())
d3={10:"Arti",11:"Jay",12:"Rashik"}
d.update(d3)
print(d)

for i in d:
    print(i," : ",d[i])
