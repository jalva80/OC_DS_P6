# from flask import Flask
from . import utils
from flask import render_template, flash, redirect, url_for
from label_app import app
from label_app.forms import NewMsgForm

# app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NewMsgForm()

    if form.validate_on_submit():
        # pred_label = utils.label_pred(form)
        if pred_tags:
            flash('Catégorie(s) proposée(s): {}'.format(pred_tags))
        else:
            flash('Une erreur s\'est produite... aucun résultat')

    return render_template('predict.html', title='Proposition de catégorie', form=form)

if __name__ == "__main__":
    app.run()
