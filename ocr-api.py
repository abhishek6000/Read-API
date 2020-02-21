import http.client, urllib.request, urllib.parse, urllib.error, base64, json
SUBSCRIPTION_KEY = '<key here>'
ENDPOINT = '<name here>.cognitiveservices.azure.com'

# Change this to other images
IMAGE_URL = '<URL here>'

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


ocrResult = json.loads(data)
print(ocrResult)
#for line in ocrResult['recognitionResults'][0]['lines']:
 #   print(line['text'])