from __future__ import print_function


class Items(object):

    def __init__(self, name, type, weight, price):
        self.name = name
        self.type = type
        self.weight = weight
        self.price = price

    def __str__(self):
        return f'Name: {self.name} Type: {self.type} Weight: {self.weight} Price: {self.price}'


def partition(array, low, high):

    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
          i = i + 1

          (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)


banana = Items("banana", "Food", 0.2, 20)
phone = Items("phone", "Electronics", 0.8, 23000)
keyboard = Items("keyboard", "Electronics", 1.0, 3000)
notebook = Items("notebook", "Electronics", 2.2, 19000)
mouse = Items("mouse", "Electronics", 0.3, 4000)
screen = Items("screen", "Electronics", 1.4, 7000)
tea = Items("tea", "Electronics", 0.6, 700)
lamp = Items("lamp", "Electronics", 0.2, 4000)
headphones = Items("headphones", "Electronics", 0.2, 15000)
cheese = Items("cheese", "Food", 0.5, 1000)
watch = Items("watch", "Electronics", 0.2, 13000)
whiskey = Items("whiskey", "Food", 0.75, 60000)
xbox = Items("xbox", "Electronics", 0.9, 27000)
beer = Items("beer", "Food", 0.5, 300)
fish = Items("fish", "Food", 1.9, 9000)

item_list = [banana, phone, keyboard, notebook, mouse, screen, tea, lamp, headphones, cheese, watch, whiskey, xbox, beer, fish]
backpack = []

for i in item_list:
    backpack.append((i.name, i.weight, i.price / i.weight / 10))
counter = 0

sortedBackPack = sorted(backpack, key=lambda price: price[2])
sortedBackPack.reverse()
finalCount = 0
BackpackCapacity = 5.3
totalPricePer100gramm = 0
totalPrice = 0
just = 0
finalBackPack = []
print("##################################################################################################################")
while counter < len(sortedBackPack):
    if finalCount <= BackpackCapacity:
        #print("ProductName", "(", sortedBackPack[counter][0], ")", "Weight:", "(", sortedBackPack[counter][1], ")", "Price per 100 grams of product:", "(", sortedBackPack[counter][2], ")")
        totalPricePer100gramm += int(sortedBackPack[counter][2])
        finalCount += sortedBackPack[counter][1]
        finalBackPack.append(sortedBackPack[counter])
        if finalCount > BackpackCapacity:
            finalCount -= sortedBackPack[counter][1]
            finalBackPack.pop(just)
            just -= 1
        counter += 1
        just += 1

counter1 = 0
while counter1 < len(finalBackPack):
    print("ProductName", "(", finalBackPack[counter1][0], ")", "Weight:", "(", finalBackPack[counter1][1], ")",
          "Price:", "(", finalBackPack[counter1][2] * finalBackPack[counter1][1] * 10, ")")
    totalPrice += finalBackPack[counter1][2] * finalBackPack[counter1][1] * 10

    counter1 += 1
    if counter1 == counter:
        break

print("##################################################################################################################")
print("-Totals",  "(Items:", just, ")", "(Weight:", round(finalCount, 2), ")", "(Price:", totalPrice, ")")
