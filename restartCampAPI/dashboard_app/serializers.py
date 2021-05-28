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

class MemberSerializers(serializers.ModelSerializer):
	team_name = serializers.ReadOnlyField(source='team.name')
	class Meta:
		model = Member
		fields = [field.name for field in model._meta.fields]
		fields.append('team_name')

class CoursesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Courses
		fields = '__all__'

class LearnerSerializers(serializers.ModelSerializer):
#	course_name = CoursesSerializers(many=True, read_only=True)
	class Meta:
		model = Learner
		fields = '__all__'
		depth = 1
	#	fields.append('course_name')

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

# class LearnerSubmittedToCoursesSerializers(serializers.ModelSerializer):
# 	class Meta:
# 		model = LearnerSubmittedToCourses
# 		fields = '__all__'

class TeamRoleSerializers(serializers.ModelSerializer):
	class Meta:
		model = TeamRole
		fields = '__all__'

class TeamSerializers(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = '__all__'

class WorkExperienceSerializers(serializers.ModelSerializer):
	class Meta:
		model = WorkExperience
		fields = '__all__'


class ViewCourseScheduleTrainerSerializers(serializers.ModelSerializer):
	class Meta:
		model = ViewCourseScheduleTrainer
		fields = '__all__'


class TestimonialsSerializers(serializers.ModelSerializer):
	class Meta:
		model = Testimonials
		fields = '__all__'
