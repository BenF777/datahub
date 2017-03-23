#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

datahub = "/mnt/genmachines/MPS Data Hub/Samples/2017/"
source = "/home/benflies/Desktop/"

sample_basename = "test"

library_prep_kit = "/tst15/"

directory = datahub+sample_basename+library_prep_kit
print(directory)

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
          return name



os.makedirs(directory)

shutil.copy(source+"test_file", directory)

open(directory+"_workflow.txt", "a").close()

workflow_file = open(directory+"_workflow.txt", "w")

workflow_file.write("analysis:\n")
workflow_file.write("    raw_reads:\n")
workflow_file.write("        - test.fastq.gz\n")
workflow_file.write("    assemblies:\n")
workflow_file.write("    variants:\n")

workflow_file.close()
