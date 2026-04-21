import  re
import csv

#TODO: add to this program
    # clean the data using your functions 
    # write the cleaned data into a new csv file (optional but helpful for next step)
    # put the cleaned data into a dataframe
    #    - use your cereal_analysis python file as a template to read from csv

with open('alumni_anonymized.csv') as records:
    reader = csv.reader(records)
    entries = [] #this will store the rows in dictionary form
    next(reader)  #skip header
    count = 0
    for row in reader:
        new_row = dict()
        if count< 6:
            print(row)
            print(row[0])
            new_row['Exit_Year'] = row[1]
            new_row['Last_Name'] = row[0]
            entries.append(new_row)
        count+=1

with open('alumni_clean.csv', 'w', newline='') as new_file:
    csv_writer = csv.DictWriter(new_file,fieldnames=['Last_Name','Exit_Year'])
    csv_writer.writeheader()
    csv_writer.writerows(entries)
