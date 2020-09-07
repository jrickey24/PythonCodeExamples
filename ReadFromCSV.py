import csv

with open('WGUPSPackageFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # for row in readCSV:  # This will read & print the entire csv contents
    # print(row)

    packages = []
    address_streets = []
    address_cities = []
    address_states = []
    address_zips = []
    expected_delivery_times = []
    package_weight_kgs = []
    special_notes = []

    for row in readCSV:  # This will parse out the data attributes from each record & populate the respective lists
        package = row[0]
        address_street = row[1]
        address_city = row[2]
        address_state = row[3]
        address_zip = row[4]
        expected_delivery_time = row[5]
        package_weight_kg = row[6]
        special_note = row[7]

        packages.append(package)
        address_streets.append(address_street)
        address_cities.append(address_city)
        address_states.append(address_state)
        address_zips.append(address_zip)
        expected_delivery_times.append(expected_delivery_time)
        package_weight_kgs.append(package_weight_kg)
        special_notes.append(special_note)

print(packages)
print(address_streets)
print(address_cities)
print(address_states)
print(address_zips)
print(expected_delivery_times)
print(package_weight_kgs)
print(special_notes)
