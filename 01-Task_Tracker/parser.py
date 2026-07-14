import sys
import main 

commands = {
    "add":main.add,
    "list":main.list
}

command = sys.argv

if len(command) >1 and command[1] in commands:
    if len(command)>2:
        commands[command[1]](command[2])
    else:
        commands[command[1]]()