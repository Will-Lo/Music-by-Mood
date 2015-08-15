en = pyen.Pyen("PM7SRY6GGZNM4QNTG")
en.trace = False

def wait_for_analysis(id):
    while True:
        response = en.get('track/profile', id=id, bucket=['audio_summary'])
        if response['track']['status'] <> 'pending':
            break
        time.sleep(1)

    list = []

    for k,v in response['track']['audio_summary'].items():
        #print "%32.32s %s" % (k, str(v))
        if k == "tempo":
            if v <= 108:
                low.append(id)
                low.append(v)
                low.append(mp3)
                print low
            else:
                high.append(id)
                high.append(v)
                high.append(mp3)
                print high



mp3 = r"C:\Python work\tech retreat\Darude - Sandstorm.mp3"
#type = "mp3"

f = open(mp3, 'rb')
response = en.post('track/upload', track=f, filetype='mp3')
trid = response['track']['id']
print 'track id is', trid
wait_for_analysis(trid)