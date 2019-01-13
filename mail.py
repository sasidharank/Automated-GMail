import yagmail

yagmail.register('yourmail', 'yourpassword')  #only for first time

yag = yagmail.SMTP('yourmail')
to = 'tosomeone@abc.com'
subject = 'This is subject'
body = 'Your Body'
html = 'html codes here'
yag.send(to=to, subject=subject, contents=[body, html])



