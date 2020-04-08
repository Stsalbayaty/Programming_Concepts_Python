
# hold shift tab (control / to comment out)
def GetMenuChoice(userList):
    # userList = todoList 
    
#todolist wasnt passed
    print("1) Add Item to list")
    print("2) Remove Item from list")
    print("3) Display List")
    print("4) Quit Program")

    choice = int(input("Please choose from the menu:"))
    while choice < 1 or choice > 4:
        choice = int(input("Must choose from the menu options:"))

    if choice == 1:
        userList = AddItem(userList)
    elif choice == 2:
        userList = RemoveItem(userList)
    elif choice == 3:
        print(userList)
    return choice

def AddItem(todoList):

    value = (input("Please enter the next To-Do item: "))
    todoList.append(value)
    return todoList

def RemoveItem(todoList):
    print(todoList)

    targetVal = (input("Enter a value to remove from the list:"))

    if targetVal in todoList:
        todoList.remove(targetVal)
        print(todoList)
    else:
        print(targetVal, "not found in the list")
    return todoList


#scoping not passing list
#mutable vs immutable
#double click shift
#hotkeys
def main():
    todoList = []
    choice = 0
    while choice != 4:
        choice = GetMenuChoice(todoList)


main()
    


