# Name: CSVCoarseFine
# Language: Python
# Input: TXT
# Output: PREFIX
# Tested with: PluMA 2.0, Python 3.6
# Dependencies: none 

PluMA plugin that will sum rows of a CSV file based on a coarse and fine classification.

The input file is a TXT file of tab-delimited keyword-value pairs:
csvfile: Name of the input CSV file (Dataset)
doboth: True if we want to do coarse and fine sums, false otherwise

In the CSV file we assume the first line is the header, and each subsequent line contains data.
The first column is assumed to be the coarse classification.
The second column is assumed to be the fine classification.

The output CSV files will contain one row per classification, corresponding to the sum of all rows in the input file.
CSV files produced:
PREFIX.coarse.csv: Coarse sums (if doboth was set to True)
PREFIX.fine.csv: Fine sums
