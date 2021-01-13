# score = input("Enter Score: ")
# _value = float(score)
# if _value < 0.0 or _value > 1.0:
#     print("Error")
# elif _value >= 0.9:
#     print("A")
# elif _value >= 0.8:
#     print("B")
# elif _value >= 0.7:
#     print("c")
# elif _value >= 0.6:
#     print("d")
# else:
# 	print("F")
for _el in range(0, 10, 2):
    print(_el)

_notes = [1,2,3,4,5,6,7]
print(_notes) # print all elements
print(_notes[:]) # print all elements
print(_notes[0:-1])
print(_notes[1:-2])
print(_notes[-2:1]) # empty
print(_notes[:-2])
print(_notes[-2:])
print(_notes[-4:-2])
print(_notes[-2:-4]) # empty
print(_notes[-2:1:-1])
print(_notes[::1])
print(_notes[::2])
