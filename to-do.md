# What is the Dog group going to do

## Step 1: Data cleaning

- implement read_csv method
- count nr of missing values for living_area --> check with the group what to do
- split "type" into different columns: "type" for the main type (house or apartment) and "subtype" for the extra info 
- fill empty values in "garage" with 0s
- change "garden" column to 1 (for True) and 0 (False)
- EPC decide what's a minimum realistic nr and replace values below that with None
- Renovation: fill missing data with False. Turn all values into 0/1 