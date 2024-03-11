
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:17:26 2023

@author: kushal
"""

import csv
from io import StringIO
year = "2023"
# NFC
NFC_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(NFC_string)

# Define the file name for the CSV file
csv_filename = "NFC.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(NFC_string)

print(f"CSV file '{csv_filename}' has been created.")

# AFC
AFC_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(AFC_string)

# Define the file name for the CSV file
csv_filename = "AFC.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(AFC_string)

print(f"CSV file '{csv_filename}' has been created.")

# Off
Off_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(Off_string)

# Define the file name for the CSV file
csv_filename = year+"Off.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(Off_string)

print(f"CSV file '{csv_filename}' has been created.")

# PassOff
POff_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(POff_string)

# Define the file name for the CSV file
csv_filename = year+"PassingOff.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(POff_string)

print(f"CSV file '{csv_filename}' has been created.")

# RushOff
ROff_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(ROff_string)

# Define the file name for the CSV file
csv_filename = year+"RushingOff.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(ROff_string)

print(f"CSV file '{csv_filename}' has been created.")

# ScoringOff
SOff_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(SOff_string)

# Define the file name for the CSV file
csv_filename = year+"ScoringOff.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(SOff_string)

print(f"CSV file '{csv_filename}' has been created.")

# Def
Def_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(Def_string)

# Define the file name for the CSV file
csv_filename = year+"Def.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(Def_string)

print(f"CSV file '{csv_filename}' has been created.")

# PassDef
PDef_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(PDef_string)

# Define the file name for the CSV file
csv_filename = year+"PassingDef.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(PDef_string)

print(f"CSV file '{csv_filename}' has been created.")

# RushDef
RDef_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(RDef_string)

# Define the file name for the CSV file
csv_filename = year+"RushingDef.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(RDef_string)

print(f"CSV file '{csv_filename}' has been created.")

# ScoringDef
SDef_string = """
"""

# Create a CSV file from the string
csv_file = StringIO(SDef_string)

# Define the file name for the CSV file
csv_filename = year+"ScoringDef.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(SDef_string)

print(f"CSV file '{csv_filename}' has been created.")

