import wave

def get_audio_length(file_path):
   with wave.open(file_path, 'r') as audio_file:
      frame_rate = audio_file.getframerate()
      n_frames = audio_file.getnframes()
      duration = n_frames / float(frame_rate)
      return duration
   
def get_annotation_ratios(file_path):
    audio_length = get_audio_length(file_path[:-8] + '.wav')
    with open(file_path, 'r') as annotation_file:
       

    #Sample Annotation File:
    #(0)[5.00s] This is a test
    #(1)[10.00s] This is another test
    #which spans multiple lines
    #(2)[15.00s] This is a third test

        annotations = annotation_file.readlines()
        annotation_ratios = []
        for annotation in annotations:
            if annotation.find('[') == -1:
                continue
            annotation_ratio = float(annotation[annotation.find('[') + 
            1:annotation.find(']') - 1]) / audio_length
            annotation_ratios.append(annotation_ratio)
        return annotation_ratios
    

        
        