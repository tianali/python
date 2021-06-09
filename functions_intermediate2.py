#1. Update values in Dictionaries and Lists 
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15    #1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
print(x)
students[0]['last_name'] = 'Bryant' #2. Change the last_name of the first student from 'Jordan' to 'Bryant'
print(students)
sports_directory['soccer'][0] = 'Andres' #3. In the sports_directory, change 'Messi' to 'Andres'
print(sports_directory)
z[0]['y'] = 30 #4. Change the value 20 in z to 30
print(z)

#2. Iterate Through a List of Dictionaries 
#Create a function iterateDictionary(some_list) that given a list or dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list: 
def iterateDictionary(some_list):
    for i in range(len(some_list)):
        key_list = list(some_list[i].keys())
        print (key_list[0] + " - " + some_list[i]['first_name'] + ", " + key_list[1] + " - " + some_list[i]['last_name'])


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

#3. Get Values From a List of Dictionaries - Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name',students) should output: Michael, John, Mark, KB and iterateDictionary2('last_name',students) should output: Jordan, Rosales, Guillen Tonel
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        if key_name == 'first_name':
            print(some_list[i]['first_name'])
        if key_name == 'last_name':
            print(some_list[i]['last_name'])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4. Iterate Through a Dictionary with List values - Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example: 
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for i in range(len(some_dict)):
        key_list=list(some_dict.keys())
        val_list=list(some_dict.values())
        print (str(len(val_list[i])) + " " + (key_list[i].upper()))
        print (*val_list[i], sep = "\n")
printInfo(dojo)
