#JS Lab 6-3 11/7/2022

#Create the list with 4 colors

colors = ['Blue', 'Pink', 'Red', 'Purple']

#Add 3 extra colors to the list
colors.extend(['Yellow', 'Green', 'Orange'])

#Add 1 new color
colors.append('Black')

#Insert new color with .insert
colors.insert(3,'Brown')
print(colors)


#Clone of list
color_list_2 = colors

#Remove all colors in duplicate list
color_list_2.remove('Blue')

print(color_list_2)