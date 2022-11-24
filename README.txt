InterNLR v1.0 
Created by Luís Miguel Gonçalves

Description
-----------

InterNLR is a tool to rapidly identify NLR and NLR-like proteins from a protein file based on the presence and order of specific domains.



Requirements
------------

Python3

Interproscan 5.51-85.0



Installation
------------

1. Copy the content to a desired directory

2. Add the following lines to the end of .bashrc: 

export IPS_PATH=/path/to/interproscan-5.51-85.0/
export INTERNLR_PATH=/path/to/internlr/
export PATH=$PATH:/path/to/internlr/

3. Restart the Linux session



Usage
-----

internlr /path/to/input/protein.fasta /path/to/output/directory