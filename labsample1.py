import csv



#--------- Start of Functions to be implemented for Practice Lab 1 -----------------------

##########################################################
# Function to get the workout with longest duration      #
# Parameters:                                            #
#  'workouts': List containing the CSV file contents     #
#                                                        #
# Return value:                                          #
#   'longest': Workout dictionary with max duration      #
#              or None if workouts is empty              #
##########################################################
def get_longest_workout(workouts):
    longest = None

    # Add your implementation from here
    #HINT: Loop through workouts and compare durations
    for workout in workouts:
        if longest is None or workout["duration"] > longest["duration"]: #looping through the python dic n comparing w the
           longest = workout
    return longest


##################################################################
# Function to calculate total duration of all workouts           #
# Parameters:                                                    #
#  'workouts': List containing the CSV file contents (List type) #
#                                                                #
# Return value:                                                  #
#    total: Calculated total duration                            #
##################################################################
def calc_total_duration(workouts):
    total = 0

    # Add your implementation from here
    #HINT: start with this code: for workout in workouts:
    for workout in workouts:
        total += workout["duration"]
    return total

##################################################################
# Function to calculate average duration of all workouts        #
# Parameters:                                                    #
#  'workouts': List containing the CSV file contents (List type) #
#                                                                #
# Return value:                                                  #
#    average: Calculated average duration                        #
##################################################################
def calc_average_duration(workouts):
    average = 0

    # Add your implementation from here
    #HINT: Use calc_total_duration(workouts) and len(workouts)
    average = calc_total_duration(workouts) / len(workouts)
    return average

#--------- End of Functions to be implemented for Practice Lab 1 -----------------------


##########################################################
# Function to display the main menu of the application #
# Parameters: None                                      #
# Return value = None                                   #
#########################################################
def display_menu():
    print("\n" + "=" * 40)
    print("----- Fitness Tracker -----")
    print("=" * 40)
    print("Select option")
    print("1 - Display all records")
    print("2 - Display statistics")
    print("3 - Display longest workout")
    print("Q - Quit")
    print("=" * 40)


##########################################################
# Function to read from a CSV file                      #
# Parameters: None                                       #
#                                                        #
# Return value:                                          #
#   'workouts': List containing the CSV file data        #
##########################################################
def load_csv():
    print("\nLoading CSV file database")

    workouts = []
    try:
        with open('samplelabtest1-weixiang67\workouts.csv', 'r') as file: #file path impt
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                workouts.append({
                    'date': row['date'],
                    'activity': row['activity'],
                    'duration': float(row['duration'])
                })
    except FileNotFoundError:
        print("Error: workouts.csv file not found!")
    except Exception as e:
        print(f"Error loading CSV: {e}")
    
    return workouts


##################################################################
# Function to display all records from CSV file on the console  #
# Parameters:                                                    #
#  'workouts': List containing the CSV file contents (List type) #
#                                                                #
# Return value: None                                             #
#                                                                #
##################################################################
def display_all_records(workouts):
    print("\nAll Workout Records")
    print("=" * 50)
    print(f"{'Date':<15} {'Activity':<20} {'Duration (min)':<15}")
    print("-" * 50)

    for workout in workouts:
        print(f"{workout['date']:<15} {workout['activity']:<20} {workout['duration']:<15.0f}")

    print("=" * 50)


##################################################################
# Function to display statistics for workouts                    #
# Parameters:                                                    #
#  'workouts': List containing the CSV file contents (List type) #
#                                                                #
# Return value: None                                             #
#                                                                #
##################################################################
def display_statistics(workouts):
    total_duration = calc_total_duration(workouts)
    average_duration = calc_average_duration(workouts)

    print("\nWorkout Statistics")
    print("=" * 50)
    print(f"Total Workouts: {len(workouts)}")
    print(f"Total Duration: {total_duration:.1f} minutes")
    print(f"Average Duration: {average_duration:.1f} minutes")
    print("=" * 50)


#############################
# Main Function             #
# Parameters: None          #
#                           #
# Return value: None        #
#                           #
#############################
def main():
    while True:
        display_menu()
        choice = input("Enter selection => ").strip().upper()

        # Load CSV file database
        workouts = load_csv()

        if choice == '1':
            display_all_records(workouts)
        elif choice == '2':
            display_statistics(workouts)
        elif choice == '3':
            # Get the longest workout
            longest = get_longest_workout(workouts)

            if longest:
                print("\nLongest Workout")
                print("=" * 50)
                print(f"Date: {longest['date']}")
                print(f"Activity: {longest['activity']}")
                print(f"Duration: {longest['duration']:.0f} minutes")
                print("=" * 50)
            else:
                print("\nNo workouts found!")

        elif choice == 'Q':
            print("\nThank you for using Fitness Tracker!")
            break
        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()
