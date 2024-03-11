#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:17:26 2023

@author: kushal
"""

import csv
from io import StringIO

# Sample string to convert to CSV
csv_string = """Tm,W,L,W-L%,PF,PA,PD,MoV,SoS,SRS,OSRS,DSRS
Philadelphia Eagles*,8,1,.889,252,195,57,6.3,-1.5,4.9,5.1,-0.2
Dallas Cowboys+,6,3,.667,269,165,104,11.6,-2.7,8.8,8.0,0.8
Washington Commanders,4,6,.400,217,274,-57,-5.7,-3.1,-8.8,-1.8,-7.0
New York Giants,2,8,.200,118,266,-148,-14.8,1.4,-13.4,-10.7,-2.7
Detroit Lions*,7,2,.778,241,203,38,4.2,0.4,4.6,6.6,-2.0
Minnesota Vikings+,6,4,.600,233,209,24,2.4,0.7,3.1,2.4,0.7
Green Bay Packers,3,6,.333,179,182,-3,-0.3,-1.6,-1.9,-2.9,1.0
Chicago Bears,3,7,.300,204,255,-51,-5.1,-1.9,-7.0,-1.9,-5.2
New Orleans Saints*,5,5,.500,214,198,16,1.6,-1.0,0.6,-0.1,0.7
Tampa Bay Buccaneers,4,5,.444,178,173,5,0.6,0.8,1.4,-2.4,3.8
Atlanta Falcons,4,6,.400,189,217,-28,-2.8,-1.0,-3.8,-3.3,-0.5
Carolina Panthers,1,8,.111,153,242,-89,-9.9,0.8,-9.1,-6.5,-2.6
San Francisco 49ers*,6,3,.667,252,143,109,12.1,0.8,13.0,7.1,5.8
Seattle Seahawks*,6,3,.667,200,201,-1,-0.1,-1.4,-1.5,0.0,-1.5
Los Angeles Rams,3,6,.333,178,204,-26,-2.9,2.4,-0.5,-1.5,1.1
Arizona Cardinals,2,8,.200,176,263,-87,-8.7,1.8,-6.9,-3.2,-3.7
"""

# Create a CSV file from the string
csv_file = StringIO(csv_string)

# Define the file name for the CSV file
csv_filename = "NFC.csv"

# Write the contents of the string to a CSV file
with open(csv_filename, "w", newline="") as file:
    file.write(csv_string)

print(f"CSV file '{csv_filename}' has been created.")






