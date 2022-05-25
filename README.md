# Computer controller


## Introduction
 Control your computer with one single python script
(note: some actions require admin / sudo privileges, when asked, simply give it needed admin perms)

## How to Install
There is a setup script that will install all the dependencies and the controller script.

Run the setup script:
```
python setup.py install
```
And then type in `y` to install.

And now, you can control your computer as you wish!*

###### *With limitations which we will get to later.

## How to uninstall
Accidentally installed it? Changed your mind? （；へ：） Do not fear!

Simply run:
```
pip uninstall computer_controller
```
And then type in `y` to uninstall.

To fully uninstall, you need to remove the folder called `computer_controller.egg-info`. This is `rm -rf computer_controller.egg-info` in bsh, or `del computer_controller.egg-info` in cmd.

Then, if you want to install it again, refer back to [the installation section.](#How-to-Install)

## How to run
Since this is a PACKAGE, you can make a python file that imports this package and then run it.

Open up your ide of choice, make a new python file, and type in:
```
import computer_controller
computer_controller.main()
```

Then, you can run the script by typing in `python name.py` in the command line.

## How to use

For linux users (i.e. Ubuntu, Debian, Arch, etc.), you can use the commands from Windows.
Example: `dir` in Windows is `ls` in Linux.

For Windows migrators/users (i.e. Windows 10, Windows 8.1, etc.), you can use commands from linux.
For example, to print something to a file, you can use `cat "message" > /path/to/file`

**NOTE THAT NOT ALL COMMANDS ARE SUPPORTED.** For example, NT users can't use the `sudo` command, and Linux users can't use the `cmd` command. _Or at least, not currently._

## How to Give Permissions

For Windows users, follow the instructions [here](https://www.windowscentral.com/how-set-apps-always-run-administrator-windows-10).

For Linux users, first, you need to login as root (i.e. `sudo su -`).

Then, you need to install the `doas` package using the command `apt-get install doas`


Then, you need to add main.py to the `/etc/sudoers` file using the command:
```
echo "doas ALL=(ALL) NOPASSWD: /usr/bin/python3 /home/user/path/to/main.py" >> /etc/sudoers
```

Then, you need to log back into your account using the `exit` command.

Then, you can run the script using the command:
```
sudo doas /usr/bin/python3 /home/user/path/to/main.py
```

## Dependencies
It currently only uses the following dependencies:
* [python3](https://www.python.org/downloads/)
* ~~[git](https://git-scm.com/downloads) (at least until releases get added)~~ no need for git anymore. You can still install from source, however.
* [os](https://docs.python.org/3/library/os.html)
* Nothing else! :D

## Credits
Me and GitHub Copilot, currently.

## Contributing
To contribute, please fork the repository and submit a pull request.
