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
        for line in reader:
            url = line[3]
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
            if 'Real' in path and 'tweet' in path:
                parse_tweet_csv(path, 'TweetRealUrl.txt')
            elif 'Fake' in path and 'tweet' in path:
                parse_tweet_csv(path, 'TweetFakeUrl.txt')
            elif 'NewsReal' in path:
                parse_news_csv(path, 'NewsRealUrl.txt')
            elif 'NewsFake' in path:
                parse_news_csv(path, 'NewsFakeUrl.txt')
            else:
                continue

    # remove duplicates
    os.system("sort NewsRealUrl.txt | grep -v 'news_url' | uniq > NewsRealUrl_tmp.txt && mv NewsRealUrl_tmp.txt NewsRealUrl.txt")
    os.system("sort NewsFakeUrl.txt | grep -v 'news_url' | uniq > NewsFakeUrl_tmp.txt && mv NewsFakeUrl_tmp.txt NewsFakeUrl.txt")
    os.system("sort TweetRealUrl.txt | grep -v 'tweetid' | uniq > TweetRealUrl_tmp.txt && mv TweetRealUrl_tmp.txt TweetRealUrl.txt")
    os.system("sort TweetFakeUrl.txt | grep -v 'tweetid' | uniq > TweetFakeUrl_tmp.txt && mv TweetFakeUrl_tmp.txt TweetFakeUrl.txt")
if __name__ == '__main__':
    main()
