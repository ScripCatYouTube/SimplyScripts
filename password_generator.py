import datetime

from random import seed, randint

list_numbers = '0123456789'
list_symbols = '!@#$%^&*()"№;:?*_+-=[]{}/'

english_alphabet = 'abcdefghijklmnopqrstuvwxyz'

class PasswordGenerator:
	def __init__(self, *alphabets):
		self.alphabets = alphabets

	def generate(self, length):
		if self.is_all_value_type(self.alphabets, str): 
			alphabet = self.compare_list(self.alphabets)

			return self._generate(alphabet, length)
		return False 

	def is_all_value_type(self, list_, type_elements):
		for i in list_:
			if isinstance(i, type_elements) == False: return False
		return True

	def compare_list(self , list_):
		result_text = ''

		for i in list_:
			result_text += str(i)

		return result_text

	def _generate(self, alphabet, length):
		password = ''
		seed(self.get_time())
		lenght_alphabet = len(alphabet) - 1

		for i in range(length):
			random_number = randint(0, lenght_alphabet)
			symbol = alphabet[random_number]
			password += str(symbol)

		return password

	def get_time(self):
		now = datetime.datetime.now()
		date = [now.year, now.month, now.day, now.hour, now.minute, now.second]

		result_date = ''
		for i in date:
			result_date += str(i)

		return int(result_date)

def generate(length = 16):
	generator = PasswordGenerator(
		list_numbers, 
		list_symbols,
		english_alphabet
	)

	return generator.generate(length)
