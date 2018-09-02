# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars  ,including index_col.
cars=pd.read_csv("cars.csv")

# Print out cars
print(cars)


# Import pandas as pd
import pandas as pd

# Fix import by including index_col ,excluding index_col;
cars = pd.read_csv('cars.csv',index_col=0)

# Print out cars
print(cars)


# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])


# Print out DataFrame with country and drives_right columns
print(cars[["country","drives_right"]])