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
            print(url)

def parse_tweet_csv(file, output):
    '''
    Parse csv tweet files
    '''

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
                if 'tweet' in path:
                    parse_tweet_csv(path, 'output.csv')
                else:
                    parse_news_csv(path, 'output.csv')

if __name__ == '__main__':
    main()
