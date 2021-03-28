#! /usr/bin/env python3

""" example module: extra.iota """

def FunI():
	return "Iota"

def Div():
	try:
		number = int(input("Input number: "))
		div = 1 / number
		return div
	except ZeroDivisionError:
		print("Error ZeroDivisionError, input illegal")
	except ValueError:
		print("Error ValueError, input illegal")
	return None

def getException(type):
	try:
		if type == 1:
			raise IndexError
		elif type == 2:
			raise KeyError
		elif type == 3:
			raise ZeroDivisionError
	except (IndexError, KeyError):
		print("raise -> IndexError, KeyError")
	except ZeroDivisionError:
		print("raise -> ZeroDivisionError")

if __name__ == "__main__":
	print("I prefer to be a module")
