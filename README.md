# Computer controller


## Introduction
 Control your computer with one single python script
(note: some actions require admin privileges, when asked, simply give it needed admin perms)

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

For linux migrators (i.e. Ubuntu, Debian, Mint, etc.), you can use commands from windows.
For example, to install a package, you can use:
```
winget install package-name
```

For Windows migrators (i.e. Windows 10, Windows 8.1, etc.), you can use commands from linux.
For example, to print something to a file, you can use:
```
cat "message" > C:\path\to\file.txt
```

**NOTE THAT NOT ALL COMMANDS ARE SUPPORTED.** For example, NT users can't use the `sudo` command. _(yet, anyway)_

## Dependencies
Currently only uses the following dependencies:
* [python3](https://www.python.org/downloads/)
* [git](https://git-scm.com/downloads) (at least until releases get added)
* [os](https://docs.python.org/3/library/os.html)