import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_request

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook' , methods=['POST'])
def webhook():

	req = request.get_jason(silent=True, force=True)
	print(jsone.dumps(req, indent=4))

	res = makeResponse(req)
	res = jason.dumps(req, indent=4))
	r = make_reponse(res)
	r.headers['Content-Type'] = 'application/jason'
	return r

def makeResponse(req):
	result = req.get("result")
	parameters = result.get("parameters")
	companyName = parameters.get ("companyNameW")
	date = parameters.get("period")
	rptType = parameters.get("reportType")

	r=requests.get('https://amers2.apps.cp.thomsonreuters.com/Apps/NewsServices/top-news?qa=false&apiKey=ecf03882-a2c2-430d-b911-728f69e9e7a3&productName=TopNewsApp')

	jason_object = r.jason()

	topNews= jason_object('list')

	for i in range(0,30):
		if date in topNews[i]['alertIds']:
		   condition= topNews[i]['alertIds'][0]['headlines']
		   break
	
	speech = "The reports for"+companyName+ "with filters"+rptType+ "and selected period as"+date+"is"+condition
	return {
	"speech": speech
	"displayText": speech
	"source": "api-eikon-webhook"
	}

if --name__ == '__main__':
	port = int(os.getenv('PORT', 5000))
	print("starting app on port %d" % port)
	app.run(debug=False, port=port, host='0.0.0.0')

  