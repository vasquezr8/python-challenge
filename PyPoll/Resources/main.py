import os
import csv

with open("election_data.csv") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_votes_counter = 0
    charles_votes_counter = 0
    diana_votes_counter = 0
    raymon_votes_counter = 0

    for row in csvreader:

        candidate = row[2]

        total_votes_counter = total_votes_counter + 1

        if candidate == "Charles Casper Stockham":
            charles_votes_counter = charles_votes_counter + 1

        elif candidate == "Diana DeGette":
                diana_votes_counter = diana_votes_counter + 1

        else:
                raymon_votes_counter = raymon_votes_counter + 1

    # Summary table outside of loop
    print("Election Results")
    print("-------------------------")

    print(f"Total Votes: {total_votes_counter}")
    print("-------------------------")

    print(f"{charles_votes_counter}")
    print(f"{diana_votes_counter}")
    print(f"{raymon_votes_counter}")