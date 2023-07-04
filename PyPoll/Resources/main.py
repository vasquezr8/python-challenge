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
    var = {charles_votes_counter: "Charles Casper Stockham",
            diana_votes_counter: "Diana DeGette",
            raymon_votes_counter: "Raymon Anthony Doane"}

    charles_pct = (charles_votes_counter / total_votes_counter) * 100
    charles_rounded = round(charles_pct, 3)

    diana_pct = (diana_votes_counter / total_votes_counter) * 100
    diana_rounded = round(diana_pct, 3)

    raymon_pct = (raymon_votes_counter / total_votes_counter) * 100
    raymon_rounded = round(raymon_pct, 3)

    print("Election Results")
    print("-------------------------")

    print(f"Total Votes: {total_votes_counter}")
    print("-------------------------")

    print(f"Charles Casper Stockham: {charles_rounded}% ({charles_votes_counter})")
    print(f"Diana DeGette: {diana_rounded}% ({diana_votes_counter})")
    print(f"Raymon Anthony Doane: {raymon_rounded}% ({raymon_votes_counter})")
    print("-------------------------")

    print(f'Winner: {var.get(max(var))}')
    print("-------------------------")