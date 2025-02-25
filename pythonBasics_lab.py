#1. Find Common Elements:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common_elements = set(list1) & set(list2)
print(common_elements)  # Output: {3, 4}


#2. Unique Characters in a String:
string = "programming"
unique_chars = set(string)
print(unique_chars)  # Output: {'g', 'i', 'p', 'o', 'r', 'm', 'a', 'n'}


#3. Union of Sets:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}


#4. Intersection of Sets:
A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}

intersection_set = A & B
print(intersection_set)  # Output: {'b', 'c'}


#5. Difference of Sets:
X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}

difference_set = X - Y
print(difference_set)  # Output: {1, 2}
