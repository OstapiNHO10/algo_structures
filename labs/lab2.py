def simplify_busy_schedule(schedule):
   schedule.sort(key=lambda x: x[0]) 
   simplified_schedule = []

   for start, end in schedule:
       if not simplified_schedule or start > simplified_schedule[-1][1]:
           simplified_schedule.append([start, end])
       else:
           simplified_schedule[-1][1] = max(simplified_schedule[-1][1], end)
  
   return simplified_schedule