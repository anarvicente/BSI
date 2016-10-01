#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ids_biogrid.py
#  
#  Copyright 2016 ana <ana@rubia>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import re

def main():
	arqIn = open("BIOGRID-ALL.txt", 'r')
	arqOut = open('OUTRO.txt', 'a')
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
