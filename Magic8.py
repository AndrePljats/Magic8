import random
def random_ans():
	answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
			   "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
			   "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
			   "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
	return random.choice(answers)
def body():
	while True:
		print('Ask the question!')
		input()
		print(random_ans())
		break
	if retry():
		body()
def name():
	print('What`s your name?')
	name_in=input()
	print('Hello,', name_in)
def retry():
	print('Do you have another one question? y/n')
	while True:
		ans=input()
		if ans=='y':
			return True
		elif ans=='n':
			print('See you soon!')
			return False
		else:
			print("Please input 'y' or 'n'")
def game():
	print('Hello, I`m a magic ball, come on - ask the question!')
	name()
	body()
game()

