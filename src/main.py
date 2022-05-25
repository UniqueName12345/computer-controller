import os

if os.name != 'nt':  # Windows has a separate command interpreter, thus no need to use the command line interpreter
    # for *nix systems
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
        # NOTE: This is not a builtin command, but an apt-get command. It is not a part of the shell. Thus,
        # it only works with Debian-based systems.
        'install-rpm': 'yum install',
        # NOTE: This is not a builtin command, but a yum command. It is not a part of the shell. Thus, it only works
        # with Redhat-based systems.
        'install-pacman': 'pacman -S',
        # NOTE: This is not a builtin command, but a pacman command. It is not a part of the shell. Thus,
        # it only works with Arch-based systems.
        'install-brew': 'brew install',
        # NOTE: This is not a command, but a brew command. It is not a part of the shell. Thus, it only works with
        # MacOS-based systems.
    }
    # print the dictionary
    print(commands)
    # ask for user input
    user_input = input("Enter your choice: ")
    # check if the user input is in the dictionary
    if user_input in commands:
        # if it is, run the command
        os.system(commands[user_input])
    else:
        # if it is not, print an error message
        print("Command not found")
else:
    # if the system is Windows, run the command interpreter
    os.system("cmd")
