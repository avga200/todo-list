def add(s):
    todos = list()
    with open("todos.txt","r") as file:
        todos = file.readlines()
    todos.append(s)
    with open("todos.txt","w") as file:
        for element in todos:
            element = element.strip()
            file.write(element + '\n')
def get_todos():
    todo = list()
    with open('todos.txt','r') as file:
        todos = file.readlines()
        for i in todos:
            todo.append(i.strip())
    return todo
def edit(one, two):
    todos = get_todos()
    ind = todos.index(two)
    todos[ind] = one
    with open("todos.txt","w") as file:
        for element in todos:
            element = element.strip()
            file.write(element + '\n')

def complete(s):
    try:
        todos = get_todos()
        todo = list()
        for i in todos:
            todo.append(i.strip())


        todo.remove(s[0])
        with open("todos.txt","w") as file:
            for i in todo:
                i = i.strip()
                file.write(i+'\n')
    except:
        print('enter ')
def display(todos):
    with open("todos.txt", 'w') as file:
        for element in todos:
            element = element.strip('\n')
            file.write(element + '\n')


if __name__ == '__main__':
    print('This file should be used as a module')
