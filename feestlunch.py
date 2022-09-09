#feestlunch.py
croissant= int(input('hoeveel croissants heb je?'))
croissantjes= croissant * 0.39 
stokbrood= int(input('hoeveel stokbrood heb je?'))
stokbroden= stokbrood * 278
kortingsbon= int(input('hoeveel kortingsbonnen heb je?'))
kortingsbonnen= kortingsbon * 0.50
totaal = int (input(croissantjes + stokbroden - kortingsbonnen))
print ( 'totaal', totaal 'cent')
print ( f'De feestlunch kost je bij de bakker {totaal} voor de {croissant}en de {stokbrood}als de {kortingsbon} nog geldig zijn!')
