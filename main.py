from dataviz import DataAnalysis 

def main():
    dataviz = DataAnalysis()
    df = dataviz.read_csv("./immoweb-dataset.csv")
    droppped_columns = dataviz.drop_column(df)
    print(droppped_columns.info())

if __name__ == "__main__":
    main()
