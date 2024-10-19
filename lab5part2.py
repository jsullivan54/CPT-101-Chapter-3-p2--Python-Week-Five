#JOHNATHAN SULLIVAN PLANET PROGRAM LAB 5 PART 2
#This program is a menu system for calculating planetary distance from earth/
# to other solar objects

#This program calculates the distance difference between the user-chosen planet below and Earth/
#assuming shortest/orbital distance (both planets in-line)

#This program also calculates the the time required for a laser beam traveling at the speed of light to/
#reach the chosen planet from earth

#Named Constants Below are planets and their respective distance from the sun in miles

#Distance from the sun
OPTION0_EARTH= 	93000000
#Distance from the sun
OPTION1_MERCURY= 35000000
#Distance from the sun
OPTION2_VENUS= 67000000
#Distance from the sun
OPTION3_MARS= 142000000
#Distance from the sun
OPTION4_ASTEROID_BELT= 297000000
#Distance from the sun
OPTION5_JUPITER= 484000000
#Distance from the sun
OPTION6_SATURN=	889000000
#Distance from the sun
OPTION7_URANUS= 1790000000
#Distance from the sun
OPTION8_NEPTUNE= 2880000000
#Distance from the sun
OPTION9_PLUTO_KUIPER_BELT= 3670000000


SPEED_OF_LIGHT= 186000

choice=int(input('Enter the Planet Number:'))

if choice == 1 :
    planet_name = 'Mercury'
    planet_dist = OPTION0_EARTH - OPTION1_MERCURY
    time = planet_dist / SPEED_OF_LIGHT
    print(f'Distance from Earth {OPTION0_EARTH - OPTION1_MERCURY}')
    print(f'Distance for Laser {planet_dist / SPEED_OF_LIGHT:.2f}')
elif choice == 2 :
    planet_name = 'Venus'
    planet_dist = OPTION0_EARTH -OPTION2_VENUS
    time = planet_dist / SPEED_OF_LIGHT
    print(f'Distance from Earth {OPTION0_EARTH - OPTION2_VENUS}')
    print(f'Distance for Laser {planet_dist / SPEED_OF_LIGHT:.2f}')
elif choice == 3 :
    planet_name = 'Mars'
    planet_dist = OPTION3_MARS - OPTION0_EARTH
    time = planet_dist / SPEED_OF_LIGHT
    print(f'Distance from Earth {OPTION3_MARS - OPTION0_EARTH}')
    print(f'Distance for Laser {planet_dist / SPEED_OF_LIGHT:.2f}')
elif choice == 4 :
    planet_name = 'Asteroid Belt'
    planet_dist = OPTION4_ASTEROID_BELT - OPTION0_EARTH
    time = planet_dist / SPEED_OF_LIGHT
    print(f'Distance from Earth {OPTION4_ASTEROID_BELT - OPTION0_EARTH}')
    print(f'Distance for Laser {planet_dist / SPEED_OF_LIGHT:.2f}')
elif choice == 5 :
    planet_name = 'JUPITER'
    planet_dist = OPTION5_JUPITER - OPTION0_EARTH
    time = planet_dist / SPEED_OF_LIGHT
    print(f'Distance from Earth {OPTION5_JUPITER - OPTION0_EARTH}')
    print(f'Distance for Laser {planet_dist / SPEED_OF_LIGHT:.2f}')
elif choice == 6 :
    planet_name = 'Saturn'
    planet_dist = OPTION6_SATURN - OPTION0_EARTH
    time = planet_dist / SPEED_OF_LIGHT
    print(f'Distance from Earth {OPTION6_SATURN - OPTION0_EARTH}')
    print(f'Distance for Laser {planet_dist / SPEED_OF_LIGHT:.2f}')
elif choice == 7 :
    planet_name = 'Uranus'
    planet_dist = OPTION7_URANUS - OPTION0_EARTH
    time = planet_dist / SPEED_OF_LIGHT
    print(f'Distance from Earth {OPTION7_URANUS - OPTION0_EARTH}:')
    print(f'Distance for Laser {planet_dist / SPEED_OF_LIGHT:.2f}')
elif choice == 8 :
    planet_name = 'Neptune'
    planet_dist = OPTION8_NEPTUNE- OPTION0_EARTH
    time = planet_dist / SPEED_OF_LIGHT
    print(f'Distance from Earth {OPTION8_NEPTUNE - OPTION0_EARTH}')
    print(f'Distance for Laser {planet_dist / SPEED_OF_LIGHT:.2f}')
elif choice == 9 :
    planet = 'Pluto/Kuiper Belt'
    planet_dist = OPTION9_PLUTO_KUIPER_BELT - OPTION0_EARTH
    time = planet_dist / SPEED_OF_LIGHT
    print(f'Distance from Earth {OPTION9_PLUTO_KUIPER_BELT - OPTION0_EARTH} miles')
    print(f'Distance for Laser {planet_dist / SPEED_OF_LIGHT:.2f}')


