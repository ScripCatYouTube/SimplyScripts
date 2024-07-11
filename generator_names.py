import pyttsx3
from random import choice

listvowels = "aоеуяию"
listconsonants = "цкнгшщзхфвпрлджчсмтб"

double_vowels = 'аааоии'
double_consonants = 'ввннгпррккммддбб'

listvowels += double_vowels
listconsonants += double_consonants

formats = ["{0}{1}", "{0}{1}{2}","{0}"]
max_len_formats = 100
min_len_formats = 4
chance_list = [0,0,0, 2]

dict_russian_sound = {
	'а':'a',
	'о':'o',
	'е':'ye',
	'у':'u',
	'я':'ya',
	'и':'i',
	'ю':'yu',
	'ц':'ts',
	'к':'kh',
	'н':'n',
	'г':'g',
	'ш':'sh',
	'щ':'chs',
	'з':'z',
	'х':'h',
	'ф':'f',
	'в':'v',
	'п':'p',
	'р':'r',
	'л':'l',
	'д':'d',
	'ж':'j',
	'ч':'ch',
	'с':'s',
	'м':'m',
	'т':'t',
	'б':'b'

}

result = ""

for i in range(0, max_len_formats):
	if i != 0:
		ii = choice(chance_list)
	elif i == 0:
		ii = 0
	
	if ii == 0:
		result += choice(listconsonants) + choice(listvowels)
	elif ii == 1:
		result += choice(listconsonants) + choice(listconsonants) + choice(listvowels)
	elif ii == 2:
		result += choice(listvowels)

def from_russian_in_english(russian_text):
	english_sound_text = russian_text
	for i in dict_russian_sound:
		english_sound_text = english_sound_text.replace(i, dict_russian_sound[i])
	return english_sound_text

english_name = from_russian_in_english(result)

print(english_name)
print(result.title(), "\n")
exit()
engine = pyttsx3.init()

# Set the speed and volume of the voice
engine.setProperty('rate', 100)  # 150 words per minute
engine.setProperty('volume', 0.8)  # 80% volume

# Convert the text to speech
engine.say(english_name)
engine.runAndWait()

