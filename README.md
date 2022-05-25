# Computer controller


## Introduction
 Control your computer with one single python script
(note: some actions require admin / sudo privileges, when asked, simply give it needed admin perms)

## How to Install
Since there are no releases, you need to install the latest version from source. TODO: add releases

First, install git [here](https://git-scm.com/downloads) if you don't have it already.

Then, clone the repository using the command:
```
git clone https://github.com/UniqueName12345/computer-controller
```

Then, go into the /src folder and run the following command:
```
python3 main.py
```

And now, you can control your computer as you wish!

## How to use

For linux migrators/users, you can use commands from windows.
For example, to install a package, you can use:
```
winget install package-name
```

For Windows migrators/users (i.e. Windows 10, Windows 8.1, etc.), you can use commands from linux.
For example, to print something to a file, you can use:
```
cat "message" > C:\path\to\file.txt
```

**NOTE THAT NOT ALL COMMANDS ARE SUPPORTED.** For example, NT users can't use the `sudo` command, and Linux users can't use the `cmd` command. _Or at least, not currently._

## How to Give Permissions

For Windows users, follow the instructions [here](https://www.windowscentral.com/how-set-apps-always-run-administrator-windows-10).

For Linux users, first, you need to login as root (i.e. `sudo su -`).

Then, you need to install the `doas` package using the command `sudo apt-get install doas`


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
* [git](https://git-scm.com/downloads) (at least until releases get added)
* [os](https://docs.python.org/3/library/os.html)
* Nothing else! :D

## Credits
Me and Github Copilot, currently.

## Contributing

To contribute, please fork the repository and submit a pull request.

## One more thing....

Goodbye.