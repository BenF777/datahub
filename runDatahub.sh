#!/bin/bash

#Define inputs

source_folder = "" #contains files downloaded from SophiaDDM
datahub_location = "" #/MPS Data Hub
year = "2017"
library_prep = "" #tst15, hcs, csc47, etc

#Create folders for each sample in the datahub_location

#Find out sample names in the source destination, include a manual check where
#you have f.ex. to typ manually "yes" to ensure that the correct files are
#transferred to the datahub

#Check that files in the source_folder have all the same generic name
#i.e. GLIMS_sophia.bam, GLIMS_full_variant_table_sophia.vcf, etc
#If not, stop the script and manually change the names of the files

#If the previous QC steps have been passed, copy files from source to destination

#Automatically fill '_workflow.txt'

#
