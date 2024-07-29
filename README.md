# PyBank
To begin this analysis, I imported both csv and os libraries. 


### Questions to answer: 

--The total number of months included in the dataset

--The net total amount of "Profit/Losses" over the entire period

--The changes in "Profit/Losses" over the entire period, and then the average of those changes

--The greatest increase in profits (date and amount) over the entire period

--The greatest decrease in profits (date and amount) over the entire period


### Variables, constants, and lists that were added in the Python file:

--monthCount (variable) 

--totalProfits (variable)

--dateMonth (list)

--netMOverM (list)

--greatestProfit (list) min value "0"

--greatestLoss (list) max value "999999999999999"


### Steps
I reviewed the budget_data_csv. Each row represents one month and the profit/loss for that period.

I separated the headers from the data. 

Using a for loop I gathered a count of rows to get the total number of months and the total profits from profit/loss.

Within the for loop I calculated the difference between the previous month's profit/loss value and the current month's value and added them to the list "netMOverM".

From that list, I identified the month and amount of the greatest increase in profit month-over-month and the value of the greatest decrease.

Using the values from "netMOverM" and the number of months within the data, I could determine the average change month-to-month of the data overall.

I formatted output values to answer each of the above questions and then saved that output to a text file. 




# PyPoll
To begin this analysis, I imported both csv and os libraries. 


### Questions to answer: 

--The total number of votes cast

--A complete list of candidates who received votes

--The percentage of votes each candidate won

--The total number of votes each candidate won

--The winner of the election based on popular vote


### Variables, constants, and lists that were added in the Python file:

--totalVotes (variable) 

--candidateVotes (dictionary)

--electedCandidate (empty string)

--electedCacndidateVotes (variable)



### Steps
I reviewed the budget_data_csv. Each row represents one vote and contains the Ballot ID, Count, and Candidate. 

I separated the headers from the data. 

Using a for loop I gathered a count of rows to get the total number of votes cast as well as compile a list of the distinct candidates.

In each loop, the candidate name would be compared to a list of candidates. If the candidate was not already listed, they were added and a count of votes for that candidate was initialized.

I saved the list of candidates and their vote count within a string. 

Within another for loop I used the totalVotes and the candidateVotes to calculate the percentage of all votes each candidate won. This also identified which candidate won the election.

I formatted an output that answered the above questions.

The output was saved to a text file.
