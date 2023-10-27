#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Salom"""

import os
from tqdm import tqdm

main_dir = '/media/juliarymuza/30802472802440A8/'
files = [file for file in os.listdir(main_dir + 'rna_seq/raw/')]
files = [i.strip('.fastq.gz') for i in files]
files = list(set([i[:-2] for i in files]))
files.sort()
ana_dir = main_dir + 'rna_seq'
#  # files maja dlugosc 49 bo jedna probka jest powtorzona

def run_main(files, ana_dir):
    for file in tqdm(files):
        if '96s_merged' in file:
            samp = '96s'
        elif '96s' in file:
            continue
        else:
            samp = file.split('_')[1:-3]
            samp =  '_'.join(samp)
        
        print(file, samp)
        os.system('salmon quant -l A -i {ref}/index/ \
                      -1 {folder}/raw/{file}_1.fastq.gz \
                      -2 {folder}/raw/{file}_2.fastq.gz \
                      --seqBias --gcBias --validateMappings --rangeFactorizationBins 4 -p 4 \
                      -o {folder}/salmon/{samp}_quant'.format(ref=main_dir + 'S2996/S2996_1/reference',
                      folder=ana_dir, samp=samp, file=file))
def make_index(folder):
    os.system(f'salmon index -t {folder}/gencode.v39lift37.transcripts.fa.gz --gencode -i {folder}/index')
    # dodanie --gencode upraszcza header z transcripts.fa


# make_index(main_dir + 'S2996/S2996_1/reference')
files = ['NG-27772_86s_lib492696_7584_3']
print(files, len(files))
run_main(files, ana_dir)
