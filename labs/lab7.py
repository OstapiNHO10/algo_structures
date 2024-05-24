
def create_shift_table(needle):
   needle_set = set()
   shift_table = {}

   for i in range(len(needle) - 2, -1, -1):
       if needle[i] not in needle_set:
           shift_table[needle[i]] = len(needle) - i - 1
           needle_set.add(needle[i])

   if needle[len(needle) - 1] not in needle_set:
       shift_table[needle[len(needle) - 1]] = len(needle)

   shift_table['*'] = len(needle)

   return shift_table

def boyer_moore(needle, haystack, shift_table):
   if len(haystack) < len(needle):
       return "Nothing found"

   i = len(needle) - 1

   while i < len(haystack):
       k = 0
       for j in range(len(needle) - 1, -1, -1):
           if haystack[i - k] != needle[j]:
               if j == len(needle) - 1:
                   off = shift_table[haystack[i]] if shift_table.get(haystack[i], False) else shift_table['*']
               else:
                   off = shift_table[needle[j]]

               i += off
               break
      
           k += 1

       if j == 0:
           return f"needle is found at index {i - k + 1}"
   return "Nothing found"

def find_needle_in_haystack(needle, haystack):
   shift_table = create_shift_table(needle)
   result = boyer_moore(needle, haystack, shift_table)
   return result

if __name__ == "__main__":
   needle = "дані"
   haystack = "метеодані"
   result = find_needle_in_haystack(needle, haystack)
   print(result)
