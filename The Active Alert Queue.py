# MAC 108 Lab: The Active Alert Queue (Week 7)

#Task: Intrusions and malware alerts are passing through the terminal
#and disappear without giving us a chance to address them. Our job is
#to build an interactive, dynamic "Active Alert Queue" to log, view,
#and systematically resolve incoming threats. 

alert_queue = []

while True:
    print("System Main Menu Options:\n" \
          "1. Log New Alert\n" \
          "2. View Active Queue\n" \
          "3. Resolve Oldest Alert\n" \
          "4. Exit System"
    )
    choice = input("Select an option [1-4]: ")

    if choice == "1":
        print("Log New Alert")
        new_alert = input("Enter threat description: ")
        alert_queue.append(new_alert)
        print("Alert logged successfully.")

    elif choice == "2":
        print("---Current Pending Alerts---")
        if len(alert_queue) == 0:
            print("No Pending alerts")
        for alert in alert_queue:
            print(alert)    

    elif choice == "3":
        if len(alert_queue)!= 0:
            resolved_threat = alert_queue.pop(0)
            print(f"Resolved and cleared: {resolved_threat}")
        else: print("No Pending alerts")        

    elif choice == "4":
        break

    else:
        print("Invalid choice, please select a listed option")