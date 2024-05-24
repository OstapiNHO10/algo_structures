def read_input(file_path):
   with open(file_path, 'r') as file:
       L = int(file.readline().strip())
       levels = []
       for _ in range(L):
           levels.append(list(map(int, file.readline().strip().split())))
       return L, levels

def write_output(file_path, result):
   with open(file_path, 'w') as file:
       file.write(str(result) + '\n')

def max_experience(L, levels):
   for i in range(L-2, -1, -1):
       for j in range(len(levels[i])):
           levels[i][j] += max(levels[i+1][j], levels[i+1][j+1])
   return levels[0][0]

if __name__ == "__main__":
   L, levels = read_input('career.in')
   result = max_experience(L, levels)
   write_output('career.out', result)
