def add_todo(element):
    with open('todos.txt', 'a') as file:
        file.write(element + '\n')


def get_todos(filename='todos.txt'):
    todo = list()
    with open(filename, 'r') as file:
        todos = file.readlines()
        for i in todos:
            todo.append(i.strip())
    return todo


def push_todos(todos, filename='todos.txt'):
    with open(filename, 'w') as file:
        for element in todos:
            element = element.strip('\n')
            file.write(element + '\n')


def edit_todo(new_element, old_element):
    try:
        todos = get_todos()
        index_element = todos.index(old_element)
        todos[index_element] = new_element
        push_todos(todos)
    except:
        print('Select a to-do')

def complete(todo):
    try:
        todos = get_todos()
        todos.remove(todo[0])
        with open("todos.txt", "w") as file:
            for i in todos:
                file.write(i + '\n')
    except IndexError:
        print('Select an option')


if __name__ == '__main__':
    print('This file should be used as a module')
