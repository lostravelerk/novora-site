#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""发送 novora 每日文章发布通知邮件"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 文章信息
title = '你的工厂90%的时间都在等待——价值流图析揭示的精益真相'
filename = '2026-06-17-lean-value-stream'
summary = (
    '从原材料进厂到成品出厂，真正在创造价值的时间可能不到5%。'
    '精益生产不是\u201c省\u201d，而是\u201c看见\u201d'
    '——看见那些吞噬利润的浪费。'
)

# SMTP 配置
SMTP_HOST = 'smtp.exmail.qq.com'
SMTP_PORT = 465
SMTP_USER = 'info@megee.com'
SMTP_PASS = '8joAX7hust7JPzUd'

FROM = 'megeebot <info@megee.com>'
TO = 'megeer@megee.com'

subject = 'megeebot 今日文章：' + title

body = (
    '各位同事好，\n'
    '\n'
    '今日文章已发布：\n'
    '\n'
    '\U0001F4D6《' + title + '》\n'
    '\u2192 https://lostravelerk.github.io/novora-site/articles/'
    + filename + '.html\n'
    '\n'
    + summary + '\n'
    '\n'
    '\u2014 megeebot'
)

# 构建邮件
msg = MIMEText(body, 'plain', 'utf-8')
msg['From'] = FROM
msg['To'] = TO
msg['Subject'] = Header(subject, 'utf-8')

try:
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, [TO], msg.as_string())
    print('SUCCESS: 邮件已发送')
except Exception as e:
    print(f'FAILED: {e}')
    raise
