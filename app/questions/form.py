from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class QuestionForm(FlaskForm):
    content = StringField('', [DataRequired()], render_kw={"placeholder": "Content"}, widget=TextArea())
    answer = StringField('', [DataRequired()], render_kw={"placeholder": "Answer"}, widget=TextArea())
    submit = SubmitField('Įvesti')

if __name__ == "__main__":
    pass