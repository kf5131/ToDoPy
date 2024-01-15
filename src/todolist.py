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
