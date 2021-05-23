import chat
import speech_recognition as sr 
import pyaudio

def speech():

	sample_rate = 48000
	chunk_size = 2048
	r = sr.Recognizer() 

	#mic_list = sr.Microphone.list_microphone_names() 
	#print(mic_list)
	#for i, microphone_name in enumerate(mic_list): 
	#    if microphone_name == mic_name: 
	#        device_id = i 
	#    print(i, microphone_name)
	#device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size
	with sr.Microphone() as source: 
		r.adjust_for_ambient_noise(source) 
		print ("Say Something")
		
		audio = r.listen(source) 
			
		try:
		        
		        text = r.recognize_google(audio)
			#text=r.recognize_sphinx(audio)
		        print ("you said: " + text )
		        chat.voicechat(text)
		
		
		except sr.UnknownValueError: 
		        print("Google Speech Recognition could not understand audio") 
		
		except sr.RequestError as e: 
		        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
