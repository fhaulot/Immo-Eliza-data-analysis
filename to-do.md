# What is the Dog group going to do

## Step 1: Data cleaning

- columns we need to delete : 
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
- input false if empty :
    "has garden", "has terrace", garden surface (0 if empty)
-what to pick :
    id, price, subtype, postaclcode, province, locality
- dropping empty cells
    price, epc score, bedroom count, 
- remove 1 '0' from the bedroom
- new column :
    parking columns (either has value, say one, if not 0)


