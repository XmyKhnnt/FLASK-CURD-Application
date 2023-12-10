from flask import render_template, request
from flask.views import MethodView
from ..models import Student


class StFailsView(MethodView):

    def get(self):

        search = request.args.get('q')
        if search:
            search = str(search).lower()

        student_instance = Student()
        fails = student_instance.studentWithFails(search)
        print(fails)
        return render_template('pages/view-tfails.html', fails=fails)
