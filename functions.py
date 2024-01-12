FILEPATH="tedes.txt"


def get_todos(filepath='tedes.txt'):
    """Read a textfile and return the list of To-do items.
    """
    with open(filepath, 'r') as file:
         todos_local=file.readlines()
    return todos_local
def write_todos(todos_arg,filepath='tedes.txt'):
    """Write the To-do items list in a textfile"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__=="__main__":
    print("Hello")
    print(get_todos())