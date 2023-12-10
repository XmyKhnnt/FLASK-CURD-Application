
from flask import Blueprint
from . import controllers

main = Blueprint('main', __name__)


main.add_url_rule('/', view_func=controllers.Index.as_view('index'))
main.add_url_rule(
    '/students', view_func=controllers.ViewStudent.as_view('students'))
main.add_url_rule(
    '/students/details', view_func=controllers.ViewStudentsDetails.as_view('students-details'))
main.add_url_rule(
    '/courses', view_func=controllers.CourseView.as_view('courses'))
main.add_url_rule(
    '/fails', view_func=controllers.StFailsView.as_view('fails'))
