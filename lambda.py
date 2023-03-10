people = [ 
    {"name": "Atiwit", "Job":"Engineer"},
    {"name": "Nuntakorn", "Job":"Audit"},
    {"name": "Panitchaya", "Job":"Teacher"}
]

people.sort(key= lambda person: person["Job"])

print(people)