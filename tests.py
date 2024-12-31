import datetime 
  
  
dt = datetime.date(2020, 1, 26) 
# prints the date as date 
# object 
print(dt) 
  
# prints the current date 
print(datetime.date.today()) 
  
# prints the date and time 
dt = datetime.datetime(1999, 12, 12, 12, 12, 12, 342380)  
print(dt) 
   
# prints the current date  
# and time 
print(datetime.datetime.now()) 