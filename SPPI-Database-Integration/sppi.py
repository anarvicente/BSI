#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ids_biogrid.py
#  
#  Copyright 2016 ana <ana@rubia>


import re
import sys
def write_mint(filename):
	arqIn = open(filename,'r')
	arqOut = open('Output/all.sif','a')
	#---------------------------------------------------------------
	linhas = []
	linha = arqIn.readline()
	while linha != '':
		linhas.append(linha)
		linha = arqIn.readline()
	
	arqIn.close()
	#---------------------------------------------------------------
	tam = len(linhas) 
	taxid = "taxid:9606(human)|taxid:9606(Homo sapiens)"
	#---------------------------------------------------------------

	for i in range(1,tam):
		sep = linhas[i].split('\t')
		cond1 = (sep[9] == taxid and sep[10] == taxid)
		
		geneA = re.search('(uniprotkb:)([A-Za-z0-9_-]+)(\(gene name\))', sep[4])
		
		geneB = re.search('(uniprotkb:)([A-Za-z0-9_-]+)(\(gene name\))', sep[5])
		
		cond2 = (geneA is not None and geneB is not None)	
		
		if cond1 and cond2:
			arqOut.write(geneA.group(2)+'\t'+'pp'+'\t'+geneB.group(2)+'\n')

	arqOut.close()
    
def write_hprd(filename):
	arqIn = open(filename,'r')
	arqOut = open('Output/all.sif','a')
	#---------------------------------------------------------------
	linhas = []
	linha = arqIn.readline()
	while linha != '':
		linhas.append(linha)
		linha = arqIn.readline()
	
	arqIn.close()
	#---------------------------------------------------------------
	tam = len(linhas) 
	#---------------------------------------------------------------
	for i in range(tam):
		sep = linhas[i].split('\t')
		
		arqOut.write(sep[0]+'\t'+'pp'+'\t'+sep[3]+'\n')

	arqOut.close()
	
def write_intact(filename):
	arqIn = open(filename,'r')
	arqOut = open('Output/all.sif','a')
	#---------------------------------------------------------------
	linhas = []
	linha = arqIn.readline()
	while linha != '':
		linhas.append(linha)
		linha = arqIn.readline()
	
	arqIn.close()
	#---------------------------------------------------------------
	tam = len(linhas) 
	taxid = 'taxid:9606(human)|taxid:9606(Homo sapiens)'
	#---------------------------------------------------------------

	for i in range(1,tam):
		sep = linhas[i].split('\t')
		cond1 = (sep[9] == taxid and sep[10] == taxid)
		
		geneA = re.search('(uniprotkb:)([A-Za-z0-9_-]+)(\(gene name\))', sep[4])
		
		geneB = re.search('(uniprotkb:)([A-Za-z0-9_-]+)(\(gene name\))', sep[5])
		
		cond2 = (geneA is not None and geneB is not None)	
		
		if cond1 and cond2:
			arqOut.write(geneA.group(2)+'\t'+'pp'+'\t'+geneB.group(2)+'\n')

	arqOut.close()
        
def write_biogrid(filename):
	arqIn = open(filename,'r')
	arqOut = open('Output/all.sif','a')
	#---------------------------------------------------------------
	linhas = []
	linha = arqIn.readline()
	while linha != '':
		linhas.append(linha)
		linha = arqIn.readline()
	
	arqIn.close()
	#--------------------------------------------------------------
	tam = len(linhas)
	taxid = 'taxid:9606'
	#--------------------------------------------------------------
	for i in range(1,tam):
		sep = linhas[i].split('\t')
		cond1 = (sep[9] == taxid and sep[10] == taxid)
		
		geneA = re.search('(locuslink:)([A-Z0-9]+)|(locuslink:)([A-Z0-9])+\|', sep[2])
		idA = re.search('\d{6,}', sep[2])
		
		geneB = re.search('(locuslink:)([A-Z0-9]+)|(locuslink:)([A-Z0-9])+\|', sep[3])
		idB = re.search('\d{6,}', sep[3])
		
		cond2 = (geneA is not None and geneB is not None)
		if cond1 and cond2:
			arqOut.write(geneA.group(2)+'\t'+'pp'+'\t'+geneB.group(2)+'\n')
	
	arqOut.close()

def main():	
	tam = len(sys.argv)
	for i in range(1,tam):
		if sys.argv[i] == '1':
			write_biogrid("Samples/sample_biogrid.txt")	
		if sys.argv[i] == '2':
			write_intact("Samples/sample_intact.txt")
		if sys.argv[i] == '3':
			write_hprd("Samples/sample_hprd.txt")
		if sys.argv[i] == '4':
			write_mint("Samples/sample_mint.txt")
	
	
	#~ write_biogrid("Samples/sample_biogrid.txt")	
	#write_intact("Samples/sample_intact.txt")
	#~ write_hprd("Samples/sample_hprd.txt")
	#~ write_mint("Samples/sample_mint.txt")
	

	return 0
if __name__ == '__main__':
	main()
