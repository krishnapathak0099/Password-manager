def add():
    app = input("Enter app name: ")
    usr = input("Enter username: ")
    pss = input("Enter password: ")

    with open("password.txt", "a") as f:
        f.write(f"{app} | {usr} | {pss}\n")

    print("Saved successfully!")


def view():
    with open("password.txt", "r") as f:
        for line in f:
            print(line.strip())


def search():
    app_name = input("Enter app name to search: ")

    found = False

    with open("password.txt", "r") as f:
        for line in f:
            data = line.strip().split(" | ")

            if len(data) == 3:
                app, usr, pss = data

                if app.lower() == app_name.lower():
                    print("\nFOUND:")
                    print("App:", app)
                    print("Username:", usr)
                    print("Password:", pss)
                    found = True
                    break

    if not found:
        print("App not found")


while True:
    print("""
    PASSWORD MANAGER
1. add
2. view
3. search
4. quit
""")

    chs = input("Enter choice: ")

    if chs == "1" or chs == "add":
        add()

    elif chs == "2" or chs == "view":
        view()

    elif chs == "3" or chs == "search":
        search()

    elif chs == "4" or chs == "quit":
        print("Exiting...")
        break

    else:
        print("Invalid choice")