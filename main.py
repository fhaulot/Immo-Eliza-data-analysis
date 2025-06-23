from dataviz import DataAnalysis 

def main():
    dataviz = DataAnalysis()
    csv = dataviz.read_csv("./immoweb-dataset.csv")
    print(csv)

if __name__ == "__main__":
    main()