import re

# The multiline string containing the raw data from the website.

speakers_raw = """    A Bessas 1
    A Bingham 1
    A Cuni 3
    A Garassino 1
    A Jesse Jiryu Davis 13
    A Kanterakis 1
    Žygimantas Medelis 1"""
    
# Split the string into a list of individual lines.
speakers_list = speakers_raw.splitlines()

csv_lines = []

# The Regex Breakdown:
# ^\s* : Matches any leading whitespace at the beginning of the line
# (.*)   : Group 1 - Captures the speaker's name (greedy match until the last space)
# \s     : Matches the space between the name and the number
# (\d+)  : Group 2 - Captures one or more digits
# $      : Ensures the digits are at the end of the string
regex = re.compile(r"^\s*(.*)\s(\d+)$")

for line in speakers_list:
    # Use re.sub to replace the entire line with Group 1, a comma, and Group 2
    # \1 represents the name, \2 represents the number
    csv_line = regex.sub(r"\1,\2", line)
    csv_lines.append(csv_line)

# Combine the list back into a single string separated by newlines
csv_content = "\n".join(csv_lines)

# Write the result to speakers.csv
with open("speakers.csv", "w", encoding="utf-8") as file:
    file.write(csv_content)

print("File 'speakers.csv' has been created successfully.")