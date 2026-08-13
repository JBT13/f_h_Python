def browser_navigation():
    back_stack = []
    forward_stack = []

    print("Browser History Simulator")
    print("Commands: visit <url>, back, forward, exit")

    while True:
        user_input = input("> ").strip().split()
        if not user_input:
            continue
            
        command = user_input[0].lower()

        if command == "visit":
            if len(user_input) < 2:
                print("Error: Please specify a page name.")
                continue
            
            new_page = user_input[1]
            back_stack.append(new_page)
            forward_stack.clear()
            print(f"Visited: {back_stack[-1]}")

        elif command == "back":
            if len(back_stack) <= 1:
                print("Error: No history to go back to.")
            else:
                popped_page = back_stack.pop()
                forward_stack.append(popped_page)
                print(f"Back to: {back_stack[-1]}")

        elif command == "forward":
            if not forward_stack:
                print("Error: No forward history.")
            else:
                popped_page = forward_stack.pop()
                back_stack.append(popped_page)
                print(f"Forward to: {back_stack[-1]}")

        elif command == "exit":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    browser_navigation()