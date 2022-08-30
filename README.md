# Name: CSVCoarseFine
# Language: Python
# Input: CSV
# Output: CSV
# Tested with: PluMA 2.0, Python 3.6
# Dependencies: none 

PluMA plugin that will sum rows of a CSV file based on a coarse and fine classification.

The input file is a CSV file where we assume the first line is the header, and each subsequent line contains data.
The first column is assumed to be the coarse classification.
The second column is assumed to be the fine classification.

The output CSV file will contain one row per coarse and fine classification, corresponding to the sum of all rows in the input file.
