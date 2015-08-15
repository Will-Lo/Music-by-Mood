import pyen
import time


en = pyen.Pyen("PM7SRY6GGZNM4QNTG")
en.trace = False

def wait_for_analysis(id):
    while True:
        response = en.get('track/profile', id=id, bucket=['audio_summary'])
        if response['track']['status'] <> 'pending':
            break
        time.sleep(1)

    for k,v in response['track']['audio_summary'].items():
        print "%32.32s %s" % (k, str(v))




#mp3 = "C:\Python work\tech retreat\Darude - Sandstorm.mp3"
#type = "mp3"

f = open("Darude - Sandstorm.mp3", 'rb')
response = en.post('track/upload', track=f, filetype='mp3')
trid = response['track']['id']
print 'track id is', trid
wait_for_analysis(trid)

a=1