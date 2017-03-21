current_population = 312032486
print("Current US population is:", current_population)

birth_rate = 7
death_rate = 13
immigration_rate = 45

for i in range(0, 5):
    birth_population = (365 * 24 * 60 * 60)/birth_rate
    death_population = (365 * 24 * 60 * 60)/death_rate
    immigration_population = (365 * 24 * 60 * 60)/immigration_rate
    current_population = current_population + birth_population + immigration_population - death_rate
    print("Population for next", i+1, "year is: ", current_population)
