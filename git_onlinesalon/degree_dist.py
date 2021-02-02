#!/usr/bin/env python3
# coding: utf-8
# 実行方法: python3 network_follow.py < list.csv
import networkx as nx # NetworkXのインポート
import numpy as np
import sys
import matplotlib.pyplot as plt

edge_list = []
for line in sys.stdin:
  data_list = line.replace("\n", "").replace('"', '').split(",")
  #print(data_list)
  edge_list.append( (data_list[0], data_list[1]) ) 

G = nx.Graph()
# 辺の追加
for edge_pair in edge_list:
  G.add_edge( edge_pair[0], edge_pair[1] )

# 次数分布の計算
degrees_mod_list = list(nx.degree(G))
degrees_list = []
for item in degrees_mod_list:
  degrees_list.append(item[1])
print("次数:", degrees_list)


# plot histogram
n, bins, patches = plt.hist(degrees_list, bins=50, density=True)
plt.savefig("plot4-0.png")
plt.clf()

# plot histogram curve with normal plot
bins_mod = []
for i in range(len(bins)-1):
  bins_mod.append( (bins[i] + bins[i+1])/2.0 )
# normal plot
plt.plot(bins_mod, n, marker="o", linestyle="-")
#plt.show()
plt.savefig("degree_dist-normal.png")
plt.clf()

# plot with semilogy 
plt.semilogy(bins_mod, n, marker="o", linestyle="-")
#plt.show()
plt.savefig("degree_dist-semilogy.png")
plt.clf()

# plot with loglog 
plt.loglog(bins_mod, n, marker="o", linestyle="-")
#plt.show()
plt.savefig("degree_dist-loglog.png")
plt.clf()

