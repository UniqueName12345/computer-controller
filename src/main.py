import os

print("""
System controller!
1. Show all processes
2. Show all processes by user
3. Show all processes by name
4. Show all processes by name and user
5. Show all processes by name and user and status
6. Show all processes by name and status
7. Show all processes by user and status
8. Kill a process
9. Kill all processes
10. Kill a process repeatedly
11. Kill all processes repeatedly
12. Kill a process by name
13. Shutdown the system""") # TODO: should I use a dictionary?
# ask for user input
user_input = input("Enter your choice: ")
# if user_input is 1
if user_input == "1":
    # show all processes
    os.system("ps -A")
# if user_input is 2
elif user_input == "2":
    # show all processes by user
    user = input("Enter the user: ")
    os.system("ps -u " + user)
# if user_input is 3
elif user_input == "3":
    # show all processes by name
    name = input("Enter the name: ")
    os.system("ps -f -C " + name)
# if user_input is 4
elif user_input == "4":
    # show all processes by name and user
    name = input("Enter the name: ")
    user = input("Enter the user: ")
    os.system("ps -u " + user + " -f -C " + name)
# if user_input is 5
elif user_input == "5":
    # show all processes by name and user and status
    name = input("Enter the name: ")
    user = input("Enter the user: ")
    status = input("Enter the status: ")
    os.system("ps -u " + user + " -f -C " + name + " -s " + status)
# if user_input is 6
elif user_input == "6":
    # show all processes by name and status
    name = input("Enter the name: ")
    status = input("Enter the status: ")
    os.system("ps -f -C " + name + " -s " + status)
# if user_input is 7
elif user_input == "7":
    # show all processes by user and status
    user = input("Enter the user: ")
    status = input("Enter the status: ")
    os.system("ps -u " + user + " -f -s " + status)
# if user_input is 8
elif user_input == "8":
    # kill a process
    pid = input("Enter the pid: ")
    os.system("kill " + pid)
# if user_input is 9
elif user_input == "9":
    # kill all processes
    os.system("killall")
# if user_input is 10
elif user_input == "10":
    # kill a process repeatedly
    pid = input("Enter the pid: ")
    os.system("kill -9 " + pid)
# if user_input is 11
elif user_input == "11":
    # kill all processes repeatedly
    os.system("killall -9")
# if user_input is 12
elif user_input == "12":
    # kill a process by name
    name = input("Enter the name: ")
    os.system("killall " + name)
# if user_input is 13
elif user_input == "13":
    # shutdown the system
    os.system("shutdown -h now")
# if user_input is not 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
else:
    # show error
    print("Error!")
    print("Please enter a valid choice!")