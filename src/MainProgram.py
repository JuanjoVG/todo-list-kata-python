from Todo import Todo


def print_menu():
    print("Options:")
    print("1 - Add item")
    print("2 - Show items")
    print("3 - Check item")
    print("4 - Uncheck item")
    print("5 - Remove item")
    print("0 - Exit")
    print()


todo = Todo()
print_menu()
opt = int(input())
while opt != 0:
    if opt == 1:
        description = input("Enter a description:\n")
        todo.add(description)
        todo.print()
    elif opt == 2:
        todo.print()
    elif opt == 3:
        todo.check(int(input("What item? ")))
        todo.print()
    elif opt == 4:
        todo.uncheck(int(input("What item? ")))
        todo.print()
    elif opt == 5:
        todo.remove(int(input("What item? ")))
        todo.print()
    else:
        print("Incorrect option")
    print_menu()
    opt = int(input())
