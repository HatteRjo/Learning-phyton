import random 
while true:
 print() 
 usersQuestion = input( "preguntale a la bola 8 lo que quieras
(press enter to quit): ")
 if usersQuestion == “:
 break 
 randomAnswer = random.randrange(0, 7) 
 if randomAnswer == 0:
 print('It is certain.')
 elif randomAnswer == 1:
 print('Absolutely!')
 elif randomAnswer == 2:
 print('You may rely on it.')
 elif randomAnswer == 3:
 print('Answer is foggy, ask again later.')
 elif randomAnswer == 4:
 print('Concentrate and ask again.')
 elif randomAnswer == 5:
 print('Unsure at this point, try again.')
 elif randomAnswer == 6:
 print('No way, dude!')
 elif randomAnswer == 7:
 print('No, no, no, no, no.')
