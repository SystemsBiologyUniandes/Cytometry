import pandas as pd
import fcsparser
import os

#####
def make_dir(path):
    '''
    Checks if the provided path exists and if it doesn't creates it

    Arguments
    --
    path: (string) path - pointing to the desired folder in memory
    '''
    if not os.path.exists(path):
        os.makedirs(path)
    
def listFiles(directory, extension):
    '''
    Lists the file names with a certain extension in a certain directory. Afterwards stores the filenames in a list.

    Arguments
    --
    directory: (string) Path to the directory where files should be listed
    extension: (string) desired extension (ie. .csv, .fsc, .py, etc...)
    '''
    files = [file for root, dirs, files in os.walk(directory) for file in files if file.endswith(extension)]
    #print(extension + " files in " + directory + " listed")
    return files 

def fcs_to_csv(fcs_directory, csv_directory):
    '''
    converts .fcs files extracted from a cytometer into conventional .csv files.
    
    Arguments
    --
    fcs_directory: (string) Directory where the .fcs files are stored
    csv_directory: (string) Directory where the .csv files are to be stored
    '''
    files = listFiles(fcs_directory, '.fcs')
    make_dir(csv_directory)
    for i in files:
        path = fcs_directory + i
        meta, data = fcsparser.parse(path, meta_data_only=False, reformat_meta=True)
        data.columns=['FSC-A','SSC-A','FL1-A','FL2-A','FL3-A','FL4-A','FSC-H','SSC-H','FL1-H','FL2-H','FL3-H','FL4-H','Width','Time']
        data.to_csv(csv_directory +'/'+ i[:-3]+'csv', index=False)
        
def merge_dfs(csv_dir,merged_csv_dir,merged_filename):
    '''
    Merges all .csv files into one, and adding an extra identifier column.

    Arguments
    --
    csv_dir:(string) Directory containing all csv files
    merged_csv_dir: (string) Directoy where the merged file is to be stored
    merged_filename: (string) Name for the merged file
    '''    
    files = listFiles(csv_dir, '.csv')
    df = pd.read_csv(csv_dir  + files[0])
    df['name'] = files[0][:-3]
    for i in files[1:]:
        df1 = pd.read_csv(csv_dir  + i)
        df1['name'] = i[:-3]
        df = df.append(df1)
    
    make_dir(merged_csv_dir)
    df.to_csv(merged_csv_dir +'/'+ merged_filename +'.csv',index=False)
