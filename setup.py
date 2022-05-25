import setuptools

install = input("Install? (y/n) ")
if install == "y":
    setuptools.setup(
        name="computer_controller",
        version="0.1",
        description="A controller for the computer",
        author="UniqueName12345",
        author_email="[email protected]",
        url="https://github.com/UniqueName12345/computer-controller",
        packages=["os"]
    )
else:
    print("Aborting...")
    exit()
