'''
Script to parse the CoAID dataset for URLs that may contain images
'''

import os
import csv

def parse_news_csv(file, output):
    '''
    Parse csv news files
    '''
    with open(file, 'r') as f:
        print(file)
        reader = csv.reader(f)
        # extract the URL column
        for row in reader:
            url = row[2]
            with open(output, "a") as out_file:
                out_file.write(url + "\n")

def parse_tweet_csv(file, output):
    '''
    Parse csv tweet files
    '''
    with open(file, 'r') as f:
        print(file)
        reader = csv.reader(f)
        # extract the URL column
        for row in reader:
            tweetid = row[1]
            with open(output, "a") as out_file:
                out_file.write(f"https://twitter.com/i/web/status/{tweetid}\n")

def main():
    '''
    Main function to iterate through the CoAID dataset
    '''
    # iterate through the CoAID dataset
    CoAID_path = 'CoAID'
    for root, dirs, files in os.walk(CoAID_path):
        for file in files:
            path = os.path.join(root, file)
            if 'git' not in path and 'README.md' not in path:
                output_file = 'outputFake.txt' if 'Fake' in path else 'outputReal.txt'
                if 'tweet' in path:
                    parse_tweet_csv(path, output_file)
                else:
                    parse_news_csv(path, output_file)

if __name__ == '__main__':
    main()
