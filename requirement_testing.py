import os

def requirement_testing():
    with open("requirements.txt", "r") as file:
        required_depend = file.readlines()
        required_depend = [line.strip() for line in required_depend]
    current_depend = os.popen("pip list").readlines()
    current_depend = [package.strip().split(" ")[0] for package in current_depend[2:]]

    missing_depend = []
    for depend in required_depend:
        if depend not in current_depend:
            missing_depend.append(depend)

    if len(missing_depend) == 0:
        print("All dependencies are installed.")
    else:
        print("The following dependencies are missing: [Install the current mentioned version]")
        for depend in missing_depend:
            print(depend)