from dataviz import DataAnalysis 

def main():
    dataviz = DataAnalysis()
    df = dataviz.read_csv("./immoweb-dataset.csv")
    df = dataviz.drop_column(df)
    print(df.info())
    
    df = dataviz.convert_has_garden(df)
    print(df.info())

    df = dataviz.convert_garden_surface (df)
    print(df.info())

    df = dataviz.convert_has_terrace (df)
    print(df.info())

        
if __name__ == "__main__":
    main()

