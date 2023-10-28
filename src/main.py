from langchain.llms import Ollama
from Transcribe import transcribe
from VoiceRecording import start_recording

def start_application(filename: str):
    transcribe(filename)


    llm = Ollama (base_url = 'http://localhost:11434', model = 'mistral')

    f = open (f'static\{filename}.txt', 'r') 

    prompt = f'''
    I will provide you with the transcript of a recorded lecture.
    I would like you to go through the transcript and create detailed notes for the lecture.
    timestamps are provided within square brackets at the start of each line.
    
    Use numbered points and write every new point on a new line.


    {f.read()}
    '''
    f.close()

    output = llm(prompt)
    output_file = open (f'static\{filename}_NOTES.txt', 'a')

    output_file.write(output)
    output_file.close()