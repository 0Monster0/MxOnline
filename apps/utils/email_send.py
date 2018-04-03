# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 23:19
# @File    : email_send.py
import random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = generate_random_str(16)
    if send_type == 'update_email':
        code = generate_random_num(4)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = '慕学在线网注册激活链接'
        # http://118.89.105.65 是我自己的服务器 IP 地址，你部署的时候，请换成你自己的 IP 或 域名
        email_body = '请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            # TODO
            pass

    elif send_type == 'forget':
        email_title = '慕学在线网密码重置链接'
        email_body = '请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            # TODO 提示发送成功
            pass

    elif send_type == 'update_email':
        email_title = '慕学在线邮箱修改验证码'
        email_body = '你的邮箱验证码为：{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            # TODO 提示发送成功
            pass


def generate_random_str(random_length=8):
    str = ''
    chars = [chr(x) for x in range(65, 91)] + [chr(y) for y in range(97, 123)] + [chr(z) for z in range(48-58)]
    length = len(chars) - 1
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


def generate_random_num(random_length=8):
    str = ''
    chars = [chr(x) for x in range(48, 58)]
    for i in range(random_length):
        str += chars[random.randint(0, 9)]
    return str
