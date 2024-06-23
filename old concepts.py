## When you want to specify the data type of a variable

brand: str = "New rand old {} brands{}"

## When you want to specify the return type of a function 

def func() -> int:
    return 0

brands = ["Nike","Volks","Wagon"]
print(brand.join(brands))

print(brand.format("name","worth"))
brandss = ["brand 1","brand 2"]
# Ternary If statements

message = 'positive' if len(brand) > 3 else " 0 or negative"
print(message)

brands.extend(brandss) # Adding an iterable to a list

del brands[4]

print(brands)
print(brands.index("brand 1"))

brands = set(brands)
print(brands)

lettersA  = {'a','b','c','d'}
lettersB  = {'f','e','a','g'}

union = lettersA | lettersB
intersection = lettersA & lettersB
diff = lettersA - lettersB

print("""
      This is the Union of sets{}
      This is the Intersection of sets {}
      This is the Difference of sets {}
      """.format(union,intersection,diff))

## Dictionaries

person = {
    'Name': "Kyle",
    'Age':26,
    'Location': "University of Cape Coast"
}

for key, value in person.items():
    print("Key: {}, Value: {}".format(key,value))
