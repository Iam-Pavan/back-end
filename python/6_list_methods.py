list1 = [1,2,7,6,5]
list2 = ['banana','apples','mango','mango']
list1.sort()
print(list1)
list2.append('cherry')
print(list2)
list2.insert(0,'fruits')
print(list2)
list2.remove('cherry')
print(list2)
list1.extend(list2)
print(list1)
print(list2.index('apples'))
print(list2.count('mango'))
list2.reverse()
print(list2)

# list2.clear()
# print(list2)
list3 = list2.copy()
print(list3)
# del list2
# del()