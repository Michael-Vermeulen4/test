# This script will be for indexing and downloading indexes for reference genomes to use for alignment
# in HISTAT2

import sys
import os
import urllib.request
import tarfile
import subprocess

inputs = sys.argv
ref = inputs[1]
dirpath = os.getcwd()

def extract_tar_gz(file):
    if (file.endswith("tar.gz")):
        tar = tarfile.open(file)
        tar.extractall()
        tar.close()
    elif (file.endswith("tar")):
        tar = tarfile.open(file, "r:")
        tar.extractall()
        tar.close()

#def chunk_report(bytes_so_far, chunk_size, total_size):
#   percent = float(bytes_so_far) / total_size
#   percent = round(percent*100, 2)
#   sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" %
#       (bytes_so_far, total_size, percent))
#
#   if bytes_so_far >= total_size:
#      sys.stdout.write('\n')
#
#def chunk_read(response, chunk_size=8192, report_hook=None):
#   total_size = response.info().getheader('Content-Length').strip()
#   total_size = int(total_size)
#   bytes_so_far = 0
#
#   while 1:
#      chunk = response.read(chunk_size)
#      bytes_so_far += len(chunk)
#
#      if not chunk:
#         break
#
#      if report_hook:
#         report_hook(bytes_so_far, chunk_size, total_size)
#
#   return bytes_so_far
#
#
#if len(inputs) < 2:
#    print("""Choose reference genome:
#    human:
#    GRCh38
#    GRCh37
#    hg19
#
#    mouse:
#    mm10
#    GRCm38
#
#    usage: download_index [reference_genome]
#    """)
#    exit()

down=""
if inputs[1]:
    #add the urls into a dictionary to make this piece of code cleaner
    if ref.lower()=="grch38":
        url="ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/data/grch38.tar.gz"
        #url="ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/data/r64.tar.gz"
        filename="./GRCh38.tar.gz"
        print("DOWNLOADING %s" % filename)
        response = urllib.request.urlretrieve(url, filename)
        print("complete")
        down="GRCh38.tar.gz"

    if ref.lower()=="grch37":
        url = "ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/data/grch37.tar.gz"
        filename="./GRCh37.tar.gz"
        response = urllib.request.urlretrieve(url, filename)
        down = "GRCh37.tar.gz"

    if ref.lower()=="hg19":
        url = "ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/data/hg19.tar.gz"
        filename="./hg19.tar.gz"
        response = urllib.request.urlretrieve(url,filename)
        down = "hg19.tar.gz"

    if ref.lower()=="mm10":
        url = "ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/data/mm10.tar.gz"
        filename="./mm10.tar.gz"
        response = urllib.request.urlretrieve(url,filename)
        down = "mm10.tar.gz"

    if ref.lower()=="grcm38":
        url = "ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/data/grcm38.tar.gz"
        filename="./grcm38.tar.gz"
        response = urllib.request.urlretrieve(url,filename)
        down = "grcm38.tar.gz"
 #    else:
 #       print("""You genome isn't available. Check https://ccb.jhu.edu/software/hisat2/index.shtml
 #       or use the hisat2-build script to index your genome.
 #       I'll automate this process in the future, having problems with the hisat-build script right now
 #       """)
 #       exit()
# ideally in here add a function that asks the user if they want to index the file they've listed
# run hisat2-build on the reference and align using that.


extract_tar_gz(filename)

#subprocess.call(["hisat2"], shell=True)
#-q input file fastq
#--summary-file
#-f input file fasta
#-S output SAM file (at end of comment)
#hisat2 [options]* -x <hisat2-idx> -U <r> | --sra-acc <SRA accession number>} [-S <hit>]
#hisat2 --summary-file -q -x index_name -U input_files (comma_sep) | -S SAM_output_file
#



