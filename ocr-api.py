import http.client, urllib.request, urllib.parse, urllib.error, base64, json

# These are my credentials
SUBSCRIPTION_KEY = '<key here>'
ENDPOINT = '<name here>.cognitiveservices.azure.com'

# Change this to other images
IMAGE_URL = 'https://www.elearnmarkets.com/blog/wp-content/uploads/2016/01/Bearer-cheque-1024x460.jpg'

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
}

params = urllib.parse.urlencode({
})

opLocation = None
try:
    conn = http.client.HTTPSConnection(ENDPOINT)
    conn.request(
        "POST", 
        "/vision/v2.0/read/core/asyncBatchAnalyze?%s" % params, 
        str({
            "url":IMAGE_URL
        }), 
        headers
    )
    response = conn.getresponse()
    opLocation = response.headers["Operation-Location"]
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

if opLocation:
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    }

    params = urllib.parse.urlencode({})

    try:
        conn = http.client.HTTPSConnection(ENDPOINT)
        conn.request("GET", "/vision/v2.0/read/operations/{0}?{1}".format(opLocation.rsplit('/',1)[-1],params), "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

ocrResult = json.loads(data)
print(ocrResult)
# You have to precess ocrResult from here on. Here, I print all the lines 
#for line in ocrResult['recognitionResults'][0]['lines']:
 #   print(line['text'])