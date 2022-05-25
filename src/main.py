import os

commands = {
    'help': 'help',
    'exit': 'exit',
    'clear': 'clear',
    'ls': 'ls',
    'cd': 'cd',
    'pwd': 'pwd',
    'cat': 'cat',
    'mkdir': 'mkdir',
    'rm': 'rm',
    'mv': 'mv',
    'cp': 'cp',
    'install-deb': 'apt-get install',
    # NOTE: This is not a command, but an apt-get command. It is not a part of the shell. Thus, it only works with
    # Debian-based systems.
    'install-rpm': 'yum install',
    # NOTE: This is not a command, but a yum command. It is not a part of the shell. Thus, it only works with
    # Redhat-based systems.
    'install-pacman': 'pacman -S',
    # NOTE: This is not a command, but a pacman command. It is not a part of the shell. Thus, it only works with
    # Arch-based systems.
    'install-brew': 'brew install',
    # NOTE: This is not a command, but a brew command. It is not a part of the shell. Thus, it only works with
    # MacOS-based systems.
}
# ask for user input
user_input = input("Enter your choice: ")
# if user_input is 1
if user_input == "1":
    # show all processes
    os.system(
        "ps -A")  # NOTE: I believe this is not the best way to do this. For example, I could import the subprocess
    # module.
# if user_input is 2
elif user_input == "2":
    # show all processes by user
    user = input("Enter the user: ")
    os.system("ps -u " + user)  # NOTE: same as above
# if user_input is 3
elif user_input == "3":
    # show all processes by name
    name = input("Enter the name: ")
    os.system("ps -f -C " + name)  # NOTE: same as above
# if user_input is 4
elif user_input == "4":
    # show all processes by name and user
    name = input("Enter the name: ")
    user = input("Enter the user: ")
    os.system("ps -u " + user + " -f -C " + name)  # NOTE: same as above
# if user_input is 5
elif user_input == "5":
    # show all processes by name and user and status
    name = input("Enter the name: ")
    user = input("Enter the user: ")
    status = input("Enter the status: ")
    os.system("ps -u " + user + " -f -C " + name + " -s " + status)  # NOTE: same as above
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
    # save current process id
    pid = os.getpid()
    # kill all processes apart from the current one AND the parent process AND explorer.exe
    os.system("kill -9 $(ps -eo pid | grep -v " + str(pid) + " | grep -v " + str(os.getppid()) + "| grep -v "
                                                                                                 "explorer.exe)")
# if user_input is 10
elif user_input == "10":
    # kill a process repeatedly
    pid = input("Enter the pid: ")
    os.system("kill -9 " + pid)  # TODO: add debug messages
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
    print("Please enter a valid choice!")  # NOTE: Well, to be honest, I don't know how to do this.
