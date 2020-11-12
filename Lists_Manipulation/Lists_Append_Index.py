# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
ext = ['Rowen','Sandeep']
baby_names.extend(ext)

# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index('Aliza')

# Remove 'Aliza' from baby_names
pop_name = baby_names.pop(position)

# Print baby_names
print(baby_names)