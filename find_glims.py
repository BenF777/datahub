#!usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import re
import os

directory = "/mnt/files-bioseq/bioseq-temporary/ben/Transfer_Sophia_DDM"

def get_basename(name, extensions, cut_paired=False):
     """
     Extensions: ['.fastq', '.fastq.gz']
     Cuts of extensions provided and full path,
     If cut_paired, it looks to detect paired signs and cuts those off
     """

     if name is None:
          return None
     else:
          name = os.path.basename(name)
          for ext in extensions:
                name = re.sub("%s$" % ext, '', name)
          if cut_paired is True:
                name = re.sub("_L001_R._001$", '', name)
                name = re.sub("_1$|_2$", '', name)
                name = re.sub("_S.*", '', name)
          return name

name_collector = []

fastq_file_list = [f for f in glob.iglob(directory+"/*.fastq.gz")]

for file in fastq_file_list:
    name = get_basename(file, ['.fastq', '.fastq.gz'], cut_paired=True)
    if name in name_collector:
        continue
    else:
        name_collector.append(name)

answer = input("Are these the correct sample names? \n %s \n" % name_collector)

if answer != "yes":
    raise ValueError("Incorrect sample names")

for name in name_collector:

    bam = [f for f in glob.iglob(directory+"/"+name+"_sophia.bam")]
    bai = [f for f in glob.iglob(directory+"/"+name+"_sophia.bam.bai")]
    vcf = [f for f in glob.iglob(directory+"/"+name+"_full_variant_table_sophia.vcf")]
    txt = [f for f in glob.iglob(directory+"/"+name+"_full_variant_table_sophia.txt")]

    if bam == []:
        raise ValueError("Incorrect BAM file name")
    if bai == []:
        raise ValueError("Incorrect BAM index file name")
    if vcf == []:
        raise ValueError("Incorrect VCF file name")
    if txt == []:
        raise ValueError("Incorrect TXT file name")
