#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  biogrid_idenficadores.py
#  
#  Copyright 2016 ana <ana@rubia>
#  


import re

def main():
	arqIn = open("../../Samples/BioGrid/Input/BioGrid.txt", 'r')
	arqOut = open('../../Samples/BioGrid/Output/BioGrid.txt', 'a')
	arqOut.write('id_biogrid_A\tInteractor_A\tid_biogrid_B\tInteractor_B\n')
	
	#---------------------------------------------------------------
	linhas = []
	linha = arqIn.readline()
	while linha != '':
		linhas.append(linha)
		linha = arqIn.readline()
	
	arqIn.close()
	#--------------------------------------------------------------
	tam = len(linhas)
	geneA = []
	geneB = []
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
			arqOut.write(str(idA.group())+'\t'+geneA.group(2)+'\t'+str(idB.group())+'\t'+geneB.group(2)+'\n')
	
	arqOut.close()

	return 0
if __name__ == '__main__':
	main()
