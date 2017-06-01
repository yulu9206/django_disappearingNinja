from django.shortcuts import render

def index(request):
	return render(request, 'disappearing_ninja/index.html')
def ninjas(request):
	return render(request, 'disappearing_ninja/ninjas.html')
def colors(request, color):
	if color == 'red':
		return render(request, 'disappearing_ninja/red.html')
	elif color == 'blue':
		return render(request, 'disappearing_ninja/blue.html')
	elif color == 'orange':
		return render(request, 'disappearing_ninja/orange.html')
	elif color == 'purple':
		return render(request, 'disappearing_ninja/purple.html')
	else:
		return render(request, 'disappearing_ninja/else.html')