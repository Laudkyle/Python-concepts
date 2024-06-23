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
intersection = lettersA & letters