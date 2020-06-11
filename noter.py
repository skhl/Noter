import datetime
import os.path
import os

tag_sign = "#"

def gettime():
    return datetime.datetime.now().strftime("%H:%M:%S")

def checkfileexists():
    if not os.path.isfile(datetime.datetime.now().strftime("%Y%m%d") + ".txt"):
        writeline("")

def writeline(text_line):
    with open(datetime.datetime.now().strftime("%Y%m%d") + ".txt", "a") as text_file:
        text_file.write(format(text_line) + "\n")
    readfile(datetime.datetime.now().strftime("%Y%m%d") + ".txt")

def sliceatspace(line):
    for i in range(0, len(line)):
        if line[i] == " ":
            return i
def removelastline(filename):
    f = open(filename, "r")
    file_content = f.readlines()
    f.close()
    with open(filename, "w") as text_file:
        for line in file_content[:-1]:
            text_file.write(format(line))
    readfile(datetime.datetime.now().strftime("%Y%m%d") + ".txt")


def readfile(filename):
    os.system("cls||clear")
    f = open(filename, "r")
    file_content = f.readlines()
    f.close()
    tags = []
    notes = []
    #date = file_content[0]
    for line in file_content:
        if line[0] == tag_sign:
            tags.append(line)
        else:
            notes.append(line)
    print(filename)
    tags.sort()
    for tag in tags:
        print(tag.rstrip())
    print("\n")
    for note in notes:
        print(note.rstrip())

def options(i):
    if i[1:5] == "exit":
        exit(1)
    elif (i[1:5] == "read"):
        if len(i) == 5:
            checkfileexists()
            readfile(datetime.datetime.now().strftime("%Y%m%d") + ".txt")
        elif os.path.isfile(i[6:len(i)] + ".txt"):
            readfile(i[6:len(i)] + ".txt")
        else:
            print("No file found.")
    elif (i[1:5] == "open"):
        print("Function comming")
    elif(i[1:5] == "undo"):
        removelastline(datetime.datetime.now().strftime("%Y%m%d") + ".txt")
    elif(i[1:5] == "time"):
        if len(i)>5:
            writeline(gettime() + " " + i[6:len(i)])
        else:
            writeline(gettime())
    elif(i[1:5] == "help"):
        print("#exit - Exit the application\n")
        print("#read - Read the content of the current file\n")
        print("#read YYYYMMDD - Read the content of the file with the filename\n")
        print("#undo - Undo the last commit\n")
        print("#time - Add a time stamp and an optional header\n")

    else:
        writeline(i)

def f():
    i = input()
    if len(i) > 0:
        if i[0] == tag_sign:
            options(i)
            return f()
        else:
            writeline(i)
        return f()
    return f()

def init():
    checkfileexists()
    readfile(datetime.datetime.now().strftime("%Y%m%d") + ".txt")
    f()

init()