import pandas as pd
pd.date_range('2020-12-01','2020-12-31')

# importing pandas as pd 
import pandas as pd 
  
# Create the Timestamp object 
ts = pd.Timestamp(year = 2021,  month = 11, day = 6,  
                  hour = 7, second = 30, tz = 'US/Central')  
  
# Print the Timestamp object 
print(ts) 