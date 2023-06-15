from flask import render_template, request, url_for, redirect
from app.questions import bp
from app.models.question import Question
from app.extensions import db
from app.questions.form import QuestionForm

@bp.route('/', methods=('GET', 'POST'))
def index():
    form = QuestionForm()
    questions = Question.query.all()
    
    if request.method == 'POST' and form.validate_on_submit():
        new_question = Question(content=form.content.data,
                                answer=form.answer.data)
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('questions.index'))
    
    return render_template('questions/index.html', questions=questions, form=form)


