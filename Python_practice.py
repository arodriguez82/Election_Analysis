counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver' :
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

counties_dict = {"Arapahoe": 422829, "Denver":463323, "Jefferson": 432438}

for county in counties_dict:
    print(county)