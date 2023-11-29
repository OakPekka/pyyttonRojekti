import csv
import os


file_path = 'file2.csv'
stop_substring = '15:30'
copy_file_path = "file4.csv"
apu_taulukko = []
apu_boolean = False
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not apu_boolean:
            found_in_row = any(stop_substring in column_data for column_data in row)
            if found_in_row:
                apu_boolean = True
                stop_column_index = row.index(next((column_data for column_data in row if stop_substring in column_data), None))
                apu_taulukko.append(row[:stop_column_index + 1])
                break  
            else:
                apu_taulukko.append(row)  

print(apu_taulukko)

with open(copy_file_path, 'w', newline='') as copyfile:
    writer = csv.writer(copyfile)
    writer.writerows(apu_taulukko)
