#1st Program
my_list = [10,20,30,40,50]
print("First element: ",my_list[0])
print("Last element: ",my_list[-1])
print("Third element: ",my_list[2])
#output:
First element:  10
Last element:  50
Third element:  30


#2nd Program
fruits=['Apple','Banana','Strawberry','Kiwi','Cherry']
print("The second element: ",fruits[1])
print("The fourth element: ",fruits[3])

fruits[2]="Grape"
print("Updated list: ", fruits)
#output:
The second element:  Banana
The fourth element:  Kiwi
Updated list:  ['Apple', 'Banana', 'Grape', 'Kiwi', 'Cherry']


#3rd Program
list=[1,2,3,4,5,6,7,8,9]
print('First 5 elements: ',list[:5])
print('Alternate elements: ',list[1::2])
print('Reversed list: ',list[::-1])
#output:
First 5 elements:  [1, 2, 3, 4, 5]
Alternate elements:  [2, 4, 6, 8]
Reversed list:  [9, 8, 7, 6, 5, 4, 3, 2, 1]


#4th Program
alphabet=['A','B','C','D','E','F','G','H','I','J']
print(alphabet)
print("First 5 letters: ",alphabet[0:5])
print("Last 5 letters: ",alphabet[-5:])
print("Every second letter: ",alphabet[::2])
#ouput:
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
First 5 letters:  ['A', 'B', 'C', 'D', 'E']
Last 5 letters:  ['F', 'G', 'H', 'I', 'J']
Every second letter:  ['A', 'C', 'E', 'G', 'I']


#5th Program
colors=['Red', 'Blue', 'Green']
print(colors)
colors.insert(1,"Yellow")
colors.append("Purple")
print("Updated List: ",colors)
#output:
['Red', 'Blue', 'Green']
Updated List:  ['Red', 'Yellow', 'Blue', 'Green', 'Purple']


#6th Program
n=[]
for i in range(1,6):
    n.insert(0,i)
print("List: ",n)
n.insert(2, "Middle")
print("Updated List: ",n)
#output:
List:  [5, 4, 3, 2, 1]
Updated List:  [5, 4, 'Middle', 3, 2, 1]


#7th Program
num=[10,20,30,40,50,60]
print(num)
del num[2]
print(num)
del num[-1]
print(num)
num.clear()
print("The updated list: ", num)
#output:
[10, 20, 30, 40, 50, 60]
[10, 20, 40, 50, 60]
[10, 20, 40, 50]
The updated list:  []


#8th Program
user_list = [int(input("Enter an element: ")) for _ in range(5)]
# Delete the first and last elements
del user_list[0]
del user_list[-1]
# Remove the element at index 3 using pop()
if len(user_list) > 3:
    user_list.pop(3)
print("Updated list:", user_list)
#output:
Enter an element: 1
Enter an element: 2
Enter an element: 3
Enter an element: 4
Enter an element: 5
Updated list: [2, 3, 4]
             

#9th Program
x = [1,2,3,4,5,6,7,8,9,10]
sublist = x[2:7]
x.insert(5, 99)
print("Sublist:", sublist)
print("Updated list:", x)
#output:
Sublist: [3, 4, 5, 6, 7]
Updated list: [1, 2, 3, 4, 5, 99, 6, 7, 8, 9, 10]


#10th Program
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sublist = my_list[1:4]
my_list[3] = 'x'
my_list.remove('g')
my_list.append('z')
print("Sublist:", sublist)
print("Updated list:", my_list)
#output:
Sublist: ['b', 'c', 'd']
Updated list: ['a', 'b', 'c', 'x', 'e', 'f', 'z']
