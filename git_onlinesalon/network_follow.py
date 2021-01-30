# coding: utf-8
# 実行方法: python3 network.py < list.csv
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys

edge_list = []
for line in sys.stdin:
  data_list = line.replace("\n", "").replace('"', '').split(",")
  edge_list.append( (data_list[0], data_list[1]) ) 

G = nx.Graph()
# 辺の追加
for edge_pair in edge_list:
  G.add_edge( edge_pair[0], edge_pair[1] )
print("頂点数:", G.number_of_nodes()) # 頂点数の表示
print("辺数:", G.number_of_edges()) # 辺数の表示
print("連結性", nx.is_connected(G)) # 連結性の確認

# 最大連結成分を調べる
print("### 以下，最大連結成分で計算 ###")
max_size = 0
connected_components_number_of_nodes = []
for c in list(nx.connected_components(G)):
  connected_components_number_of_nodes.append(nx.number_of_nodes(G.subgraph(c)))
  if nx.number_of_nodes(G.subgraph(c)) > max_size:
    SG = G.subgraph(c)
    max_size = nx.number_of_nodes(SG)
print("連結成分の頂点数:", connected_components_number_of_nodes)
print("最大連結成分の頂点数:", SG.number_of_nodes()) # 頂点数の表示
print("最大連結成分の辺数:", SG.number_of_edges()) # 辺数の表示
print("最大連結成分の平均次数:", np.average(list(dict(nx.degree(G)).values()))) # 平均次数の表示
print("最大連結成分の平均クラスタ係数:", nx.average_clustering(G)) # 平均クラスタ係数の表示
print("最大連結成分の平均頂点間距離:", nx.average_shortest_path_length(SG)) # 平均頂点間距離の表示
print("最大連結成分の連結性:", nx.is_connected(SG)) # 連結性の確認
nx.draw(SG, node_size=5) # ネットワークを描画
plt.savefig("network-visualization.png")
plt.clf()

