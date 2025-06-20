# What is the Dog group going to do

## Step 1: Data cleaning

- implement read_csv method
- count nr of missing values for living_area --> check with the group what to do
- split "type" into different columns: "type" for the main type (house or apartment) and "subtype" for the extra info 
- fill empty values in "garage" with 0s
- change "garden" column to 1 (for True) and 0 (False)
- EPC decide what's a minimum realistic nr and replace values below that with None
- Renovation: fill missing data with False. Turn all values into 0/1
- Change Garage where more than 5 spots change to 1, the one with 15 we keep
- Type Project  delete
- Street and number columns delete
- Delete column year built
