#!/usr/bin/env python
#
#       smallworld.py
#       
#       Copyright 2009 christopher chow <chow@mail.usf.edu>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import networkx as nx
import random as rand
#import matplotlib.pyplot as plt



def kleinberg_grid(n, p=1, q=0, r=0,seed=1):
	"""
	Returns a square 2d DiGraph of size n*n
	
	Parameters as folows:
	- n : size of the grid with sides n*n
	- p : number of local contacts each node will have
	- q : number of long range contacts created for each node
	- r : clustering factor
	- seed : seed value for the random method
	
	"""
	
	#starts with a undirected graph
	G = nx.empty_graph()
	G.name="kleinberg_grid n=%s p=%s q=%s r=%s seed=%s"%(n,p,q,r,seed)
	
	#make all the nodes
	G.add_nodes_from( (i,j) for i in xrange(n) for j in xrange(n) )
	
	#add local edges
	for (i,j) in G.nodes():
		for k in xrange(i-p,i+p+1):
			for l in xrange(j-p, j+p+1):
				#seach within a square of size p to find lattice dist<p
				if (k >= 0 and k < n and l >= 0 and l < n):
					if( ( abs(i-k)+abs(j-l) )<=p):
						if (i,j) != (k,l):
							G.add_edge( (i,j), (k,l) )
							
	#add long distance links (oh directed!)
	G=G.to_directed()
	#also for each node, q is how many extra links per node
	#r is the distribution
	
	if q > 0:
		#start adding long range only if nessisarry
		rand.seed(seed)
		for (i,j) in G.nodes():
			#for each node in G run this q times
			for x in xrange(q):
				(k,l)=(i,j)
				#set temp node eq to start loop
				while ( (k,l)==(i,j) ):
					#select a (k,l) node thats not a selfloop
					(k,l) = rand.choice(G.nodes())
					#possible inf loop here if only one node	
				#add the edge (its directed, i,j -> k,l)
				G.add_edge( (i,j), (k,l) )
						
	return G

def kb_trav(G, u, v):
	#take DiGraph G, nodes u,v - traverse edges and count number
	#of edges to v, calc distance of each in adjacency list
	#pick smallest dist value
	#is found, when dist is 0
	#use.neighbors(node) to search best route
	count = 0
	
	return count
	
def dist(i,j,k,l):
	return (abs(i-k)+abs(j-l))
	
#other functions to write
#average degree of all nodes
#traverse n pairs and return list, or stats, hi lo, avg
#need to parameratize r for the script, and to verify data
	
if __name__ == '__main__': 
	import sys
	kleinberg_grid(int(sys.argv[1]), sys.argv[1] )


