course = {
    'php':{'duration':'1 years','fees':1000},
    'python':{'duration':'2 years','fees':2000},
    'Java':{'duration':'3 years','fees':3000},
}
print(course['php']['duration'])
print(course.get('python').get('duration'))

print(course)

del course['php']['duration']
print(course)

