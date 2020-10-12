buildings = {
    "Burj Khalifa": "United Arab Emirates",
    "Central Park Tower": "United States",
    "Willis Tower": "United States",
    "Marina 101": "United Arab Emirates",
    "Princess Tower": "United Arab Emirates",
    "Al Hamra Tower": "Kuwait",
}

country_buildings1 = {}
country_buildings2 = {}

for building, country in buildings.items():

    if country not in country_buildings1:
        country_buildings1[country] = [building]
    else:
        country_buildings1[country].append(building)

    if country not in country_buildings2:
        country_buildings2[country] = {building}
    else:
        country_buildings2[country].add(building)

print()
print("List into Dictionary:")
print(country_buildings1)

print()
print("Tuple into Dictionary:")
for country, building in country_buildings1.items():
    country_buildings1[country] = tuple(building)
print(country_buildings1)

print()
print("Set into dictionary:")
print(country_buildings2)
