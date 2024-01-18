import sqlite3

class TodoList:
    def __init__(self, db_name='todo.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                completed INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_task(self, task):
        self.cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
        self.conn.commit()
        print(f'Task "{task}" added.')

    def view_tasks(self):
        self.cursor.execute('SELECT * FROM tasks WHERE completed = 0')
        tasks = self.cursor.fetchall()

        if not tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for task in tasks:
                print(f'{task[0]}. {task[1]}')

    def mark_task_completed(self, task_id):
        self.cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
        self.conn.commit()
        print(f'Task with ID {task_id} marked as completed.')

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
            task_id = int(input('Enter the task ID to mark as completed: '))
            todo_list.mark_task_completed(task_id)
        elif choice == '4':
            print('Exiting the Todo List app. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

    todo_list.conn.close()

if __name__ == "__main__":
    main()
