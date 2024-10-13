


def read_releases(file_name):   #This defines a function called read_releases that takes in the name of the file (file_name) as an argument.
    """ Reads the releases from the file and returns a list of tuples (delivery_day, duration). """
    releases = []    #Creates an empty list called releases to store the data that will be read from the file.
    
    
    with open(file_name, 'r') as file: #Opens the file in "read" mode ('r') using the file name passed as the argument.
                                     #The with statement ensures the file is properly closed after reading.
        
        
        for line in file:    #Loops through each line of the file.
            delivery_day, duration = map(int, line.strip().split()) #Removes any leading/trailing whitespace 
                                                                    #using strip() and splits the line into 
                                                                    # two parts (delivery day and duration) based on spaces.
                                                                    #Converts the split values into integers using map(int, ...)
            
            
            releases.append((delivery_day, duration))  #Appends each pair of values (delivery_day, duration) as a tuple to the releases list.
    return releases

def select_releases(releases):   #Defines a function select_releases that takes the list of releases (tuples of delivery day and duration) as input.


    """ Selects the maximum number of releases Bob can validate within the 10-day sprint. """
    releases.sort()  # Sort releases by delivery day (and duration if necessary)
    selected_releases = []  #Creates an empty list called selected_releases to store the releases that Bob can validate within the 10-day sprint.
    current_day = 0      #nitializes a variable current_day to track Bob's available time. Initially, it is set to 0, meaning Bob can start from day 1.

    for release in releases:
        
        delivery_day, duration = release  #Unpacks the tuple release into two variables: delivery_day and duration.
        
        if delivery_day >= current_day and (delivery_day + duration - 1) <= 10:  #This checks two conditions:
                                                                                 #The release can start only on or after the current_day (no overlap).
                                                                                 #The release should finish before or on day 10, i.e., (delivery_day + duration - 1) <= 10.
            # If Bob can start on delivery_day and finish within 10 days, select the release
            
            selected_releases.append((delivery_day, delivery_day + duration - 1))  #If the release satisfies the conditions, 
                                                                                    #it is added to the list selected_releases with its start and end day.
            current_day = delivery_day + duration  # Updates current_day to the next available day, which is the day after Bob finishes the current release.
    return selected_releases

def write_solution(file_name, selected_releases):  #Defines a function write_solution that takes the output file name (file_name) 
                                                    #and the list of selected_releases as input.
    """ Writes the solution to the file with the maximum number of releases and their days. """
    with open(file_name, 'w') as file:
        file.write(f"{len(selected_releases)}\n")     #Writes the number of selected releases (i.e., the length of the selected_releases list) as the first line in the output file.
        for release in selected_releases:   
            file.write(f"{release[0]} {release[1]}\n")

def main():   
    # Step 1: Read input from the file
    releases = read_releases('releases.txt')   #Calls the read_releases function to read the releases data 
                                                #from releases.txt and stores the result in releases.
    
    # Step 2: Select the maximum number of releases
    selected_releases = select_releases(releases)  #selected_releases = select_releases(releases): 
                                                   #Calls the select_releases function to select the maximum number of releases Bob can handle within the sprint, storing the result in selected_releases
    
    # Step 3: Write the output to the solution file
    write_solution('solution.txt', selected_releases)  #Calls the write_solution function to write the results to solution.txt.
    # Run the program

main()
