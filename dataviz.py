import pandas as pd


class DataAnalysis:
    COL_TO_DROP = [
        "bathroomCount",
        "roomCount",
        "monthlyCost",
        "hasAttic",
        "hasBasement",
        "hasDressingRoom",
        "diningRoomSurface",
        "hasDiningRoom",
        "buildingConstructionYear",
        "facedeCount",
        "floorCount",
        "streetFacadeWidth",
        "hasLift",
        "floodZoneType",
        "heatingType",
        "hasHeatPump",
        "hasPhotovoltaicPanels",
        "hasThermicPanels",
        "kitchenSurface",
        "kitchenType",
        "landSurface",
        "hasLivingRoom",
        "livingRoomSurface",
        "hasBalcony",
        "gardenOrientation",
        "hasAirConditioning",
        "hasArmoredDoor",
        "hasVisiophone",
        "hasOffice",
        "toiletCount",
        "hasSwimmingPool",
        "hasFireplace",
        "terraceSurface",
        "terraceOrientation",
        "accessibleDisabledPeople",
    ]

    def read_csv(self, path):
        # read the csv file with pandas
        df = pd.read_csv(path)
        print(df.info())
        return df
