from django.shortcuts import render

# Create your views here.
def UserProfile(request):
	if request.method == 'POST':
		JDCode = request.POST['JDCode']
		VacancyCode = request.POST['VacancyCode']
		Title = request.POST['Title']
		Location = request.POST['Location']
		HiringManager = User.objects.make_random_HiringManager()
		RequisitionManager = request.POST['RequisitionManager']
		KeySkills = request.POST['KeySkills']
		Role = request.POST['Role']
		DesiredExperience = request.POST['DesiredExperience']
		Education = request.POST['Education']
		MinExpRange = request.POST['MinExpRange']
		MaxExpRange = request.POST['MaxExpRange']
		CTC = request.POST['CTC']
		NoticePeriod = request.POST['NoticePeriod']
		Status = request.POST['Status']
		Openings = request.POST['Openings']
		No_Filled = request.POST['No_Filled']
		HiringMgrContact = request.POST['HiringMgrContact']
		HiringMgrEmail = request.P = request.POST['HiringMgrEmail']
		RecruiterAssignedTo = request.POST['RecruiterAssignedTo']
		AssignedDate = request.POST['AssignedDate']
		ClientID = request.POST['ClientID']

		user = User(JDCode=JDCode,VacancyCode=VacancyCode,Title=Title,Location=Location,HiringManager=HiringManager,RequisitionManager=RequisitionManager,KeySkills=KeySkills,Role=Role,DesiredExperience=DesiredExperience,Education=Education, MinExpRange=MinExpRange, MaxExpRange=MaxExpRange, CTC=CTC, NoticePeriod=NoticePeriod, Status=Status, Openings=Openings, No_Filled=No_Filled, HiringMgrContact=HiringMgrContact, HiringMgrEmail=HiringMgrEmail, RecruiterAssignedTo=RecruiterAssignedTo, AssignedDate=AssignedDate, ClientID=ClientID)
		user.save()
		print('Mandates Uploaded')


	else:
		return render(request,'mandates.html')