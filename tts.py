import gtts
# import playsound


def textToSpeech(sentence):
	tts = gtts.gTTS(str(sentence))
	tts.save("response.mp3")



# textToSpeech('''Hello from server, This is a test song
#             The club isn't the best place to find a lover
#             So the bar is where I go
#             Me and my friends at the table doing shots
#             Drinking fast and then we talk slow
#             And you come over and start up a conversation with just me
#             And trust me I'll give it a chance now
#             Take my hand, stop, put Van the Man on the jukebox
#             And then we start to dance, and now I'm singing like
#             Girl, you know I want your love
#             Your love was handmade for somebody like me
#             Come on now, follow my lead
#             I may be crazy, don't mind me
#             Say, boy, let's not talk too much
#             Grab on my waist and put that body on me
#             Come on now, follow my lead
#             Come, come on now, follow my lead
#             I'm in love with the shape of you
#             We push and pull like a magnet do
#             Although my heart is falling too
#             Come on now, follow my lead
#             I may be crazy, don't mind me
#             Say, boy, let's not talk too much
#             Grab on my waist and put that body on me
#             Come on now, follow my lead
#             Come, come on now, follow my lead
#             I'm in love with the shape of you''')
