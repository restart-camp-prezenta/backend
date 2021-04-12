from rest_framework import serializers
from .models import *

class CourseCategorySerializers(serializers.ModelSerializer):
	class Meta:
		model = CourseCategory
		fields = '__all__'

class DiscountSerializers(serializers.ModelSerializer):
	class Meta:
		model = Discount
		fields = '__all__'

class OwnerSerializers(serializers.ModelSerializer):
	class Meta:
		model = Owner
		fields = '__all__'

class TrainerSerializers(serializers.ModelSerializer):
	class Meta:
		model = Trainer
		fields = '__all__'

class CoursesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Courses
		fields = '__all__'

class OwnerPrcSerializers(serializers.ModelSerializer):
	class Meta:
		model = OwnerPrc
		fields = '__all__'

class TrainerPrcSerializers(serializers.ModelSerializer):
	class Meta:
		model = TrainerPrc
		fields = '__all__'

class ScheduleSerializers(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = '__all__'

class JobDomainsSerializers(serializers.ModelSerializer):
	class Meta:
		model = JobDomains
		fields = '__all__'

class StudentsSerializers(serializers.ModelSerializer):
	class Meta:
		model = Students
		fields = '__all__'

class InvoiceSerializers(serializers.ModelSerializer):
	class Meta:
		model = Invoice
		fields = '__all__'

class SoldCoursesSerializers(serializers.ModelSerializer):
	class Meta:
		model = SoldCourses
		fields = '__all__'

class ParticipantsSerializers(serializers.ModelSerializer):
	class Meta:
		model = Participants
		fields = '__all__'

class TargetsSerializers(serializers.ModelSerializer):
	class Meta:
		model = Targets
		fields = '__all__'