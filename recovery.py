import os
import csv

#Parse the urls for Recovery dataset
def parse_news_csv(file, output, reliability_column_index):
    '''
    Parse csv news files based on reliability column
    '''
    with open(file, 'r') as f:
        reader = csv.reader(f)
        # extract the URL column and reliability column
        for line in reader:
            url = line[2]
            reliability = int(line[reliability_column_index])
            if reliability == 0:
                with open(output, "a") as out_file:
                    out_file.write(url + "\n")

def main():
    '''
    Main function to iterate through the CoAID dataset
    '''
    # iterate through the recovery dataset
    ReCoVery_path = 'recovery-news-data'
    reliability_column_index = 12
    for root, dirs, files in os.walk(ReCoVery_path):
        for file in files:
            path = os.path.join(root, file)
            if 'reliable' in file:
                parse_news_csv(path, 'reliableUrls.txt', reliability_column_index)
            elif 'unreliable' in file:
                parse_news_csv(path, 'unreliableUrls.txt', reliability_column_index)

    # remove duplicates
    os.system("sort reliableUrls.txt | grep -v 'news_url' | uniq > reliableUrls_tmp.txt && mv reliableUrls_tmp.txt reliableUrls.txt")
    os.system("sort unreliableUrls.txt | grep -v 'news_url' | uniq > unreliableUrls_tmp.txt && mv unreliableUrls_tmp.txt unreliableUrls.txt")

if __name__ == '__main__':
    main()
