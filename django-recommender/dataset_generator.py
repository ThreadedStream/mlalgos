import os
import pandas as pd
import argparse
import wget
import django


'''
    To avoid problem with accessing django's models
'''
os.environ["DJANGO_SETTINGS_MODULE"] = 'mlproject.settings'
django.setup()

from bookapp.models import *

'''
    Script for loading book data from a csv file and turning it into multitude of 
    book model instances
'''

parser = argparse.ArgumentParser(description='Populating book model using data in csv file')
parser.add_argument('remote', metavar='remote', type=str, help='Indicates whether data should be downloaded from network\n')
parser.add_argument('--path', metavar='path', type=str, help='Path to a csv file. Specify this option in case if "remote" option is set to true')

'''
    @Reads csv file and returns instance of DataFrame
'''

def load_csv(path):
    df = pd.read_csv(path,error_bad_lines=False)
    return df

def fetch_book_data(url):
    file = wget.download(url)
    return file

def transform(df):
    print(df.head())

def main():
    args = parser.parse_args()
    df = None
    if args.remote == '1': 
        fetch_book_data('https://www.kaggle.com/jealousleopard/goodreadsbooks?select=books.csv')
    else:
        if args.path:
            df = load_csv(args.path)
        else:
            print('Please, specify a path argument.')
            return

    transform(df)

main()
