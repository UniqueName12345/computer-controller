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
    # if the system is Windows, use the Windows command interpreter
    wincommands = {
        '?': 'help',
        'exit': 'exit',
        'clear': 'cls',
        'ls': 'dir',
        'cd [directory]': 'cd [directory]',
        'cat [file or directory]': 'type [file or directory]',
        'mkdir [directory]': 'mkdir [directory]',
        'rm [file or directory]': 'del [file or directory]',
        'mv [file or directory]': 'move [file or directory]',
        'cp [file or directory]': 'copy [file or directory]',
        'install [package]': 'winget install [package]',  # NOTE: Winget is a Windows package manager. It is not a
        # part of the shell.
        'uninstall [package]': 'winget uninstall [package]',  # NOTE: See above.
        'upgrade [package]': 'winget upgrade [package]',
        'search [package]': 'winget search [package]',
        'sys-info': 'systeminfo',
        'sys-info /file': 'type systeminfo > C:\\systeminfo.txt',
        'sys-info /file /save': 'systeminfo > C:\\systeminfo.txt',
        # todo: add more commands
    }
    # print the dictionary
    print(wincommands)
    # ask for user input
    user_input = input("Enter your choice: ")
    # check if the user input is in the dictionary
    if user_input in wincommands:
        # if it is, run the command
        os.system(wincommands[user_input])
    else:
        # if it is not, print an error message
        print("Command not found")

