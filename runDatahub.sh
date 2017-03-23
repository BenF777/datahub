#!/bin/bash

#Define inputs

source_folder=test #contains files downloaded from SophiaDDM
datahub_location=test #/MPS Data Hub
year=2017
library_prep=test #tst15, hcs, csc47, etc

#Find out sample names in the source destination, include a manual check where
#you have f.ex. to typ manually "yes" to ensure that the correct files are
#transferred to the datahub

#Check that files in the source_folder have all the same generic name
#i.e. GLIMS_sophia.bam, GLIMS_full_variant_table_sophia.vcf, etc
#If not, stop the script and manually change the names of the files

python find_glims.py


#Create folders for each sample in the datahub_location

python create_sample_folders.py

#If the previous QC steps have been passed, copy files from source to destination

#cp

#Automatically fill '_workflow.txt'

python fill_workflow.py

#Convert the QA-report.pdf to txt file and collect data such as number of reads etc

#pdftotext

python ngs_statistics_collector.py
