import pyen
import time

en = pyen.Pyen("PM7SRY6GGZNM4QNTG")
en.trace = False

calm = []
exercise = []

def wait_for_analysis(id):
    while True:
        response = en.get('track/profile', id=id, bucket=['audio_summary'])
        if response['track']['status'] <> 'pending':
            break
        time.sleep(1)

    tempo_speed = response['track']['audio_summary']['tempo']
    loudness = response['track']['audio_summary']['loudness']
    if tempo_speed <= 108 and loudness <= -7:
        calm.append(id)
        calm.append(tempo_speed)
        calm.append(loudness)
        calm.append(mp3)
        #print low
    else:
        exercise.append(id)
        exercise.append(tempo_speed)
        exercise.append(loudness)
        higexercise.append(mp3)
        #print high

mp3 = r"C:\Python work\tech retreat\Darude - Sandstorm.mp3"
#type = "mp3"

f = open(mp3, 'rb')
response = en.post('track/upload', track=f, filetype='mp3')
trid = response['track']['id']
print 'track id is', trid
wait_for_analysis(trid)