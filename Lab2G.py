#Lab2G
planet_string = "Mercury|Venus|Earth|Mars|Jupiter|Saturn|Uranus|Neptune"
planet_string2 = planet_string.split('|')
planet_list = list(planet_string2)

def log_planets():
    print "Here is a list of the planets:"
    for planet in planet_list:
        print planet
    print "----------------"
log_planets()

print 'Adding "The Sun" to the beginning of the planets list.'
planet_list.insert(0, 'The Sun')
log_planets()

print 'Adding "Pluto" to the end of the planets list.'
planet_list.append('Pluto')
log_planets()

print 'Removing "The Sun" from the beginning of the planets list.'
planet_list.remove('The Sun')
log_planets()

print 'Removing "Pluto" from the end of the planets list.'
planet_list.remove ('Pluto')
log_planets()

print 'Finding and logging the index of "Earth" in the planets list.'
print planet_list.index('Earth')
log_planets()

print 'Removing the planet after "Earth".'
del planet_list[3]
log_planets()

print 'Adding back in the planet removed after "Earth".'
planet_list.insert(3, 'Mars')
log_planets()

print 'Reversing the order of the planets list.'
planet_list.reverse()
log_planets()

print 'Sorting the planets list'
planet_list.sort()
log_planets()