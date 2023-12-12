def display(todos):
    with open("todos.txt", 'w') as file:
        for element in todos:
            element = element.strip('\n')
            file.write(element + '\n')