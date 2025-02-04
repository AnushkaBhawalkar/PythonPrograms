#7. write a menu driven program to calculate the area of different shapes.


while True:
    print("\nMenu:")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Triangle")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        radius = float(input("Enter the radius: "))
        print(f"Area of Circle: {3.14 * radius * radius}")
    elif choice == 2:
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        print(f"Area of Rectangle: {length * breadth}")
    elif choice == 3:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        print(f"Area of Triangle: {0.5 * base * height}")
    elif choice == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

'''output
Menu:
1. Area of Circle
2. Area of Rectangle
3. Area of Triangle
4. Exit
Enter your choice: 3
Enter the base: 70
Enter the height: 90
Area of Triangle: 3150.0

Menu:
1. Area of Circle
2. Area of Rectangle
3. Area of Triangle
4. Exit
Enter your choice: 1
Enter the radius: 55
Area of Circle: 9498.500000000002

Menu:
1. Area of Circle
2. Area of Rectangle
3. Area of Triangle
4. Exit
Enter your choice: 2
Enter the length: 60
Enter the breadth: 47
Area of Rectangle: 2820.0

Menu:
1. Area of Circle
2. Area of Rectangle
3. Area of Triangle
4. Exit
Enter your choice: 4
Exiting program. Goodbye!'''
