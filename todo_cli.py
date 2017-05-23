# python 3

import datetime


class ToDoList:
    """
    This class represents a todolist with functionality to:
    - add items
    - remove items
    - print the list
    - write list contents to a persistent text file
    - manage and sort by item priority
    - attach deadlines to list items using datetimes (and sort by deadline)
    """

    # initialize the ToDo list itself, as a class variable
    def __init__(self):
        self.task_list = []
        print('\nToDo List command options:\nadd, del, view, save, quit\n')

    def add_task(self, task_string, priority, days_from_now):
        self.task_list.append([
            task_string,
            priority,
            datetime.datetime.now().date() + datetime.timedelta(days=days_from_now)])

    def del_task(self, index):
        self.task_list.pop(index)

    # before printing the list to console, sort the list of lists by priority OR deadline
    def view_list(self, sort_method):
        if sort_method == 'p':
            self.task_list.sort(key=lambda x: x[1])
        else:
            self.task_list.sort(key=lambda x: x[2])

        print('\nCurrent ToDo List:\n')
        for index, task in enumerate(self.task_list):
            print(index + 1, ": ", task[0], "~ Priority:", task[1], "~ Deadline:", task[2])

    def save_list(self, sort_method):
        if sort_method == 'p':
            self.task_list.sort(key=lambda x: x[1])
        else:
            self.task_list.sort(key=lambda x: x[2])
        
        # catch IOerrors while writing the list to a text file
        try:
            f = open('todo_list_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.txt', 'w')
            f.write('Current ToDo List:\n')
            for index, task in enumerate(self.task_list):
                f.write(str(index + 1) + ': ' + str(task[0]) + ' ~ Priority: ' + str(task[1]) + ' ~ Deadline: ' + str(task[2]) + '\n')
        except IOError as e:
            print('Error: ', e)
        finally:
            if f:
                f.close()


if __name__ == "__main__":
    
    # create a single instance of the ToDoList class
    todo_list = ToDoList()

    # CLI loop to interact with the list object
    while True:
        user_input = input('\nEnter a command, or "quit" to quit:\n')

        if user_input == 'quit':
            break

        elif user_input == 'add':
            new_task = input(
                '\nEnter a new task:\n- task statement,\n- priority level (1, 2, or 3),\n- integer no. of days from TODAY as due date (1 means tomorrow).\nSeparate args with comma and space:\n')
            new_task_parsed = new_task.split(', ')
            todo_list.add_task(
                # task string
                new_task_parsed[0],
                # task priority
                int(new_task_parsed[1]),
                # task deadline
                int(new_task_parsed[2]))

        elif user_input == 'del':
            killed_task = input('\nEnter task index to delete:\n')
            # convert 0-based indexes to 1-based for readability
            todo_list.del_task(int(killed_task) - 1)

        elif user_input == 'view':
            sort_method = input('\nSorting method - enter "p" for priority, or "d" for deadline:\n')
            while sort_method not in ['p', 'd']:
                sort_method = input('\nInput not "p" or "d". Try again:\n')
            todo_list.view_list(sort_method)

        elif user_input == 'save':
            sort_method = input('\nSorting method - enter "p" for priority, or "d" for deadline:\n')
            while sort_method not in ['p', 'd']:
                sort_method = input('\nInput not "p" or "d". Try again:\n')
            todo_list.save_list(sort_method)

        else:
            print('\nCommand not recognized.\n')