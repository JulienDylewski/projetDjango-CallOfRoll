from django.shortcuts import render
from .models import Cursus, Student, Presence, ParticularPresence
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .forms import StudentForm, PresenceForm, ParticularPresenceForm
from django.urls import reverse


# Create your views here.
# def index(request):
# return HttpResponse("Racine de lycee")

def detail(request, cursus_id):
    cursus = Cursus.objects.get(pk=cursus_id)
    student_list = Student.objects.filter(cursus=cursus_id)
    context = {
        'cursus': cursus,
        'student_list': student_list
    }

    return render(request, 'lycee/cursus/detail_cursus.html', context)


def callview(request):
    Presence_list = Presence.objects.order_by('date')
    ParticularPresence_list = ParticularPresence.objects.order_by('date')
    context = {
        'Presence_list': Presence_list,
        'ParticularPresence_list': ParticularPresence_list
    }

    print(Presence.objects.get(pk=1).student.all())

    return render(request, 'lycee/call/viewcall.html', context)


def detail_callview(request, presence_id):
    Students_abs = Presence.objects.get(pk=presence_id).student.all()
    cursus_id = Presence.objects.get(pk=presence_id).cursus
    Student_pre = Student.objects.filter(cursus=cursus_id)
    print(Student_pre)
    for absent in Students_abs:
        Student_pre.exclude(id=absent.id)
    context = {
        'Absent_list': Students_abs,
        'Present_list': Student_pre
    }

    print()

    return render(request, 'lycee/call/detail_call.html', context)


def index(request):
    # result_list = Cursus.objects.all()
    result_list = Cursus.objects.order_by('name')

    # template = loader.get_template('lycee/index.html')

    context = {
        'liste': result_list,
    }

    # return HttpResponse(template.render(context,request))

    return render(request, 'lycee/index.html', context)


def detail_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)

    context = {
        'liste': result_list,
    }

    return render(request, 'lycee/student/detail_student.html', context)


class StudentCreateView(CreateView):
    # Modele
    model = Student
    # formulaire
    form_class = StudentForm
    # template
    template_name = 'lycee/student/create.html'

    def get_success_url(self):
        return reverse('detail_student', args=(self.object.pk,))


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'lycee/student/update.html'

    def get_success_url(self):
        return reverse('detail_student', args=(self.object.pk,))


class CursusCallView(CreateView):
    # Modele
    model = Presence
    # formulaire
    form_class = PresenceForm
    # template
    template_name = 'lycee/call/cursuscall.html'

    def get_context_data(self, **kwargs):
        context = super(CursusCallView, self).get_context_data(**kwargs)
        context['cursus'] = Cursus.objects.get(pk=self.kwargs.get("cursus", None))
        return context

    def get_form(self):
        form = super(CursusCallView, self).get_form(self.form_class)

        form.instance.cursus = Cursus.objects.get(pk=self.kwargs.get("cursus", None))
        form.fields["student"].queryset = Student.objects.filter(cursus=self.kwargs.get("cursus", None))
        return form

    def form_valid(self, form):
        form.instance.cursus = Cursus.objects.get(pk=self.kwargs.get("cursus", None))
        return super().form_valid(form)


class ParticularCallView(CreateView):
    # Modele
    model = ParticularPresence
    # formulaire
    form_class = ParticularPresenceForm
    # template
    template_name = 'lycee/call/particularcall.html'

    # def get_form(self):
    #       form = super(CursusCallView, self).get_form(self.form_class)

    #       form.instance.cursus = Cursus.objects.get(pk=self.kwargs.get("cursus",None))
    #       form.fields["student"].queryset = Student.objects.filter(cursus=self.kwargs.get("cursus",None))
    #       return form

    # def form_valid(self, form):
    #   form.instance.cursus = Cursus.objects.get(pk=self.kwargs.get("cursus",None))
    #   return super().form_valid(form)
