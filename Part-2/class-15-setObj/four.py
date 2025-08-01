s1={10,20,30,40}
s2={30,40,50,60}
#union
print(s1.union(s2))
print(s1 | s2)
#intesection
print(s1.intersection(s2))
print(s1 & s2)
#difference
print(s1-s2)
print(s1.difference(s2))

#symmetric_difference  - exclusing s1 and exclusing s2
print(s1^s2)
print(s1.symmetric_difference(s2))
