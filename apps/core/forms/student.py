from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

from ..models import Department

departments = Department().all()
print('------------------------------------------')
print('dept')
print(departments)
print('------------------------------------------')


class StudentForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired(), Length(
        min=2, max=20)], render_kw={"class": "form-control form-input"})
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=2, max=20)], render_kw={"class": "form-control form-input"})
    dept_name = SelectField('Department Name', validators=[
                            DataRequired()], choices=departments, render_kw={"class": "form-control form-input"})
