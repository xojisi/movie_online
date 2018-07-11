#coding:utf8
__author__ = 'xojisi'

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin

class LoginForm(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label = "帐号",
        validators = [DataRequired("请输入帐号!")],
        description = "帐号",
        render_kw = {
            "class" : "form-control",
            "placeholder" : "请输入帐号!",
            # "required" : "required"
        }
    )
    pwd = PasswordField(
        label = "密码",
        validators = [DataRequired("请输入密码!")],
        description = "密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!",
            # "required": "required"
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    def validate_account(self, field):
        account = field.date
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("帐号不存在")

class TagForm(FlaskForm):
    name = StringField(
        laber = "名称",
        validators = [DataRequired("请输入标签！")],
        description = "标签",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称！"
        }
    )
    submit = SubmitField(
        "添加",
        render_kw={
            "class": "btn btn-primary",
        }
    )