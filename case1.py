# Gestor de lista de tareas

a = []
b = []


def x(y):
    if y not in a:
        a.append(y)
        print("Task added:", y)
    else:
        print("Task already exists!")


def z(y):
    if y in a:
        a.remove(y)
        print("Task removed:", y)
    else:
        print("Task not found!")


def w(y):
    if y in a:
        a.remove(y)
        b.append(y)
        print("Task completed:", y)
    else:
        print("Task not found!")


def p():
    if len(a) == 0:
        print("No tasks to show!")
    else:
        print("Tasks to do:")
        for t in a:
            print("-", t)


def q():
    if len(b) == 0:
        print("No completed tasks to show!")
    else:
        print("Completed tasks:")
        for t in b:
            print("-", t)


def main():
    while True:
        print("\nTodo List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Show Completed Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            taskName = input("Enter task name: ")
            x(taskName)
        elif choice == "2":
            taskName = input("Enter task name to remove: ")
            z(taskName)
        elif choice == "3":
            taskName = input("Enter task name to complete: ")
            w(taskName)
        elif choice == "4":
            p()
        elif choice == "5":
            q()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")


if __name__ == "__main__":
    main()
