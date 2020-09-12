from flask import redirect, render_template, url_for, request
from flask_login import login_required

from . import courses
from .forms import MultipleChoiceQuizForm

"""
QUESTION_TOPICS = (
    "tstc", # Cancer testicular
    "crvu", # Cancer cervicouterino
    "plmn", # Cancer en pulmon
    "psta", # Cancer en prostata
    "mama", # Cancer de mama
    "diag"  # Examen diagnostico
)
"""

@courses.route("/diagnostico", methods=["GET", "POST"])
@login_required
def diagnostico():
    form = MultipleChoiceQuizForm.generate_random_quiz("diag", 10)
    if form.validate_on_submit():

    return render_template("courses/diagnostico.html", form=form)

@courses.route("/cancer-testicular", methods=["GET", "POST"])
@login_required
def cancer_testicular():
    form = MultipleChoiceQuizForm.generate_random_quiz("tstc", 3)
    return render_template("courses/cancer_testicular.html", form=form)

@courses.route("/cancer-prostata", methods=["GET", "POST"])
@login_required
def cancer_prostata():
    form = MultipleChoiceQuizForm.generate_random_quiz("psta", 3)
    return render_template("courses/cancer_prostata.html", form=form)

@courses.route("/cancer-pulmon", methods=["GET", "POST"])
@login_required
def cancer_pulmon():
    form = MultipleChoiceQuizForm.generate_random_quiz("plmn", 3)
    return render_template("courses/cancer_pulmon.html", form=form)

@courses.route("/cancer-mama", methods=["GET", "POST"])
@login_required
def cancer_mama():
    form = MultipleChoiceQuizForm.generate_random_quiz("mama", 3)
    return render_template("courses/cancer_mama.html", form=form)

@courses.route("/cancer-cervicouterino", methods=["GET", "POST"])
@login_required
def cancer_cervicouterino():
    form = MultipleChoiceQuizForm.generate_random_quiz("crvu", 3)
    return render_template("courses/cancer_cervicouterino.html", form=form)