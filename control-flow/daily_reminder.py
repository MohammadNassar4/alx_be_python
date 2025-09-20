Task = input("Enter your task: ")
Time_Bound = input("Is it time-bound? (yes / no): ").lower()
Priority = input("Priority (high / medium / low): ").lower()

match Priority:
    case "high":
        print(f"'{Task}' is a high priority task that requires immediate attention today!")
    case "medium":
        if Time_Bound == "yes":
            print(f"'{Task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"'{Task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        print(f"'{Task}' is a low priority task. Consider completing it when you have free time.")
        