from wtforms import Form, TextField, PasswordField, validators


class DeployForm(Form):
    # XXX ref was a unicode str, which later was causing issues in werkzueg
    # at:
    # https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/serving.py#L131
    # Too bad we aren't using python 3 :(
    ref = TextField('git ref',[validators.Required()], filters=(lambda s: str(s),))
    password = PasswordField('secret', [validators.Required()])
    who = TextField('identify yourself', [validators.Required()])

class LoadtestForm(Form):
    repo = TextField('git repo', [validators.Required()])
