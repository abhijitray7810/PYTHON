student={
    "name":"abhijit",
    "subject":{
        "physics":80,
        "math":90,
        "chemistry":70
        
    }
}
#nested_dictionary
print(student["subject"]["math"])
#akai nested dictionary er value print korar jonno amra akta key er moddhe onno akta key use korte pari 
print(len(list(student.keys())))#2
print(student.values())
print(list(student.values()))
print(type(student.values()))
print(student.items())
print(type(student.items()))
print(list(student.items()))    
student.update({"city":"delhi"})
print(student)