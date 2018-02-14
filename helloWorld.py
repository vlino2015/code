
#names = ['George', 'W', 'Bush']
#for name in names:
#    print(name)

#names.append("hello there")

#for name in names:
#    print(name)


#name = 'George W Bush'
#
# for character in name:
#    print(character)

def g(x):
  return x + 1
for x in range(-3, 5):
  print("f({x})={y} \t g({x})={z}".format(
          x=x, y=f(x), z=g(x)
       ))