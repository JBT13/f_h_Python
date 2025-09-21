n = int(input())
count = {
    "entry" : "entered",
    "exit" : "exited"
}
log = {}
list = []

for _ in range(n):
    officer = input()
    action, name = officer.split()

    status = count.get(action)
    if status:
        message = f"{name} {status}"

        if (action == "entry" and name in log) or (action == "exit" and name not in log):
            message += " (ANOMALY)"
        
        if action == "entry":
            log[name] = True
        elif action == "exit":
            log.pop(name, None)
        
        list.append(message)

for i in list:
    print(i)

    