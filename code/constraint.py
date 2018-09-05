# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac=cars[cars["cars_per_cap"]>500]



# Print car_maniac
print(car_maniac)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)




#2.if you have two or more constraint to get the elements..


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
medium=cars[np.logical_and(cars["cars_per_cap"]>100,cars["cars_per_cap"]<500)]



# Print medium
print(medium)