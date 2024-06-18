'''
Script to parse a specific ReCoVery dataset file for URLs based on reliability
'''

import os
import csv

def parse_urls_csv(file, reliable_output, unreliable_output):
    '''
    Parse csv news files based on reliability
    '''
    with open(file, 'r') as f:
        #print(file)
        reader = csv.reader(f)
        # iterate through each line in the csv file
        for line in reader:
            url = line[2]  # 3rd column
            reliability = line[11]  # 12th column
            if reliability == '0':
                output_file = unreliable_output
            else:
                output_file = reliable_output
            with open(output_file, "a") as out_file:
                out_file.write(url + "\n")


def main():
    '''
    Main function to parse the specified ReCoVery dataset file based on reliability
    '''
    # Specify the dataset file path
    ReCoVery_path = 'recovery-news-data.csv'  # Update this path

    # Output file paths
    reliable_output = 'reliableUrls.txt'
    unreliable_output = 'unreliableUrls.txt'

    # Parse the dataset file
    parse_urls_csv(ReCoVery_path, reliable_output, unreliable_output)

    # Remove duplicates
    os.system(f"sort {reliable_output} | uniq > {reliable_output}_tmp && mv {reliable_output}_tmp {reliable_output}")
    os.system(f"sort {unreliable_output} | uniq > {unreliable_output}_tmp && mv {unreliable_output}_tmp {unreliable_output}")

if __name__ == '__main__':
    main()
