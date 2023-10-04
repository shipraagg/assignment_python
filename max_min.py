#3rd max element
def thirdMax(list):
    list.sort(reverse = True)
    count = 1
    previous = list[0]

    for i in range(len(list)):
        if list[i] != previous:
            count = count + 1
            previous = list[i]
        if count == 3:
            return list[i]
    return list[0] 

list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list.append(ele) 
 print(list)
 result=thirdMax(list)
 print("third max element:",result)

 #3rd min element

 def thirdMin(list):
    list.sort(reverse = False)
    count = 1
    previous = list[0]

    for i in range(len(list)):
        if list[i] != previous:
            count = count + 1
            previous = list[i]
        if count == 3:
            return list[i]
    return list[0] 

list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list.append(ele) 
 print(list)
 result=thirdMin(list)
 print("third min element:",result)

