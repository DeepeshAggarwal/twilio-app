from flask import Flask
from twilio import twiml
from bs4 import BeautifulSoup
import requests as req
import xml.etree.ElementTree as ET
import re

CONSTANT_URL = 'http://static.cricinfo.com/rss/livescores.xml'

app = Flask('Live Cricket Score Feed')

@app.route('/')
def hello():
	return 'Hello world'

@app.route('/sms', methods=['POST'])
def sms():
	try:
		response = req.get(CONSTANT_URL)
		scores = _get_latest_score(response)
	except:
		scores = "Sorry!!! Some problem in Server is going on and i am fixing this."

	response = twiml.Response()
	response.message(scores)
	return str(response)


def _get_latest_score(response):
	root = ET.fromstring(response.text)
	scores = ""
	for item in root.findall('channel')[0].findall('item'):
		score = item.find('title').text
		if re.match('.*[0-9]+.*', score) is not None:
			scores += "\n" + score
	return scores