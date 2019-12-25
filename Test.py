# print just like the other language
print("Hello Python")

# input input sth. from keybord
#name = input()
#print(name)





#list
#------------
classmates = ['Michale', 'Bob', 'Tracy']
print(classmates)
print(classmates.__len__())
print(len(classmates))

#append element
classmates.append('Adam')
print(classmates)

#insert element
classmates.insert(2, 'Jack')
print(classmates)

#delete last element
classmates.pop()
print(classmates) #delete Adam

#delete assign element
classmates.pop(2)
print(classmates) #delete Jack

#replace element
classmates[1] = 'Smith'
print(classmates) #replace Bob to Smith
#------------





#tuple
#------------
#when init it, it can not change
tupleClassmates = ('Abby', 'Amy', 'Zara')
print(tupleClassmates[2])
#------------





#if...else...
#------------
#Don't forget lose ':'
age = 20
if age>=18:
    print('your age is:', age)
    print('audle')
else:
    print('your age is:', age)
    print('teenager')





#circular
#-------------
#for x in...
for name in classmates:
    print(name)


#while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


#break
#just like other language(oc, swift, js and so on)

#continue
#also like break
#-------------




#dict and set
#-------------
#dict
#How to create a dict
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}

#get value through key
print(d)
print(d['Bob'])

#change value through key
d['Bob'] = 100
print(d['Bob'])

#Judge the key is exist?
print('Thomas' in d)

print(d.get('Thoms')) #when ruturn None, python will show nothing except print it，but nothing
print(d.get('Thoms', -1))#use get methon, and set the return value

#delete key-value ---- pop(key)
d.pop('Bob')
print(d)





#set
#It is simlar with dict， but it only store key and is no-repeat
#If you add a repeat element, it will be auto-filter
s = set([1, 2, 3])
print(s)

#add(key)   for add element
s.add(4)
print(s)

#remove(key)  for delete element
s.remove(1)
print(s)