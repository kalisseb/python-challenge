import csv
import os

# Variables
totalVotes = 0
candidateVotes = {}
electedCandidate = ""
electedCandidateVotes = 0

# File path
file_path = 'python-challenge/PyPoll/Resources/election_data.csv'

with open(file_path, 'r') as csvFile:
    csvRead = csv.reader(csvFile)

    # Identifying the header
    header = next(csvRead)

    # Getting a running list of distinct candidates and their total votes
    for row in csvRead:
        totalVotes += 1
        candidateName = row[2]

        # If the candidate's name is not in the dictionary, add it to the list and begin their vote count
        if candidateName not in candidateVotes:
            candidateVotes[candidateName] = 0
        candidateVotes[candidateName] += 1

# create a string to accumulate candidate summaries
candidateSummaryStr = ""

# Determine each candidate's vote count, percentage of votes, and which candidate was elected
for candidate, votes in candidateVotes.items():
    percentOfVotes = (votes / totalVotes) * 100
    if votes > electedCandidateVotes:
        electedCandidateVotes = votes
        electedCandidate = candidate

    # Accumulate candidate summaries
    candidateSummaryStr += f"{candidate}: {percentOfVotes:.3f}% ({votes})\n"

# Prepare the final formatted results summary
resultsSummary = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"-------------------------\n"
)

# Combine the results summary with the candidate summaries
resultsSummary += candidateSummaryStr

# Add the formatted election winner results
resultsSummary += (
    f"-------------------------\n"
    f"Winner: {electedCandidate}\n"
    f"-------------------------\n"
)

# Print the results to the terminal
print(resultsSummary)

#save summary to text file
outputDirectory = 'python-challenge\\PyPoll\\Analysis'
outputFilePath = os.path.join(outputDirectory, 'election_analysis.txt')

os.makedirs(outputDirectory, exist_ok=True)

with open (outputFilePath, 'w') as file:
    file.write(resultsSummary)

print(f"Results saved to {outputFilePath}")
