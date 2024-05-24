import math
from typing import List

def calculate_max_wire_length(w: int, heights: List[int]) -> float:
   max_length = 0.0
   for i in range(len(heights) - 1):
       h1 = heights[i]
       h2 = heights[i + 1]
       max_length += math.sqrt((h1 - h2) ** 2 + w ** 2)
   return round(max_length, 2)

if __name__ == "__main__":
   w = int(input())
   heights = list(map(int, input().split()))
   result = calculate_max_wire_length(w, heights)
   print(result)
