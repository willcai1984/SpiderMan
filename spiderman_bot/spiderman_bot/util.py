# -*- coding: utf-8 -*-
# Author:Will
"""
增加工具函数，拓展爬虫功能
"""
import smtplib
import logging
from email.mime.text import MIMEText

# 第三方 SMTP 服务
MAIL_HOST = "smtp.163.com"  # 设置服务器
MAIL_USER = "willcai1984@163.com"  # 用户名
# MAIL_PASSWORD = "cw88205555"  # 口令/授权码
# 授权码cw8205555
MAIL_PASSWORD = "cw8205555"
MAIL_SENDER = 'willcai1984@163.com'
MAIL_PORT = 25
MAIL_MSG_HEADER = '''
<h4>@All:</h4>
<p>勤勤恳恳的小蜘蛛提醒您，有新增招投标记录&nbsp;</p>
<h4 style="color: #2e6c80;">新增招投标记录:</h4>
<table align="center" cellpadding="3" cellspacing="0" style="padding: 1px 1px; border: 1px #ccc solid;">
    <tbody>
        <tr style="height: 28px;" bgcolor="#ACDDEC">
            <th width="30" align="center">ID</th>
            <th width="90" nowrap="nowrap" align="center">地点</th>
            <th width="90" nowrap="nowrap" align="center">来源</th>
            <th align="center">标题</th>
            <th width="120" align="center">发布时间</th>
            <th width="60" align="center">查看</th>
        </tr>'''
MAIL_MSG_FOOTER = '''</tbody></table>'''
MAIL_MSG_ENTRY = '''
        <tr style="height:28px;background-color:%s;">
            <td align="center">%s</td>
            <td nowrap="nowrap" align="center">%s</td>
            <td nowrap="nowrap" align="center">%s</td>
            <td align="left">%s</td>
            <td align="center">%s</td>
            <td align="center"><a href="%s">查看</a></td>
        </tr>
'''


class EmailSend(object):
    def __init__(self):
        self.s = smtplib.SMTP()
        self.s.connect(MAIL_HOST, MAIL_PORT)
        self.s.login(MAIL_USER, MAIL_PASSWORD)
        self.logger = logging.getLogger(__name__)
        self.id = 1

    def __del__(self):
        self.s.close()

    def _entry_process(self, location, src_site, title, pub_date, url):
        if self.id % 2:
            # 奇数行
            entry_msg = MAIL_MSG_ENTRY % ("#ffffff", self.id, location, src_site, title, pub_date, url)
        else:
            # 偶数行
            entry_msg = MAIL_MSG_ENTRY % ("#eeeeee", self.id, location, src_site, title, pub_date, url)
        self.id += 1
        return entry_msg

    def email_send(self, receivers, subject, content_tuple_list):
        msg_entries = []
        for content_tuple in content_tuple_list:
            msg_entries.append(self._entry_process(*content_tuple))
        msg = MAIL_MSG_HEADER + "".join(msg_entries) + MAIL_MSG_FOOTER
        message_send = MIMEText(msg, 'html', 'utf-8')
        message_send['From'] = MAIL_SENDER
        message_send['To'] = ",".join(receivers)
        message_send['Subject'] = subject
        try:
            self.s.sendmail(MAIL_SENDER, receivers, message_send.as_string())
            self.logger.info("Send mail successfully")
            return True
        except Exception as e:
            self.logger.error("Send mail failed", exc_info=True)
            return False
