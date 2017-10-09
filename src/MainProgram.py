from Todo import Todo


def print_menu():
    print("Options:")
    print("1 - Add item")
    print("2 - Show items")
    print("3 - Check item")
    print("0 - Exit")
    print()


todo = Todo()
print_menu()
opt = int(input())
while opt != 0:
    if opt == 1:
        todo.add(input("Enter a description:\n"))
    elif opt == 2:
        todo.print()
    elif opt == 3:
        index = int(input("What item? "))
        todo.check(index)
    else:
        print("Incorrect option")
    print_menu()
    opt = int(input())
