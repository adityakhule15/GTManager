import pickle
import numpy as np
import pandas as pd
from .serializers import *
from AcademicDetails.models import Login, StudentDetails
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt 
import base64
from django.conf import settings
import sklearn
from sklearn.neighbors import DistanceMetric
 
@csrf_exempt
class StudentDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        usname = request.POST.get('student_userName')
        # Saving information into login details table
        frProd = Login()
        frProd.userName= usname
        frProd.position_student = 'True'
        #  Getting the password and doing incruption of it
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        frProd.password= new_key
        frProd.save()

        # Saving information into College details table
        prod=StudentDetails()
        prod.student_userName_id=usname
        prod.hod_userName_id=request.POST.get('hod_userName')
        prod.teachers_userName_id=request.POST.get('teachers_userName')
        prod.college_userName_id=request.POST.get('college_userName')
        prod.student_name=request.POST.get('student_name')
        prod.student_registrationNumber=request.POST.get('student_registrationNumber')
        prod.student_email=request.POST.get('student_email')
        prod.student_mobileNumber=request.POST.get('student_mobileNumber')
        prod.student_image='/student_images/' + usname + '.jpeg'
        prod.save()
       
        return HttpResponse("Success")


    @csrf_exempt
    def personalityPrediction(request):
      
        #SalesnetLogin.objects.filter(userName = item['userName']).update(personality_form_check = 'True')
        print(request.POST.get('userName'))
        ExecutiveDetails_out = StudentDetails.objects.filter(student_userName = request.POST.get('userName')).all()
        serializers = OnlyStudentDetailsSerializer(ExecutiveDetails_out, many = True)
        total_ExecutiveDetails_out= json.dumps(serializers.data)
        total_ExecutiveDetails_out = json.loads(total_ExecutiveDetails_out)
        print('total_ExecutiveDetails_out')
        print(total_ExecutiveDetails_out)
        gender = total_ExecutiveDetails_out[0]['student_gender']
        

        first_set = request.POST.get('first_set') 
        first_set= first_set.replace('[', '')
        first_set= first_set.replace(']', '')
        first_set= first_set.replace(" ,", '')
        first_set= first_set.replace(" ", '')
        first_set = first_set.split(',')
        print(first_set)

        second_set = request.POST.get('second_set') 
        second_set= second_set.replace('[', '')
        second_set= second_set.replace(']', '')
        second_set= second_set.replace(" ,", '')
        second_set= second_set.replace(" ", '')
        second_set = second_set.split(',')
        print(second_set)

        third_set = request.POST.get('third_set') 
        third_set= third_set.replace('[', '')
        third_set= third_set.replace(']', '')
        third_set= third_set.replace(" ,", '')
        third_set= third_set.replace(" ", '')
        third_set = third_set.split(',')
        print(third_set)

        fourth_set = request.POST.get('fourth_set') 
        fourth_set= fourth_set.replace('[', '')
        fourth_set= fourth_set.replace(']', '')
        fourth_set= fourth_set.replace(" ,", '')
        fourth_set= fourth_set.replace(" ", '')
        fourth_set = fourth_set.split(',')
        print(fourth_set)

        fifth_set = request.POST.get('fifth_set') 
        fifth_set= fifth_set.replace('[', '')
        fifth_set= fifth_set.replace(']', '')
        fifth_set= fifth_set.replace(" ,", '')
        fifth_set= fifth_set.replace(" ", '')
        fifth_set = fifth_set.split(',')
        print(fifth_set)

        first_set_pickle = open('/home/ubuntu/FINAL PROJECT/GTManager/Student/ext_pickle','rb')
        ext_file=pickle.load(first_set_pickle)
        ext_out = ext_file.predict([[int(float(first_set[0])),-int(float(first_set[1])) , int(float(first_set[2])), -int(float(first_set[3])) ,int(float(first_set[4])),-int(float(first_set[5])) ,int(float(first_set[6])) ,-int(float(first_set[7])) ,int(float(first_set[8])) ,-int(float(first_set[9]))]])[0]
        del ext_file

        second_set_pickle = open('/home/ubuntu/FINAL PROJECT/GTManager/Student/est_pickle','rb')
        est_file=pickle.load(second_set_pickle)
        est_out =  est_file.predict([[int(float(second_set[0])),-int(float(second_set[1])) , int(float(second_set[2])), -int(float(second_set[3])) ,int(float(second_set[4])),int(float(second_set[5])) ,int(float(second_set[6])) ,int(float(second_set[7])) ,int(float(second_set[8])) ,int(float(second_set[9]))]])[0]
        del est_file

        third_set_pickle = open('/home/ubuntu/FINAL PROJECT/GTManager/Student/agr_pickle','rb')
        agr_file=pickle.load(third_set_pickle)
        agr_out = agr_file.predict([[int(float(third_set[0])),int(float(third_set[1])) , -int(float(third_set[2])), int(float(third_set[3])) ,-int(float(third_set[4])),int(float(third_set[5])) ,-int(float(third_set[6])) ,int(float(third_set[7])) ,int(float(third_set[8])) ,int(float(third_set[9]))]])[0]
        del agr_file       

        fourth_set_pickle = open('/home/ubuntu/FINAL PROJECT/GTManager/Student/csn_pickle','rb')
        csn_file=pickle.load(fourth_set_pickle)
        csn_out =  csn_file.predict([[int(float(fourth_set[0])),-int(float(fourth_set[1])) , int(float(fourth_set[2])), -int(float(fourth_set[3])) ,int(float(fourth_set[4])),-int(float(fourth_set[5])) ,int(float(fourth_set[6])) ,-int(float(fourth_set[7])) ,int(float(fourth_set[8])) ,int(float(fourth_set[9]))]])[0] 
        del csn_file 

        fifth_set_pickle = open('/home/ubuntu/FINAL PROJECT/GTManager/Student/opn_pickle','rb')
        opn_file=pickle.load(fifth_set_pickle)
        opn_out = opn_file.predict([[int(float(fifth_set[0])),-int(float(fifth_set[1])) , int(float(fifth_set[2])), -int(float(fifth_set[3])) ,int(float(fifth_set[4])), -int(float(fifth_set[5])) ,int(float(fifth_set[6])) ,int(float(fifth_set[7])) ,int(float(fifth_set[8])) ,int(float(fifth_set[9]))]])[0]
        print()
        del opn_file 

        StudentDetails.objects.filter(student_userName = request.POST.get('student_userName')).update(     
        student_personalityAnalysis= "open",
        student_firstSet = [int(float(first_set[0])),-int(float(first_set[1])) , int(float(first_set[2])), -int(float(first_set[3])) ,int(float(first_set[4])),-int(float(first_set[5])) ,int(float(first_set[6])) ,-int(float(first_set[7])) ,int(float(first_set[8])) ,-int(float(first_set[9]))],
        student_secondSet = [int(float(second_set[0])),-int(float(second_set[1])) , int(float(second_set[2])), -int(float(second_set[3])) ,int(float(second_set[4])),int(float(second_set[5])) ,int(float(second_set[6])) ,int(float(second_set[7])) ,int(float(second_set[8])) ,int(float(second_set[9]))],
        student_thirdSet = [int(float(third_set[0])),int(float(third_set[1])) , -int(float(third_set[2])), int(float(third_set[3])) ,-int(float(third_set[4])),int(float(third_set[5])) ,-int(float(third_set[6])) ,int(float(third_set[7])) ,int(float(third_set[8])) ,int(float(third_set[9]))],
        student_fourthSet = [int(float(fourth_set[0])),-int(float(fourth_set[1])) , int(float(fourth_set[2])), -int(float(fourth_set[3])) ,int(float(fourth_set[4])),-int(float(fourth_set[5])) ,int(float(fourth_set[6])) ,-int(float(fourth_set[7])) ,int(float(fourth_set[8])) ,int(float(fourth_set[9]))],
        student_fifthSet = [int(float(fifth_set[0])),-int(float(fifth_set[1])) , int(float(fifth_set[2])), -int(float(fifth_set[3])) ,int(float(fifth_set[4])), -int(float(fifth_set[5])) ,int(float(fifth_set[6])) ,int(float(fifth_set[7])) ,int(float(fifth_set[8])) ,int(float(fifth_set[9]))],
        )
        output_ext   =  "En" if ext_out else "Ey" 
        output_est   =  "Nn" if est_out else "Ny" 
        output_agr   =  "An" if agr_out else "Ay" 
        output_cons  =  "Cy" if csn_out else "Cn" 
        output_opn   =  "On" if opn_out else "Oy" 

       
        output=output_ext+output_est+output_agr+output_cons+output_opn
        #print("Concatenated two different strings:",output)
        #print(output)
        #output = "EnNyAyCnOy"
        print(output)
        print("-----------------------------------")
        read_personality = pd.read_csv('/home/ubuntu/FINAL PROJECT/GTManager/Student/personality_types.csv', sep = ';')
        read_personality = np.array(read_personality)
        print(len(read_personality))
        for data in read_personality:
            print(data[0])
            if data[0] == output:
                print("True")
                # PersonalityRate = data[2]
                if gender == 'Male':
                     ananlysis = data[1].replace("his/her" , "his")
                     ananlysis = data[1].replace("His/Her" , "His") 
                     ananlysis = data[1].replace("him/her" , "him") 
                     ananlysis = ananlysis.replace("himself/herself" , "himself")
                     ananlysis = ananlysis.replace("He/She" , "He")
                     ananlysis = ananlysis.replace("he/she" , "he") 
                     break
                else:
                     ananlysis = data[1].replace("his/her" , "him")
                     ananlysis = data[1].replace("His/Her" , "Her") 
                     ananlysis = data[1].replace("him/her" , "her")  
                     ananlysis = ananlysis.replace("himself/herself" , "herself")
                     ananlysis = ananlysis.replace("He/She" , "She")
                     ananlysis = ananlysis.replace("he/she" , "she") 
                     break
        print(ananlysis)
        student_userName = request.POST.get('userName')
        StudentDetails.objects.filter(student_userName = student_userName).update(
        student_personalityAnalysis=ananlysis)
        
        return HttpResponse("Success")

    @csrf_exempt
    def updatePersonalityCheck(request):       
        student_userName = request.POST.get('userName')
        Login.objects.filter(userName = student_userName).update(
        personality_form_check='True')

        return HttpResponse("Success")    


    # Getting  College Details from database 
    @csrf_exempt
    def StudentList(request):
        teachers_userName = request.POST.get('teachers_userName')
        print(teachers_userName)
        StudentDetails1=StudentDetails.objects.filter(teachers_userName = teachers_userName).all()
        serializer = StudentDetailsSerializer(StudentDetails1, many = True)
        total_StudentDetails1 = json.dumps(serializer.data)
        total_StudentDetails = json.loads(total_StudentDetails1)
        data = {'StudentList':total_StudentDetails}
        return JsonResponse(data)
        
    # Getting  College Details from database 
    @csrf_exempt
    def StudentDetails(request):
        student_userName = request.POST.get('student_userName')
        print(student_userName)
        StudentDetails1=StudentDetails.objects.filter(student_userName = student_userName).all()
        serializer = StudentDetailsSerializer(StudentDetails1, many = True)
        total_StudentDetails1 = json.dumps(serializer.data)
        total_StudentDetails = json.loads(total_StudentDetails1)
        data = {'StudentDetails':total_StudentDetails}
        return JsonResponse(data)
  
    @csrf_exempt
    def update(request):       

        StudentDetails.objects.filter(student_userName = request.POST.get('student_userName')).update(
        student_name=request.POST.get('student_name'),
        student_registrationNumber=request.POST.get('student_registrationNumber'),
        student_email=request.POST.get('student_email'),
        student_permanentAddress=request.POST.get('student_permanentAddress'),
        student_correspondenceAddress=request.POST.get('student_correspondenceAddress'),
        student_adharcardNumber=request.POST.get('student_adharcardNumber'),
        student_mobileNumber=request.POST.get('student_mobileNumber'),
        student_fatherMobileNumber=request.POST.get('student_fatherMobileNumber'),
        student_motherMobileNumber=request.POST.get('student_motherMobileNumber'),
        student_dob=request.POST.get('student_dob'),
        student_gender=request.POST.get('student_gender'),
        student_marital_status=request.POST.get('student_marital_status'),
        student_bloodGroup=request.POST.get('student_bloodGroup'),
        student_category=request.POST.get('student_category'),
        student_cast=request.POST.get('student_cast'),
        student_alergy=request.POST.get('student_alergy'),
        student_familyDoctorName=request.POST.get('student_familyDoctorName'),
        student_familyDoctorNumber=request.POST.get('student_familyDoctorNumber'),
        student_familyDoctorAddress=request.POST.get('student_familyDoctorAddress'),
        student_healthProblem=request.POST.get('student_healthProblem'),
        student_regularMedicine=request.POST.get('student_regularMedicine'),
        student_localGuardianName=request.POST.get('student_localGuardianName'),
        student_localGuardianAddress=request.POST.get('student_localGuardianAddress'),
        student_localGuardianMobileNumber=request.POST.get('student_localGuardianMobileNumber'),
        student_localGuardianEmail=request.POST.get('student_localGuardianEmail'),
        student_previousCollegeName=request.POST.get('student_previousCollegeName'),
        student_additionalCourses=request.POST.get('student_additionalCourses'),
        student_quetionNumber1Answer=request.POST.get('student_quetionNumber1Answer'),
        student_quetionNumber2Answer=request.POST.get('student_quetionNumber2Answer'),
        student_quetionNumber3Answer=request.POST.get('student_quetionNumber3Answer'),
        student_quetionNumber4Answer=request.POST.get('student_quetionNumber4Answer'),
        student_quetionNumber5Answer=request.POST.get('student_quetionNumber5Answer'),
        )
        
        return HttpResponse("Success")    

    @csrf_exempt
    def updateImage(request):
    
        usname=request.POST.get('student_userName')
        print(usname)
        image=request.POST['image'],
        imgdata = base64.b64decode(image[0])
        path = settings.MEDIA_ROOT + '/student_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        return HttpResponse("Success")  
