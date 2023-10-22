from langchain.llms import Ollama
from Transcribe import transcribe
from VoiceRecording import start_recording

def start_application(filename: str):
    transcribe(filename)


    llm = Ollama (base_url = 'http://localhost:11434', model = 'mistral')

    f = open (f'{filename}.txt', 'r') 
    ua = open (f'{filename}_ANN.txt', 'r') 
    prompt = f'''
    I will provide you with the transcript of a recorded lecture.
    I would like you to go through the transcript and create detailed notes for the lecture.
    timestamps are provided within square brackets at the start of each line.
    The first value provided within the timestamp is the start time.
    The second value provided within the timestamp is the end time.
    Make sure you include all important and relevant points.


    {f.read()}

    Given below is a file containing user-made annotations from the lecture.
    Timestamps for every single annotation is given within square brackets.
    Please include every single one of these annotations in your notes as well,
    between the notes you have already made, such that the time in the timestamp of the
    user annotation is between the start and end time of the line in the transcript
    which you made notes for.

    {ua.read()}
    '''
    f.close()
    ua.close()

    output = llm(prompt)
    output_file = open (f'{filename}_NOTES.txt', 'a')

    output_file.write(output)
    output_file.close()