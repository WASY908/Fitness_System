# Fitness Tracker System
# Initialize tracker function
def tracker():
    track = {
        #sample activities data
        #running data bydefault    
        "Running": [{"Activity": "Running", "Duration": 30.0, "Calories Burned": 30, "Date": "2024-6-2"}],
        #Walking data bydefault
        "Walking": [{"Activity": "Walking", "Duration": 50.0, "Calories Burned": 50, "Date": "2024-5-2"}],
        #Swimming data bydefault
        "Swimming": [{"Activity": "Swimming", "Duration": 70.0, "Calories Burned": 50, "Date": "2024-7-7"}],
        #Cycling data bydefault
        "Cycling": [{"Activity": "Cycling", "Duration": 80.0, "Calories Burned": 30, "Date": "2024-4-2"}],
        #hiking data bydefault
        "Hiking": [{"Activity": "Hiking", "Duration": 90.0, "Calories Burned": 120, "Date": "2024-6-2"}],
    }
    return track

# Add activity function
def add_activity(track):
    act_type = input("Enter activity type (Cycling, Swimming, Running, Walking, Hiking): ").strip()
    try:
        duration = float(input("Enter the duration in minutes: "))
        calories = float(input("Enter Calories Burned: "))
        date = input("Enter Date (YYYY-MM-DD): ").strip()

        add_new_activity = {
            "Activity": act_type,
            "Duration": duration,
            "Calories Burned": calories,
            "Date": date
        }

        if act_type in track:
            track[act_type].append(add_new_activity)
        else:
            track[act_type] = [add_new_activity]

        print("Activity added successfully!")
    except ValueError:
        print("Invalid input. Please enter numerical values for duration and calories burned.")

# Display activities function
def display(track):
    if not track:
        print("No activities found.")
        return
    for act_type, activities in track.items():
        print(f"\nActivities for {act_type}:")
        for activity in activities:
            print(f"  - Activity: {activity['Activity']}, Duration: {activity['Duration']} mins, "
                  f"Date: {activity['Date']}, Calories Burned: {activity['Calories Burned']} kcal")

# Search activity function
def search_act(tracker):
    act_type = input("Enter the activity type to search: ").strip()
    if act_type in tracker:
        print(f"\nActivities for {act_type}:")
        for activity in tracker[act_type]:
            print(f"  - Activity: {activity['Activity']}, Duration: {activity['Duration']} mins, "
                f"Date: {activity['Date']}, Calories Burned: {activity['Calories Burned']} kcal")
    else:
        print(f"No activities found for type: {act_type}")

# Menu function
def menu():
    print("\nMenu:")
    print("1. Add Activity")
    print("2. Display Activity Summary")
    print("3. Search for Activity")
    print("4. Exit")

# Main function
def main():
    trac = tracker()
    print("Welcome to the Fitness Management System! Your fitness, my responsibility!")

    while True:
        menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_activity(trac)
        elif choice == "2":
            display(trac)
        elif choice == "3":
            search_act(trac)
        elif choice == "4":
            print("Exiting the Fitness Tracker. Stay healthy and live happily!")
            break
        else:
            print("Invalid choice. Please try again.")

# Program run
if __name__ == "__main__":
    main()




        


    


