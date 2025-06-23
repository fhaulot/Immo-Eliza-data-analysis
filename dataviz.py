import pandas as pd
import numpy as np


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

    # check "hasGarden" column, if "TRUE" change to 1, otherwise make it 0
    def convert_has_garden (self, df):         
        df["hasGarden"]= np.where(df["hasGarden"] == True,1,0)
        return df

    # check "gardenSurface" column, if empty change to 0, leave current value if NOT empty
    def convert_garden_surface (self, df):
        df["gardenSurface"]= df["gardenSurface"].fillna(0)
        return df

    # check "hasTerrace" column, if "TRUE" change to 1 otherwise make it 0
    def convert_has_terrace (self, df):         
        df["hasTerrace"]= np.where(df["hasTerrace"] == True,1,0)
        return df




