l1 = [2,10,"python"]
print(l1)

l1 = l1[0:2]
print(l1)

l2 = [4,3,54,23,12,0,9,8,78,7]

l2.sort()
print(l2)

l2.reverse()
print(l2)

l2.append(8)
print(l2)

l2.insert(3,8)
print(l2)

l2.pop(3)
print(l2)

l2.remove(23)
print(l2)

a = ()
b = (1,)
c = (1,2,30)
print(a)
print(b)
print(c)
print("Count of 1 in tuple c: ", c.count(1))
print("Index of value 1 in tuple c: ", c.index(1))

fruits = []
for i in range(1,7):
    fruitName = input("Enter your fruit")
    fruits.append(fruitName)

print(fruits)

marks = []
for i in range(1,6):
    marksEntered = int(input("Enter your marks"))
    marks.append(marksEntered)

marks.sort()
print(marks)

sum = 0
for i in marks:
    sum += i
print("Addition of all the marks are: ",sum)

d = (7,0,8,0,0,9)
print("Count of zero in tuple d are: ", d.count(0))
