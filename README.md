Apriori Algorithm Project
This project implements the Apriori Algorithm in Python, designed for mining frequent itemsets and generating association rules from transaction data. It uses a custom implementation of the Apriori Algorithm without relying on built-in data mining libraries. The program takes user-defined support and confidence thresholds to find frequent patterns and meaningful associations within a dataset.

Table of Contents
Features
Getting Started
Usage
Implementation Details
Example Output
License
Features
Accepts custom input for minimum support and confidence values.
Processes a transactional dataset to discover frequent itemsets.
Generates association rules based on the frequent itemsets found.
Displays execution time for analyzing efficiency.

Implementation Details
Hashing: Uses a hashing mechanism to store item support values efficiently.
Candidate Generation: Creates candidate sets from frequent itemsets, pruning any that fall below the minimum support.
Support and Confidence Calculation: Calculates support and confidence values for each candidate set, keeping those that meet the minimum thresholds.
Execution Time Measurement: Measures the algorithm's runtime for performance assessment.
Example Output
sql
Copy code
Please enter minimum support: 
0.2
Please enter minimum confidence: 
0.5

Database: Amazon

Rule 1 (2 item set):
{'item1'} --> {'item2'} [support: 30.0%, confidence: 75.0%]
Invalid Rule
-------------------------------
Rule 2 (3 item set):
...

Apriori Algorithm Execution time: 0.002345 seconds
