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
- input 0 if empty, 1 if not empty:
    "has garden", "has terrace"
- input 0 if empty, leave current value if not empty
   "garden surface" 
- new column :garden
    parking columns (either has value, say one, if not 0)
- dropping empty rows
    price and living surface

- normalize upper locality column
    
- drop dubble (and X) epc score (12 rows)
- drop the unnamed column



