# Opentensor_Mountain
This repo contains python script which can fetch opentensor mountain dataset from IPFS hashes in more diversified and effective approach and save it in multiple file with different encodings.

# Installation

## 1. Clone the repository
```sh
git clone https://github.com/Kunj-2206/Opentensor_Mountain.git
```
## 2. Move to the directory
```sh 
cd Opentensor_Mountain
```
## 3. Install all the packages
```sh
pip3 install -r requirements.txt  
```
## 4. Run the following command (if you are running it first time)
```sh
python3 data_mountain.py --clone true
```

# Usage

## ex Arguement
```sh
python3 data_mountain.py --ex 20
```
It fetch 20 examples from each sources and by default it will fetch 1000 example and note that it will fetch distinct example

## clone Arguement
```sh
python3 data_mountain.py --clone true
```
It clone opentensor/text-mountain github repo to current directory since it needs to fetch hashes from all this opentensor files 
If you already clone this repo in current working directory then you can set --clone false

## Dataset
The script will save example of each sources to text file and atlast it is storing all examples in 3 types of format in file so it can be used from there or you can just take raw_dataset from script which is Dataset variable and load into your model script 
