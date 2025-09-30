shopping_list = []

def add_item(item):
    shopping_list.append(item)

def remove_item(item):
    shopping_list.remove(item)

def display_list():
    for item in shopping_list:
        print("•", item)

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add = input("Enter the item you want to add: ")
            add_item(add)
        elif choice == '2':
            remove = input("Enter the item you want to remove: ")
            remove_item(remove)
        elif choice == '3':
            display_list()
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()