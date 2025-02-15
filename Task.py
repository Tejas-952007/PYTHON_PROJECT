# Define a list to store tasks
todo_list = []

# Function to display the to-do list
def show_list():
    print("\nTEJAS TO-DO LIST:")
    if len(todo_list) == 0:
        print("The list is empty!")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' has been added.")

# Function to remove a task
def remove_task(task_number):
    if task_number <= len(todo_list) and task_number > 0:
        removed_task = todo_list.pop(task_number - 1)  # Remove task based on the index
        print(f"Task '{removed_task}' has been removed.")
    else:
        print("Invalid task number.")

# Function to run the program
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show list")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        # Ask the user for an option
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            show_list()
        elif choice == '2':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '3':
            show_list()  # Show the current list
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
