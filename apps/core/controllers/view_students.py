

from flask import render_template, request, redirect, url_for
from ..models import Student

from flask.views import MethodView
from ..forms import StudentForm


class ViewStudent(MethodView):

    def __init__(self) -> None:
        super().__init__()

        self.errors = []

    def get(self):

        search_query = request.args.get('q')

        if search_query:
            search_query = str(search_query).lower()
        else:
            search_query = None

        st_form = StudentForm()
        student = Student().getStudents(search_query=search_query)

        return render_template('pages/view-students.html', students=student, form=st_form, errors=self.errors)

    def post(self):

        st_form = StudentForm(request.form)
        student_instance = Student()
        student = student_instance.getStudents()

        if st_form.validate():
            print(st_form.data)

            if student_instance.validateStudent(st_form.id.data):
                self.errors.append('Student ID already exists')

            else:
                try:
                    student_instance.insertStudent(st_form.data)
                    return redirect(url_for('main.students', success='True', msg='Student added successfully'))

                except Exception as e:
                    print(e)
                    self.errors.append('Error inserting student')
                    self.errors.append(e)

        return render_template('pages/view-students.html', students=student, form=st_form, errors=self.errors)
