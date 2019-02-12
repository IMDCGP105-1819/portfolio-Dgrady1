beer_bottles = 99
while beer_bottles >= 1:
    print(beer_bottles, "bottles of beer on the wall,", beer_bottles, "of beer.")
    beer_bottles = beer_bottles - 1
    print("take one down pass it around", beer_bottles, "bottles of beer on the wall")
else:
    print("no more bottles of beer on the wall")
