from todolist import TodoList

def main():
    todo_list = TodoList()

    while True:
        print('\n==== Todo List ====')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Mark Task as Completed')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input('Enter the task index to mark as completed: '))
            todo_list.mark_task_completed(task_index)
        elif choice == '4':
            print('Exiting the Todo List app. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__ == "__main__":
    main()
