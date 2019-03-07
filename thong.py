# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:41:34 2018

@author: rbj
"""

#!/usr/bin/env python
import gzip
from Bio import SeqIO
import itertools
import sys
import os
from tkinter import filedialog
# Copyright(C) 2011 Iddo Friedberg
# Released under Biopython license. http://www.biopython.org/DIST/LICENSE
# Do not remove this comment
def merge_fastq(fastq_path1, fastq_path2, outpath):
    outfile = open(outpath,"w")
    fastq_iter1 = SeqIO.parse(open(fastq_path1),"fastq")
    fastq_iter2 = SeqIO.parse(open(fastq_path2),"fastq")
    print("loaded now writing")
    for rec1, rec2 in zip(fastq_iter1, fastq_iter2):
        SeqIO.write([rec1,rec2], outfile, "fastq")
    print("now closing") 
    outfile.close()

if __name__ == '__main__':
    os.chdir('I:\OmarStuff')
    root = filedialog.Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",  
        multiple=1,title = "Select TWO files ONLY",filetypes = (("fastq file","*.fastq"),("all files","*.*")))
    filelist=root.tk.splitlist(root.filename)
    flist=list(filelist)
    i=0
    for file in flist:
        i+=1
        if i==1:
            file1open=file
        elif i==2:
            file2open=file
        else:
            print( "ERROR! a third file!!?")
    print (file1open,file2open)
    
    root.withdraw()
    outpath =file1open.replace('.fastq','combined.fastq')
    merge_fastq(file1open,file2open,outpath)
    print("complete")