
#The name of the baby ('GERALDINE') is the fourth entry of this list. Your job in this exercise is to loop over this
# list of lists and append the names of each baby to a new list called baby_names.

records = [['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Aarya', '10', '40'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Abby', '27', '23'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Abigail', '31', '19'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Aisha', '18', '32'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Aiza', '19', '31'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Aleena', '17', '33'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Alexandra', '11', '39'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Alice', '24', '26'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Alicia', '12', '38'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Alina', '41', '10'],
 ['2014', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Alisa', '11', '39']]

# Create the empty list: baby_names
baby_names = []

# Loop over records
for row in records:
    # Add the name to the list
    baby_names.append(row[3])

# Sort the names in alphabetical order
sorted_names = sorted(baby_names)
for name in sorted_names:
    # Print each name
    print(name)