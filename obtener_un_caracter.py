import os, platform
if platform.system() == "Windows":
    import msvcrt

def getch():
    if platform.system() == "Linux":
        os.popen("bash -c \"read -n 1\"")
    else:
        msvcrt.getch()


print("Type a key!")
x = getch()
print("Okay\n")
print x
