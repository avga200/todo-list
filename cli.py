import functions
import time


now = time.strftime('It is %B, %Y, %H:%M:%S')
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit\n")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todo = todo.strip()
        if todo == '':
            print("There is nothing to add")
            continue

        with open("todos.txt", 'a') as file:
            file.write(todo + '\n')
        print("Task", '"' + todo + '"', "successfully added")

    elif user_action.startswith("show"):
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos, 1):
            print(f"{index}>{item}", end="")

    elif user_action.startswith("edit"):
        with open("todos.txt", 'r') as file:
            try:
                todos = file.readlines()
                number = int(user_action[5:])
                number -= 1
                new_todo = input("Enter the new todo:\n")
                todos[number] = new_todo
            except ValueError:
                print('Invalid Command')
            except IndexError:
                print("The index is out of range")
        functions.push_todos(todos)
    elif user_action.startswith("complete"):
        try:
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
                number = int(user_action[9:])
                number -= 1
                todos.pop(number)
        except ValueError:
            print("Invalid Command")
            continue
        except IndexError:
            print("The index is out of range")
            continue
        functions.push_todos(todos)
        print("Item marked for completion")
    elif user_action.startswith('exit'):
        print('Bye!')
        break
    else:
        print("Invalid command")
