from flask import render_template, request
from flask.views import MethodView

from ..models import Student


class ViewStudentsDetails(MethodView):

    def get(self):
        query_param = request.args.get('q')

        students = Student().getStudentCourses(query_param)

        return render_template('pages/view-stdetails.html', students=students)
