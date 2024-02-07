accounts = {}
acc_data = {}
usrname = ""

print("Welcome to the TODO app")

def login():
  print("Enter your username")
  usrname = input()
  if usrname not in accounts:
    print("Username does not exist")
     return ''
    print("Enter your password")
    psswrd = input()
    salt = accounts[usrname]['salt']
    entered_password_hashed = _functions.hash_password(psswrd, salt)
    if entered_password_hashed == accounts[usrname]['hashed_password']:
        print("Login successful.")
        return usrname
    else:
        print("Incorrect password.")

def register_user():
    print("Type username")
    usrname = input()
    if usrname in accounts:
        print("Username already exists.")
        return
    print("Type password")
    psswrd = input()
    salt = _functions.generate_salt()
    hashed_password = _functions.hash_password(psswrd, salt)
    accounts[usrname] = {'hashed_password': hashed_password, 'salt': salt}
    print("Registration successful.")

def add_task(usrname):
    print("Enter task description")
    task_description = input()
    if usrname in acc_data:
        acc_data[usrname].append(task_description)
    else:
        acc_data[usrname] = [task_description]
    print("Task added successfully.")

def view_tasks(usrname):
    if usrname in acc_data:
        print("Your tasks:")
        for task in acc_data[usrname]:
            print("- " + task)
    else:
        print("No tasks found.")

def start():
    print("What is your username?")
    usrname = login()
    if usrname != '':
        print("$")
        if usrname in acc_data:
            print("#")
            view_tasks(usrname)
            print(acc_data)
        else:
            print("No tasks found.")
    else:
        print("Want to register? Yes/No")
        answer = input()
        if answer == "Yes":
            register_user()
            start()

        while True:
            print("Choose an option:")
            print("1. Add task")
            print("2. View tasks")
            print("3. Exit")
            option = input()
            if option == "1":
                add_task(usrname)
            elif option == "2":
                view_tasks(usrname)
            elif option == "3":
                break
            else:
                print("Invalid option. Please try again.")

start()
