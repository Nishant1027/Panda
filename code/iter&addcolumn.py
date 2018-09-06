#Getting the row and column by iter method

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab,row in cars.iterrows():
    print(lab)
    print(row)


#Getting the row and column by itermethod
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab+": "+str(row["cars_per_cap"]))    


#Adding column in Dataframe
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():
    cars.loc[lab,"COUNTRY"] = row["country"].upper()


# Print cars
print(cars)



#Adding Column in Dataframe by String method
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)    