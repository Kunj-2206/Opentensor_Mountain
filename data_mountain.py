import json
from datasets import Dataset, DatasetDict, load_dataset
import requests
import os
import argparse

def str_to_bool(value):
    if value.lower() in ['true', 'yes', '1']:
        return True
    elif value.lower() in ['false', 'no', '0']:
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected (true/false, yes/no, 0/1)')

parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--ex", help="Add number of examples", required=False, type=int)
parser.add_argument("--clone", help="text-moutain github cloning", required=False, type=str_to_bool)

args = parser.parse_args()
print(args)

if(args.clone):
    os.system("git clone https://github.com/opentensor/text-mountain.git")
if(not os.path.exists('text-mountain/')):
    print(f'text-mountain github repo is not present in current directory {os.getcwd()}')
    print(f'Usage: python3 data_mountain.py --clone true')
    exit()
print("Cloning is done, Fetching examples now......")
dataset_dict = {"text": []}
filenames = ["ArXiv", "BookCorpus2", "Books3", "DMMathematics", "EnronEmails", "EuroParl", "Gutenberg_PG", "HackerNews", "NIHExPorter", "OpenSubtitles", "PhilPapers", "UbuntuIRC", "YoutubeSubtitles"]

if(args.ex):
    no_of_ex=args.ex
    print(f"Number of example is being updated to {no_of_ex}")
else:
    no_of_ex = 1000
    print("Number of example is having default value of 1000 per sources")
for file in filenames:
    print(f"******************** Now Trying {file} *******************************")  
    with open(f"text-mountain/{file}.lf", "r") as fr:
        data = fr.read()

    file_list = json.loads(data)
    hash_list = [file_dict["Hash"] for file_dict in file_list]
    hash_set = set(hash_list)
    c=0
    distict_examples = set()
    for hash in hash_set:
        # Set up the URL for the IPFS API endpoint
        url = f"http://ipfs.opentensor.ai/api/v0/object/get?arg={hash}"

        # Make a GET request to the API endpoint
        response = requests.post(url)
        # Print the content of the response
        if(response.status_code!=404 and no_of_ex>0):
            data = json.loads(response.content.decode('utf-8'))["Data"]
            distict_examples.add(data)
            c+=1

            print(f"################### {file}_ getting example: {c} ######################")  
            

        if(len(distict_examples)>=no_of_ex):
            print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$ Writing data to  {file} $$$$$$$$$$$$$$$$$$$$$$$$$$")
            dataset_dict["text"].extend(list(distict_examples))
            with open(f'data_sample_{file}.txt', 'w', encoding='utf8') as f:
                f.write(json.dumps(dataset_dict, ensure_ascii=False))
                break
    
    with open(f'data_sample_ascii_enc.txt', 'w', encoding='utf8') as f:
        f.write(json.dumps(dataset_dict, ensure_ascii=True))

    with open(f'data_sample_enc.txt', 'w', encoding='utf8') as f:
        f.write(json.dumps(dataset_dict, ensure_ascii=False))

    with open(f'data_sample_no_enc.txt', 'w') as f:
        f.write(json.dumps(dataset_dict))


raw_train = Dataset.from_dict(dataset_dict)
