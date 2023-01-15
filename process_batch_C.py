"""
Amanda Hanway 
Assignment A1: Setup and Datagram Sockets

Batch Process - third transformation

Reads from a file, transform, write to a new file.

In this case, covert degree K to degree F.
Formula: f = (K − 273.15) × 9/5 + 32  

"""

import csv

# set file names
input_file_name = "batchfile_2_kelvin.csv"
output_file_name = "batchfile_3_farenheit.csv"

#open the input and output files
input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w", newline='')

# create file reader and writer
reader = csv.reader(input_file, delimiter=",")
writer = csv.writer(output_file, delimiter=",")

# define header column names and write to output file
header = next(reader)
header_list = ["Year","Month","Day","Time","TempF"]
writer.writerow(header_list)

for row in reader:
    #access the kelvin temp file
    Year, Month, Day, Time, TempK = row

    #convert kelvin to fahrenheit using this formula: 
    # f = (K − 273.15) × 9/5 + 32  
    TempF = round((float(TempK)-273.15) * 9/5 + 32, 2)

    #write the fahrenheit temps to the new output file
    writer.writerow([Year, Month, Day, Time, TempF])

# close files
output_file.close()
input_file.close()