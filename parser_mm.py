import os
import json


def parse_urls_json(file, reliable_output, unreliable_output):
    """
    Parse JSON news files based on reliability
    """
    with open(file, 'r') as f:
        first_line = f.readline()
        try:
            item = json.loads(first_line)
            print("Keys in the first JSON object:", item.keys())
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return

        f.seek(0)  # Reset file pointer to the beginning
        for line in f:
            try:
                item = json.loads(line)
                url = item.get('ref_source_url')  # Use get to safely access the key
                reliability = item.get('label')  # Use get to safely access the key
                if url is None or reliability is None:
                    print(f"Skipping line due to missing data: {line}")
                    continue
                if reliability == 'fake':
                    output_file = unreliable_output
                else:
                    output_file = reliable_output
                with open(output_file, "a") as out_file:
                    out_file.write(url + "\n")
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line}")
            except KeyError as e:
                print(f"Key error: {e} in line: {line}")


def main():
    """
    Main function to parse the specified ReCoVery dataset file based on reliability
    """
    # Specify the dataset file path
    MM_path = 'news_collection.json'  # Update this path for JSON file

    # Output file paths
    reliable_output = 'MMreliableUrls3.txt'
    unreliable_output = 'MMunreliableUrls3.txt'

    # Parse the dataset file
    parse_urls_json(MM_path, reliable_output, unreliable_output)

    # Remove duplicates
    os.system(f"sort {reliable_output} | uniq > {reliable_output}_tmp && mv {reliable_output}_tmp {reliable_output}")
    os.system(
        f"sort {unreliable_output} | uniq > {unreliable_output}_tmp && mv {unreliable_output}_tmp {unreliable_output}")


if __name__ == '__main__':
    main()
