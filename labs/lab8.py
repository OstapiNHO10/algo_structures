import csv
import os

def read_wells_data(file_path):
   edges = []
   with open(file_path, mode='r') as file:
       csv_reader = csv.reader(file)
       for row in csv_reader:
           if row:
               edges.append((row[0], row[1], int(row[2])))
   return edges

class DisjointSet:
   def __init__(self, n):
       self.parent = list(range(n))
       self.rank = [0] * n

   def find(self, u):
       if self.parent[u] != u:
           self.parent[u] = self.find(self.parent[u])
       return self.parent[u]

   def union(self, u, v):
       root_u = self.find(u)
       root_v = self.find(v)
       if root_u != root_v:
           if self.rank[root_u] > self.rank[root_v]:
               self.parent[root_v] = root_u
           elif self.rank[root_u] < self.rank[root_v]:
               self.parent[root_u] = root_v
           else:
               self.parent[root_v] = root_u
               self.rank[root_u] += 1

def kruskal_mst(edges):
   edges = sorted(edges, key=lambda edge: edge[2])
   nodes = set()
   for edge in edges:
       nodes.add(edge[0])
       nodes.add(edge[1])

   node_to_index = {node: index for index, node in enumerate(nodes)}
   ds = DisjointSet(len(nodes))

   mst_weight = 0
   mst_edges = 0

   for edge in edges:
       u, v, weight = edge
       if ds.find(node_to_index[u]) != ds.find(node_to_index[v]):
           ds.union(node_to_index[u], node_to_index[v])
           mst_weight += weight
           mst_edges += 1
           if mst_edges == len(nodes) - 1:
               return mst_weight

   return -1 if mst_edges != len(nodes) - 1 else mst_weight

def minimum_fiber_length(file_path):
   edges = read_wells_data(file_path)
   return kruskal_mst(edges)

if __name__ == "__main__":
   file_path = os.path.join(os.path.dirname(__file__), '..', 'communication_wells.csv')
   result = minimum_fiber_length(file_path)
   print(f"The minimum length of optical fiber needed is: {result}")
