#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  biogrid_network.py
#  
#  Copyright 2016 ana <ana@rubia>

import networkx as nx
import matplotlib.pyplot as plt
import pylab

def main():
	G=nx.Graph()
	arq = open('../../Samples/BioGrid/Output/BioGrid.txt', 'r')
	#------------------------------------------------------------------
	linha = arq.readline()
	while linha != '':
		sep = linha.split('\t')
		G.add_edge(sep[1],sep[3][:-1])
		linha = arq.readline()
	#-------------------------------------------------------------------
	arq.close()
	
	pylab.figure(2,figsize=(15,15))
	nx.draw_random(G,node_size = 600, with_labels = True, font_size = 8)
	#------------------------------------------------------------------
	plt.show()
	
	return 0
if __name__ == '__main__':
	main()
