from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html',{})

def add(request):
	from random import randint

	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		try:
			answer = int(request.POST['answer'])
		except:
			answer = 0
			my_answer = "Het antwoord is geen goed getal gebruik alleen 0,1,2,3,4,5,6,7,8,9 op het toetsenbord."
			color = "danger"
			return render(request, 'add.html', {
				'answer': answer,
				'my_answer': my_answer,
				'num_1' : num_1,
				'num_2' : num_2,
				'color' : color,
				})

		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		correct_answer = int(old_num_1) + int(old_num_2)

		if answer == correct_answer:
			my_answer = "Goed zo! "+ old_num_1 + " + " + old_num_2 + " = " + str(answer) 
			color = "success"
		else:
			my_answer = "Jammer, niet goed. "+ old_num_1 + " + " + old_num_2 + " is niet " + str(answer) + " het goede antwoord is: " +  str(correct_answer)
			color = "danger"

		return render(request, 'add.html', {
			'answer': answer,
			'my_answer': my_answer,
			'num_1' : num_1,
			'num_2' : num_2,
			'color' : color,
			})
	else:
		return render(request,'add.html',{
			'num_1' : num_1,
			'num_2' : num_2,
			})

def substract(request):
	return render(request,'substract.html',{})

def multiply(request):
	return render(request,'multiply.html',{})

def divide(request):
	return render(request,'divide.html',{})