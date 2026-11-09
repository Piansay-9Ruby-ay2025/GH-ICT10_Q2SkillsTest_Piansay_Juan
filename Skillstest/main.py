# Elements
from pyscript import display, document
# Elements
def get_Element(e):
    document.getElementById('div1').innerHTML = ' '
    NonM=document.getElementById('NonM').value.capitalize().strip()
    Nonmetals = {
'H':['Hydrogen',1,1.008],
'He':['Helium',2,4.003],
'C':['Carbon',6,12.011],
'N':['Nitrogen',7,14.007],
'P':['Phosphorus',15,30.974],
'O':['O',8, 15.999],
'Se':['Selium',34,78.971],
'F':['Flourine',9,18.998],
'Cl':['Chlorine',17,35.45],
'Br':['Bromine',35,79.904],
'I':['Iodine',53,126.904],
'At':['Atessium',85,210],
'Ts':['Tennesium',117,294],
'Og':['Ogasnium',118,294],
'Ne':['Neon',10,20.180],
'Ar':['Argon',18,39.948],
'Kr':['Krypton',36,83.798],
'Xe':['Xenon',54,131.293],
'Rn':['Radon',86,222],
}

# function

    name_checker = NonM in Nonmetals # true or falsse 1 true false 0

    display_message = ('Sorry your name is not on the list', f'{Nonmetals[NonM]} ')

    display(display_message [name_checker], target = 'div1')