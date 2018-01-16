from flask_wtf import Form
from flask_wtf.recaptcha import validators
from wtforms import TextField, PasswordField, StringField, SubmitField, FileField, HiddenField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    submit = SubmitField('Login')


class NewCampaignForm(Form):
    product = StringField('Product', validators=[DataRequired(), Length(max=40)])
    campaign_name = StringField('Campaign', validators=[DataRequired(), Length(max=40)])
    campaign_file = FileField('Audio/Video File', validators=[DataRequired(), Length(max=40)])
    submit = SubmitField('Create New Campaign')


class EditCampaignDetail(Form):
    campaign_id = HiddenField('Campaign ID')
    station_id = HiddenField('Station ID')
    schedule_dates = HiddenField("Schedule Dates")
    submit = SubmitField('Edit Campaign')


class AddCampaignDetail(Form):
    add_campaign_id = HiddenField('Campaign ID')
    add_station_id = SelectField('Select Station')
    add_schedule_dates = HiddenField("Schedule Dates")
    add_submit = SubmitField('Add Schedule')


class ForgotForm(Form):
    email = StringField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
