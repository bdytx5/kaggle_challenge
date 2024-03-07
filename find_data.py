

import os
import pandas as pd


# Directory containing the CSV files
directory = '/Users/brettyoung/Desktop/dev_24/kaggle_credit/data/home-credit-credit-risk-model-stability/csv_files/test/first_100s'


# Required columns based on your initial list
required_columns = ['totaldebt_9A', 'overdueamountmax_155A', 'profession_152M', 'pmtaverage_3A', 'maritalst_385M', 'gender_992L','education_1103M',
    'actualdpd_943P', 'amount_1115A', 'annualeffectiverate_63L', 'annuity_780A', 
    'applications30d_658L', 'avgmaxdpdlast9m_3716943P', 'credamount_590A', 
    'currdebt_22A', 'dpdmax_139P', 'numactivecreds_622L'
]


# Dictionary to hold the filenames and their associated matching columns
matched_files = {}


# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # Check if the file is a CSV file
        file_path = os.path.join(directory, filename)  # Full path of the file
        try:
            # Read only the headers to check the columns
            df = pd.read_csv(file_path, nrows=0)
            # Find any matching required columns in the CSV
            matching_columns = [column for column in required_columns if column in df.columns]
            if matching_columns:  # If there are any matching columns
                matched_files[filename] = matching_columns  # Add filename and matching columns to the dictionary
        except Exception as e:
            print(f"Error reading {filename}: {e}")


# Print out matched files and their associated matches
print("CSV files containing any of the required columns and their associated matches:")
for filename, matches in matched_files.items():
    print(f"{filename}: {matches}")


