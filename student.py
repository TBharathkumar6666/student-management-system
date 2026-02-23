students = []

while True:
    print("\n1.Add Student\n2.View Students\n3.Delete Student\n4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added")

    elif choice == "2":
        print("Students List:")
        for s in students:
            print(s)

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in students:
            students.remove(name)
            print("Deleted")
        else:
            print("Not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
