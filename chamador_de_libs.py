from printpass import PrintPass as pp
from printpass import PlayerCharacter as pc

player11 = pc('Mateus',20)
# Player12 = pc.age(20) #não funciona 
player11.name = 'Jimmy'

print(player11.name)
print(player11.age)