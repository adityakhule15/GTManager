from django.db import models
from matplotlib.pyplot import title


''' Models for Login Details '''
class Login(models.Model):
    userName = models.CharField(max_length=100, primary_key = True)
    password = models.CharField(max_length=1000)
    salt = models.CharField(max_length=1000, default= '')
    position_college = models.CharField(max_length=1000, default='False')
    position_hod = models.CharField(max_length=1000, default='False')
    position_teacher = models.CharField(max_length=1000, default='False')
    position_student = models.CharField(max_length=1000, default='False')
    personality_form_check = models.CharField(max_length=1000, default='False')
    class Meta:
        db_table = "login";


''' Models for College Details '''
class College(models.Model):
    college_userName = models.ForeignKey(Login, primary_key=True, default='unknown',on_delete=models.SET_DEFAULT)
    college_name = models.CharField(max_length=1000) 
    college_principal_name = models.CharField(max_length=200) 
    college_email = models.CharField(max_length=1000) 
    college_image=models.CharField(max_length=10000,null=True)

    class Meta:
        db_table = "college"


''' Models for HOD Details '''
class HOD(models.Model):
    college_userName = models.ForeignKey(College, default= 'unknown', on_delete=models.SET_DEFAULT) 
    hod_name = models.CharField(max_length=100)
    hod_mobileNumber = models.CharField(max_length=1000)
    hod_email = models.CharField(max_length=1000) 
    hod_userName = models.ForeignKey(Login, primary_key=True, default='unknown',on_delete=models.SET_DEFAULT)
    hod_departmentName = models.CharField(max_length=1000)
    hod_image=models.CharField(max_length=10000,null=True)

    class Meta:
        db_table = "hod"
 
''' Models for Teachers Details '''
class TeachersDetails(models.Model):
    college_userName = models.ForeignKey(College, default= 'unknown', on_delete=models.SET_DEFAULT) 
    hod_userName = models.ForeignKey(HOD, default= 'unknown', on_delete=models.SET_DEFAULT)
    teachers_userName = models.ForeignKey(Login, primary_key=True, default='unknown', on_delete=models.SET_DEFAULT)
    teachers_name = models.CharField(max_length=100)
    teachers_email = models.CharField(max_length=100)
    teachers_mobileNumber = models.CharField(max_length=1000)
    teachers_groupName = models.CharField(max_length=1000)
    teachers_image=models.CharField(max_length=20000, null=True, blank=True)

    class Meta:
        db_table = "teachers"


''' Models for Student Details '''
class StudentDetails(models.Model):
    hod_userName = models.ForeignKey(HOD, default= 'unknown', on_delete=models.SET_DEFAULT)
    college_userName = models.ForeignKey(College, default= 'unknown', on_delete=models.SET_DEFAULT) 
    teachers_userName = models.ForeignKey(TeachersDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    student_name = models.CharField(max_length=100) 
    student_registrationNumber = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100) 
    student_userName = models.ForeignKey(Login, primary_key=True, default='unknown',on_delete=models.SET_DEFAULT)
    student_permanentAddress = models.CharField(max_length=1000)
    student_correspondenceAddress = models.CharField(max_length=1000)
    student_adharcardNumber = models.CharField( max_length=1000)
    student_mobileNumber = models.CharField(max_length=1000)
    student_fatherMobileNumber = models.CharField(max_length=1000)
    student_motherMobileNumber = models.CharField(max_length=1000)
    student_dob = models.CharField( max_length=1000, default='1899-09-09')
    student_gender = models.CharField(max_length=10)
    student_marital_status = models.CharField(max_length=20)
    student_bloodGroup = models.CharField(max_length=10)
    student_category = models.CharField(max_length=100)
    student_cast = models.CharField(max_length=1000)
    student_alergy = models.CharField(max_length=1000)
    student_familyDoctorName = models.CharField(max_length=1000)
    student_familyDoctorNumber = models.CharField(max_length=1000)
    student_familyDoctorAddress = models.CharField(max_length=1000)
    student_healthProblem = models.CharField(max_length=1000)
    student_regularMedicine = models.CharField(max_length=1000)
    student_localGuardianName = models.CharField(max_length=1000)
    student_localGuardianAddress = models.CharField(max_length=1000)
    student_localGuardianMobileNumber = models.CharField(max_length=1000)
    student_localGuardianEmail = models.CharField(max_length=1000)
    student_previousCollegeName = models.CharField(max_length=1000)
    student_additionalCourses = models.CharField(max_length=1000)
    student_quetionNumber1Answer = models.CharField(max_length=1000)
    student_quetionNumber2Answer = models.CharField(max_length=1000)
    student_quetionNumber3Answer = models.CharField(max_length=1000)
    student_quetionNumber4Answer = models.CharField(max_length=1000)
    student_quetionNumber5Answer = models.CharField(max_length=1000)

    student_firstSet = models.CharField(max_length=1000,default=0)
    student_secondSet = models.CharField(max_length=1000,default=0)
    student_thirdSet = models.CharField(max_length=1000,default=0)
    student_fourthSet = models.CharField(max_length=1000,default=0)
    student_fifthSet = models.CharField(max_length=1000,default=0)

    student_personalityAnalysis = models.CharField(max_length=10000,default=1)

    student_image=models.CharField(max_length=100000, null=True)

    class Meta:
        db_table = "studentDetails"


