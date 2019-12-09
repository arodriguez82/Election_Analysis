# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our Dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# County Options and county votes
county_options = []
county_votes = {}
# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}
# County Turnout
largest_county = ""
largest_count = 0
largest_percentage = 0
# Track Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Get county name from each row
        county_name = row[1]
        # If county name does not match existing, add it to county list
        if county_name not in county_options:
            # Add county name to county list
            county_options.append(county_name)
            # Begin tracking county vote count
            county_votes[county_name] = 0
        # Add a vote to county total
        county_votes[county_name] += 1

        # Get the candidate name from each row
        candidate_name = row[2]
        # If the candidate name does not match an existing candidate add it to the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to the text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine voter turnout percentage for each county
    for county in county_votes:
        # Retrieve total voter count for each county
        voterturnout = county_votes[county]
        # Calculate voter turnout percentage
        turnout_percentage = float(voterturnout) / float(total_votes) * 100
        # Print voter turnout to terminal
        turnout_results = (f"{county}: {turnout_percentage:.1f}% ({voterturnout:,})\n")
        print(turnout_results)
        # Save voter turnout to text file
        txt_file.write(turnout_results)

        # If statement to determine county with largest voter turnout
        if (voterturnout > largest_count) and (turnout_percentage > largest_percentage):
            largest_count = voterturnout
            largest_percentage = turnout_percentage
            largest_county = county
    
    # Print largest voter turnout to terminal    
    voterturnout_summary = (
        f"\n---------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"---------------------\n")
    print(voterturnout_summary)
    # Save largest voter turnout to text file
    txt_file.write(voterturnout_summary)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate in candidate_votes: 
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidate's name
            winning_candidate = candidate

    # To do: print out the winning candidate, vote count and percentage to the terminal
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)