task = input("Enter a Task: ")
priority = input("Enter priority level (high, medium, low) ").lower()
time_bound = input("Is it time bound? (yes or no) ").lower()

match priority:
    case "high":
        print(f"'{task}' is a high priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
        