''' Models for Academic Details '''
class AcademicDetails(models.Model):
    student_userName = models.ForeignKey(StudentDetails, default= 'unknown', on_delete=models.SET_DEFAULT)
    exam_name =  models.CharField(max_length=10000)
    institute = models.CharField(max_length=10000)
    exam_taken_by = models.CharField(max_length=10000)     #Bord
    percentage = models.CharField(max_length=10000)
    total_marks = models.CharField(max_length=10000)
    obtain_marks = models.CharField(max_length=10000)
    year_of_passing = models.CharField(max_length=10000)
    result = models.CharField(max_length=10000)
    subject_back = models.CharField(max_length=10000)

    class Meta:
        db_table = "academicDetails" 


''' Models for Admission Details '''
class AddmissionDetails(models.Model):
    admission_id = models.CharField(max_length=100, primary_key = True) 
    college_userName = models.ForeignKey(College, default= 'unknown', on_delete=models.SET_DEFAULT) 
    student_userName = models.ForeignKey(StudentDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    admission_date = models.CharField(max_length=100)
    admission_year = models.CharField(max_length=100)
    admission_course = models.CharField(max_length=1000)
    admission_course_group = models.CharField( max_length=1000)

    class Meta:
        db_table = "admissionDetails"


''' Models for Attendence '''
class Attendence(models.Model):
    teachers_userName = models.ForeignKey(TeachersDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    date = models.CharField(max_length=1000) 
    present = models.ForeignKey(StudentDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 

    class Meta:
        db_table = "attendence"

''' Models for Complaint '''
class Complaint(models.Model):
    teachers_userName = models.ForeignKey(TeachersDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    student_username = models.ForeignKey(StudentDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    student_name = models.CharField(max_length=1000) 
    title = models.CharField(max_length=1000) 
    description = models.CharField(max_length=100000) 
    
    class Meta:
        db_table = "complaint"

''' Models for Family Details '''
class FamilyDetails(models.Model):
    student_userName = models.ForeignKey(StudentDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    fatherName = models.CharField(max_length=1000)
    motherName = models.CharField(max_length=1000)
    brotherName = models.CharField(max_length=1000)
    sisterName = models.CharField(max_length=1000)
    spouseName = models.CharField(max_length=1000)
    fatherOccupation = models.CharField(max_length=1000)
    motherOccupation = models.CharField(max_length=1000)
    spouseOccupation = models.CharField(max_length=1000)
    fatherIncome = models.CharField(max_length=1000)
    motherIncome = models.CharField(max_length=1000)
    spouseIncome = models.CharField(max_length=1000)

    class Meta:
        db_table = "familyDetails"


''' Models for Previous GT Details '''
class PreviousGTDetails(models.Model):
    student_userName = models.ForeignKey(StudentDetails, default= '0', on_delete=models.SET_DEFAULT) 
    year = models.CharField(max_length=1000)
    gt_name = models.CharField(max_length=1000)

    class Meta:
        db_table = "previousGTDetails"


''' Models for Appointments Details '''
class AppointmentDetails(models.Model):
    id = models.AutoField(primary_key=True)
    student_userName = models.ForeignKey(StudentDetails, default= '0', on_delete=models.SET_DEFAULT) 
    teachers_userName = models.ForeignKey(TeachersDetails, default= 'unknown', on_delete=models.SET_DEFAULT) 
    reason_of_appintment = models.CharField(max_length=1000)
    date_of_appoinment = models.CharField(max_length=1000)
    time_of_appoinment = models.CharField(max_length=1000)
    approval_status = models.CharField(max_length=1000)

    class Meta:
        db_table = "appointmentDetails"


''' Models for Meeting Details '''
class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    meeting_id = models.CharField(max_length=1000) # Making Meeting id a primary key
    organiser_id = models.ForeignKey(TeachersDetails, null=True, on_delete=models.SET_NULL) # Cheacking Admin id in Admin details table and store it into Monthly Target table
    time = models.CharField(max_length=10000)
    date = models.CharField(max_length=10000)
    message = models.CharField(max_length=10000)
    mom = models.CharField(max_length=100000, null=True)
    status = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=100000, null=True)
    link = models.URLField(max_length = 2000)
    type_of_meeting = models.CharField(max_length=100000, null=True)
    
    class Meta:
        db_table = "meeting"