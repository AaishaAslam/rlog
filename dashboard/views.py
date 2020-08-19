from django.shortcuts import render

# Create your views here.
def UserProfile(request):
	if request.method == 'POST':
		designation = request.POST['designation']
		website_link = request.POST['website_link']
		name = request.POST['name']
		user_id = request.POST['user_id']
		email = request.POST['emails']
		password = User.objects.make_random_password()
		phone_number = request.POST['phone_number']
		seniority_level = request.POST['seniority_level']
		total_recruitment = request.POST['total_recruitment']
		your_bio = request.POST['your_bio']
		team_members = request.POST['team_members']
		

		user = User(designation=designation,website_link=website_link,name=name,user_id=user_id,email=email,password=password,phone_number=phone_number,seniority_level=seniority_level,total_recruitment=total_recruitment,your_bio=your_bio,team_members=team_members)
		user.save()
		print('Profile Updated')


	else:
		return render(request,'UserProfile.html')