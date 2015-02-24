from unicodedata import lookup, name
def make_person():
	name = input('Name: ')
	age = int(input('Age: '))

	g = ''
	while g!='f' and g!='m':
		print('To denote gender, please type f for female or m for male')
		g = input('Gender: ').lower()

	if age in range(5):
		icon = lookup('baby')
	elif age in range(5, 16):
		if g=='f':
			icon = lookup('girl')
		else:
			icon = lookup('boy')
	elif age in range(16, 60):
		if g=='f':
			icon = lookup('woman')
		else:
			icon = lookup('man')
	else:
		if g=='f':
			icon = lookup('older woman')
		else:
			icon = lookup('older man')

	return {'name': name, 'age': age, 'gender': g.upper(), 'icon': icon}
def get_name(person):
	return person['name']
def get_age(person):
	return person['age']
def get_gender(person):
	return person['gender']
def get_icon(person):
	return person['icon']

def person_string(person):
	person_string = get_icon(person) + '\nName: ' + get_name(person) + '\nAge: ' + repr(get_age(person)) + '\nGender: ' + get_gender(person)
	print(person_string)

print('********************************************************')
print('')
print('')
print('Welcome to the your own personal city!')
print('')
q = input('Enter "exit" to exit the program, otherwise enter anything to begin making your citizens: ')
people = {}

print('')

if q!='exit':
	print('')
	print('Let\'s make a new person! \n')
	new_person = make_person()
	people[get_name(new_person).lower()] = new_person
	print(get_name(new_person), 'has been added to your city!')
	print('')

while q!='exit':
	menu_string = '\nEnter "l" to see a list of all citizens. \nEnter "c" to learn more about particular citizens.' 
	menu_string = menu_string + '\nEnter "exit" to exit the program. \nOtherwise enter anything else to make another citizen:\n '
	q = input(menu_string)
	print('')
	if q.lower()=='l':
		for citizen in people:
			print(get_name(people[citizen]))
	elif q.lower()=='c':
		citizen_name = input('Which citizen would you like to learn more about? Enter name here: ').lower()
		print('')
		if not citizen_name in people:
			print('This citizen does not exist')
		else:
			citizen = people[citizen_name]
			person_string(citizen)
	elif q.lower()!='exit':
		print('Let\'s make a new person! \n')
		new_person = make_person()
		people[get_name(new_person).lower()] = new_person
		print(get_name(new_person), 'has been added to your city!')
		print('')





