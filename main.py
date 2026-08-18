print("JARVIS App Started")

while True:
    cmd = input("You: ")

    cmd = cmd.lower()

    if cmd == "hello":
        print("JARVIS: Hello buddy, nenu Jarvis.")

    elif cmd == "name":
        print("JARVIS: Naa peru Jarvis buddy.")

    elif cmd == "time":
        import datetime
        now = datetime.datetime.now()
        print("JARVIS:", now)

    elif cmd == "joke":
        print("JARVIS: Why did the computer go to doctor? Because it had a virus.")

    elif cmd == "exit":
        print("JARVIS: Bye buddy.")
        break

    else:
        print("JARVIS: Command ardham kaaledu.")
