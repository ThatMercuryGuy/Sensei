from langchain.llms import Ollama
from Transcribe import transcribe
from VoiceRecording import start_recording
'''
filename = start_recording()
transcribe(filename)
'''

llm = Ollama (base_url = 'http://localhost:11434', model = 'mistral')

f = open ('Fri Oct 20 20.30.11 2023.txt', 'r') #filename.replace ('wav', 'txt')

prompt = f'''
I will provide you with the transcript of a recorded lecture.
I would like you to go through the transcript and create detailed notes for the lecture.
timestamps are provided within square brackets at the start of each line.
Make sure you include all important and relevant points.


{f.read()}
'''
f.close()

output = llm(prompt)
print (output)