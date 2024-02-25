# Financial Analysis and Election Vote Counting with Python

## Background

I tackled two challenges: PyBank and PyPoll. Both tasks simulated real-world scenarios where Python scripting skills were essential.

## PyBank

In PyBank, I analyzed the financial records of a company using Python. The financial dataset, budget_data.csv, contained two columns: "Date" and "Profit/Losses". My script calculated the following values:

- Total number of months
- Net total amount of profit/losses
- Changes in profit/losses over the entire period, along with the average change
- Greatest increase in profits (date and amount)
- Greatest decrease in profits (date and amount)

## PyPoll

In PyPoll, I modernized a small, rural town's vote-counting process using Python. The poll data, election_data.csv, contained three columns: "Voter ID", "County", and "Candidate". My script calculated the following values:

- Total number of votes cast
- List of candidates who received votes
- Percentage of votes each candidate won
- Total number of votes each candidate won
- Winner of the election based on popular vote

## Conclusion

I wrote separate scripts for each dataset and ensured they worked correctly for their respective data. Upon completion, both scripts printed the analysis to the terminal and exported a text file with the results.

## Code Citations

Convert Variables to Integers:
(Found in lines 24 and 28 of main.py PyBank file)

https://www.stechies.com/typeerror-unsupported-operand-types-int-str/#:~:text=But%20while%20doing%20so%2C%20a,have%20the%20same%20data%20type.

Rounding Numbers in Python:
(Found in line 45 of main.py PyBank file and lines 37, 40, and 43 of main.py PyPoll file)

https://www.freecodecamp.org/news/how-to-round-to-2-decimal-places-in-python/

Return Top Votes Getter Using Dictionary and Max Function:
(Found in lines 32-34, 56, and 72 of main.py PyPoll file)

https://stackoverflow.com/questions/52205011/how-to-get-max-to-return-variable-names-instead-of-values-in-python
