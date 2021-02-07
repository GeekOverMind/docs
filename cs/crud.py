# education.views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# view-func for a exam score
@permission_required('full_access')
def exam_score(request, user_id):
	"""
	Функция отображения для вывода успеваемости учащегося
	"""
	# необходимо сделать JOIN из таблиц Users, Lesson
	...

	
# semesters CRUD-classes
class SemesterCreate(LoginRequiredMixin, CreateView):
	model = Semester
	fields = '__all__'
	template_name = 'education/create_edit_form.html'


class SemesterUpdate(LoginRequiredMixin, UpdateView):
    model = Semester
    fields = ['title']
    template_name = 'education/create_edit_form.html'


class SemesterDelete(LoginRequiredMixin, DeleteView):
    model = Semester
    success_url = reverse_lazy('semesters')
	template_name = 'education/delete_form.html'	
	

# lessons CRUD-classes
class LessonCreate(LoginRequiredMixin, CreateView):
	model = Lesson
	fields = '__all__'
	template_name = 'education/create_edit_form.html'


class LessonUpdate(LoginRequiredMixin, UpdateView):
    model = LessonContent
    fields = ['__all__']
    template_name = 'education/create_edit_form.html'	

	
class LessonDelete(LoginRequiredMixin, DeleteView):
    model = Lesson
    success_url = reverse_lazy('lessons')
	template_name = 'education/delete_form.html'
	

# lessons content CRUD-classes
class LessonContentCreate(LoginRequiredMixin, CreateView):
	model = LessonContent
	fields = '__all__'
	template_name = 'education/create_edit_form.html'


class LessonContentUpdate(LoginRequiredMixin, UpdateView):
    model = LessonContent
    fields = ['__all__']
    template_name = 'education/create_edit_form.html'

	
class LessonContentDelete(LoginRequiredMixin, DeleteView):
    model = Lesson
    success_url = reverse_lazy('???')
	template_name = 'education/delete_form.html'

	
# education.urls.py
# semester crud urls
url(r'^semester/create/$', views.SemesterCreate.as_view(), name='semester-create'),
url(r'^semester/(?P<pk>\d+)/update/$', views.SemesterUpdate.as_view(), name='semester-update'),
url(r'^semester/(?P<pk>\d+)/delete/$', views.SemesterDelete.as_view(), name='semester-delete'),

# lessons crud urls
url(r'^lesson/create/$', views.LessonCreate.as_view(), name='lesson-create'),
url(r'^lesson/(?P<pk>\d+)/update/$', views.LessonUpdate.as_view(), name='lesson-update'),
url(r'^lesson/(?P<pk>\d+)/delete/$', views.LessonDelete.as_view(), name='lesson-delete'),

# lessons content crud urls
url(r'^???/create/$', views.LessonContentCreate.as_view(), name='???-create'),
url(r'^???/(?P<pk>\d+)/update/$', views.LessonContentUpdate.as_view(), name='???-update'),
url(r'^???/(?P<pk>\d+)/delete/$', views.LessonContentDelete.as_view(), name='???-delete'),


# education.models.py
class SchoolPerformance(models.Model):
	"""
	Модель, описывающая успеваемость учащихся
	"""
	user_id = model.ForeignKey('User', on_delete=models.SET_NULL, null=True)
	lesson = model.ForeignKey('User', on_delete=models.SET_NULL, null=True)
	
	TYPE_EXAM = (
		('o', 'зачет'),
		(range(1, 101), 'экзамен')
	)
	
	format = model.Models(max_length=3, choices=TYPE_EXAM, blank=True, default='o', help_text='Тип сдачи')
