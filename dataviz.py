import pandas as pd

class DataAnalysis:

    def read_csv(self):
        # read the csv file with pandas

        base_file = pd.read_csv('./properties06191148_modified.csv')
        print(base_file.head())

        