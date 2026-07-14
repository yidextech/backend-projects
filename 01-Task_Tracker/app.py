import sys 
import main
args = sys.argv
args.extend([0]*(4-len(args)))
command = args[1]

match command:
    case "list":
        if args[2]:
            main.list(args[2])
        else:
            main.list()
    case "add":
        main.add(args[2])
    case "update":
        main.update_task(int(args[2]), args[3])
    case "mark-in-progress":
        main.update_status(int(args[2]), args[1])
    case "mark-done":
        main.update_status(int(args[2]), args[1])
    case "delete":
        main.delete_task(int(args[2]))
    
    case _:
        print("Wrong Command")


