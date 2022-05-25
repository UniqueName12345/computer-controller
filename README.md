# Computer controller


## Introduction
 Control your computer with one single python script
(note: some actions require admin / sudo privileges, when asked, simply give it needed admin perms)


## How to run

You can run the controller script by typing in `python [path]/src/main.py` in your terminal.

## How to use

For linux users (i.e. Ubuntu, Debian, Arch, etc.), you can use the commands from Windows.
Example: `dir` in Windows is `ls` in Linux.

For Windows migrators/users (i.e. Windows 10, Windows 8.1, etc.), you can use commands from linux.
For example, to print something to a file, you can use `cat "message" > /path/to/file`

**NOTE THAT NOT ALL COMMANDS ARE SUPPORTED.** For example, NT users can't use the `sudo` command, and Linux users can't use the `cmd` command. _Or at least, not currently._

## How to Give Permissions

For Windows users, follow the instructions [here](https://www.windowscentral.com/how-set-apps-always-run-administrator-windows-10).

For Linux users, first, you need to login as root (i.e. `sudo su -`).

Then, you need to install the `doas` package using the command `apt-get install doas` (sudo is insecure, so use `doas` instead).

Then, you need to add main.py to the `/etc/sudoers` file using the command:
```
doas echo "doas ALL=(ALL) NOPASSWD: /usr/bin/python3 /home/user/path/to/main.py" >> /etc/sudoers
```

Then, you need to log back into your account using the `exit` command.

Then, you can run the script using the command:
```
sudo doas /usr/bin/python3 /home/user/path/to/main.py
```

## Dependencies
It currently only uses the following dependencies:
* [python3](https://www.python.org/downloads/)
* [git](https://git-scm.com/downloads) **if you want to install from source**
* [os](https://docs.python.org/3/library/os.html)
* Nothing else! :D

## Credits
Me and GitHub Copilot, currently.

## Contributing
To contribute, please fork the repository and submit a pull request.
