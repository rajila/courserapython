score = input("Enter Score: ")
_value = float(score)
if _value < 0.0 or _value > 1.0:
    print("Error")
elif _value >= 0.9:
    print("A")
elif _value >= 0.8:
    print("B")
elif _value >= 0.7:
    print("c")
elif _value >= 0.6:
    print("d")
else:
	print("F")
