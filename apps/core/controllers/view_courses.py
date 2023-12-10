from flask import render_template, request
from flask.views import MethodView
from ..models import Course


class CourseView(MethodView):

    def get(self):

        search = request.args.get('q')

        courses = Course().all(keyword=search)

        return render_template('pages/view-courses.html', courses=courses)
