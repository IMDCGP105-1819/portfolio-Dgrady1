beer_bottles = 99
while beer_bottles >= 2:
    print(beer_bottles, "bottles of beer on the wall,", beer_bottles, "bottles of beer")
    beer_bottles = beer_bottles - 1
    print("Take one down, pass it around", beer_bottles, "bottles of beer on the wall")
else:
    print(beer_bottles, "bottle of beer one the wall", beer_bottles, "bottle of beer! So take it down, pass it around, no more bottles of beer on the wall")
