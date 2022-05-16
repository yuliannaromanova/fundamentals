

x = [ [5,2,3], [10,8,9] ] 
x = [1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']='Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(0, len(students)):
        print("first_name - {}, last_name - {}".format(students[i]['first_name'], students[i]['last_name']))
iterateDictionary(students)

def iterateDictionary2(key_names, someList):
    for i in range(0, len(someList)):
        print(someList[i][key_names])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for i in range(0, len(some_dict)):
        print( some_dict [i])

printInfo(dojo['locations'])
printInfo(dojo['instructors'])

