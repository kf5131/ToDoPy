import sqlite3


class TodoList:
    def __init__(self):
        self.tasks = []
        self.conn = sqlite3.connect('todo.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT
            )
        ''')
        self.conn.commit()

    def add_task(self, task):
        self.tasks.append(task)
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
        self.conn.commit()
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ?', (task_index,))
            self.conn.commit()
            print(f'Task "{completed_task}" marked as completed.')
        else:
            print('Invalid task index.')

    def __del__(self):
        self.conn.close()

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
