# Cytometry

to [install](https://github.com/eyurtsev/fcsparser) fcsparser:  pip install fcsparser

FCSparser - converts a bunch of fcs files to csv files and plots some statistics
Work in progress - plots the thing

Troubleshooting:
- Check for filepaths
- Check folders exist

To Do:
- Turn Work in progress into a functional plotting script 
- Come up with original names
- migrate to python script
- Green fluorescence statistics
- Add median for each variable
- Specify the filter for E. coli. 
- make jointplots and matrixplots with seaborn.

Done:
- Make FCSparser output a second DF with the summary statistics: created in ./csv_data/Statistics_csv/statistics.csv.
- Add number of events per cell	 in statistics DataFrame: new column in the statistics df named n_events.

Contact us: ca.sanchez1209@uniandes.edu.co
