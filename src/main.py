import os


def another_command():
    cmd = input("> ")
    if cmd == "quit":
        print("Bye!")
    elif os.name == "nt":
        if cmd.find(" ") == -1:
            # if it doesn't have arguments, check against the windows commands
            if cmd in windows_command_dict:
                # execute the command
                windows_command_dict[cmd]()
                another_command()

        else:
            # if it has arguments, split the command and arguments
            cmd, args = cmd.split(" ", 1)
                # check against the windows commands
            if cmd in windows_command_dict:
                # execute the command
                windows_command_dict[cmd](args)
            else:
                print("Command not found!")
            another_command()


def main():
    import os

    if os.name != 'nt':  # Windows has a separate command interpreter, thus no need to use the command line interpreter
        # for *nix systems
        global command_dict  # FIXME: could potentially cause problems, because it says that command_dict is
        # undefined at the module level
        command_dict = {
            'help [cmd]': 'man [cmd]',
            'exit': 'exit',
            'cls': 'clear',
            'dir': 'ls',
            'cd': 'cd',
            'type': 'cat',
            'mkdir': 'mkdir',
            'del': 'rm',
            'move': 'mv',
            'copy': 'cp',
            'winget-deb install': 'apt-get install',  # HACK: winget-deb is a wrapper for apt-get
            'winget-deb remove': 'apt-get remove',  # HACK: see above
            'winget-deb run': 'apt-get run',  # HACK: see above
            'winget-deb update': 'apt-get update',  # HACK: see above
            'winget-rpm install': 'yum install',  # HACK: see above
            'winget-rpm remove': 'yum remove',  # HACK: see above
            'winget-rpm run': 'yum run',  # HACK: see above
            'winget-rpm update': 'yum update',  # HACK: see above
            'winget install': 'echo \"winget install\" does not work. Depending on your system, you may need to use '
                              '\"winget-deb install\" or \"winget-rpm install\" instead.',
            # NOTE: This multiline string is used a little strangely here.
            'winget remove': 'echo \"winget remove\" does not work. Depending on your system, you may need to use '
                             '\"winget-deb remove\" or \"winget-rpm remove\" instead.',
            # NOTE: And here.
            'winget run': 'echo \"winget run\" does not work. Depending on your system, you may need to use '
                          '\"winget-deb '
                          'run\" or \"winget-rpm run\" instead.',
            # NOTE: Here too!
            'winget update': 'echo \"winget update\" does not work. Depending on your system, you may need to use '
                             '\"winget-deb update\" or \"winget-rpm update\" instead.',
            # NOTE: Here.
            'winget-deb': 'echo \"winget-deb\" does not work. Use \"winget-deb install\", \"winget-deb remove\", '
                          '\"winget-deb run\", or \"winget-deb update\" instead.',
            # NOTE: Here.
            'winget-rpm': 'echo \"winget-rpm\" does not work. Use \"winget-rpm install\", \"winget-rpm remove\", '
                          '\"winget-rpm run\", or \"winget-rpm update\" instead.',
            # NOTE: Here.
            'winget': 'echo \"winget\" does not work. Use \"winget install\", \"winget remove\", \"winget run\", '
                      'or \"winget update\" instead.',
            # NOTE: Here.
            'apt-get': 'echo \"apt-get\" does not work. Use \"winget-deb install\", \"winget-deb remove\", '
                       '\"winget-deb '
                       'run\", or \"winget-deb update\" instead.',
            # NOTE: Here.
            'yum': "echo \"yum\" does not work. Use \"winget-rpm install\", \"winget-rpm remove\", \"winget-rpm run\", "
                   "or \"winget-rpm update\" instead.",
            # NOTE: And finally... Here.
            'apt-get install': 'echo \"apt-get install\" does not work. Use \"winget-deb install\" instead.',
            # TODO: add even more commands
        }
        # print a neatened form of the command dictionary
        print('\n'.join([f'{key}: {value}' for key, value in command_dict.items()]))
        # ask for user input
        user_input = input("Enter your choice: ")
        # check if the user input is in the dictionary
        if user_input in command_dict:
            # if it is, run the command
            os.system(command_dict[user_input])
            another_command()
        else:
            # if it is not, print an error message
            print("Command not found")
    else:
        # if the system is Windows, use the Windows command interpreter
        global windows_command_dict  # FIXME: could potentially cause problems, because it says that command_dict is
        # undefined at the module level
        windows_command_dict = {
            'man [cmd]': 'help [cmd]',
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
        # print a neatened form of the command dictionary
        print(
            '\n'.join(
                [
                    f'{key}: {value}'
                    for key, value in windows_command_dict.items()
                ]
            )
        )

        # ask for user input
        user_input = input("Enter your choice: ")
        # check if the user input is in the dictionary
        # unless it has arguments, in which case, compare the first word of the user input to the key
        if user_input.split()[0] in windows_command_dict:
            # if it is, run the command with the arguments
            os.system(windows_command_dict[user_input])
            # after each command, print a new line
            print()
            # then, ask the user for another command
            another_command()
        else:
            # if it is not, print an error message
            print("Command not found")


# if the program is run as a package, error out
if __name__ != '__main__':
    print("This program is not meant to be run as a package. Please run it as a script.")
    exit(1)
else:
    # if the program is not run as a package, run the main function
    main()
