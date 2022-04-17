# 자료형 - Dictionary 형과 List형의 조합

people = [{'name':'bob','age':20},{'name':'carry','age':38}]

# people[0]['name']의 값은? 'bob'
print("people[0]['name']:", people[0]['name'])
# people[1]['name']의 값은? 'carry'
print("people[1]['name']:", people[1]['name'])

person = {'name':'john','age':7}
people.append(person)

# people의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
print("people:", people)
# people[2]['name']의 값은? 'john'
print("people[2]['name']:", people[2]['name'])