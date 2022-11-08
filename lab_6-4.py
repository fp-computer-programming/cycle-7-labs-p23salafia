#JS Lab 6-4 11/8/2022
#Make a list and add a subject
subjects = ['Economics', 'Orchestra', 'Programming']
subjects.append('Calculus')
print(subjects)

#Return the index of one of the subjects
index = subjects.index('Programming')
print(index)

#Sort list
subjects.sort(key=str.lower, reverse=False)
print(subjects)

#Make a clone of the list
subjects_2= subjects

#Sort
subjects_2.sort(key=str.lower, reverse=True)
print(subjects_2)