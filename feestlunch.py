#feestlunch.py
croissant= int(input('hoeveel croissants heb je?'))
croissantjes= croissant * 0.39 
stokbrood= int(input('hoeveel stokbrood heb je?'))
stokbroden= stokbrood * 2.78
kortingsbon= int(input('hoeveel kortingsbonnen heb je?'))
kortingsbonnen= kortingsbon * 0.50
totaal = int (input(croissantjes + stokbroden - kortingsbonnen))

