from utils.news import MyNews
from utils.sendemail import MorningMail
from utils.finance import Finance
from utils.currency import FixerFX

import logging

import utils.config as config

logging.basicConfig(level=logging.INFO)

logging.info("Start compose html email...")

html_content = "<p>Good Morning, </p>"

logging.info("adding FX to html...")

fixerFX = FixerFX()
html_content += fixerFX.get_html_result()

logging.info("adding Stock Indexes to html...")
finance = Finance()
html_content += finance.get_formatted_html()

logging.info("adding News to html...")
news = MyNews()
html_content += news.get_news_by_top()

logging.info("Start to send email...")
to_emails = config.EMAIL_ADDRESSES
subject = "Morning Greeting!"
mail = MorningMail(to_emails=to_emails,subject=subject, html_content=html_content)
mail.sendMorningMail()