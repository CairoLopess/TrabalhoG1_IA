import google.generativeai as genai
import time
import tempfile
import os


api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

def upload_video(file_path):
    
    print(f"Uploading file...")
    video_file = genai.upload_file(path=file_path)
    print(f"Completed upload: {video_file.uri}")
    return video_file

def check_video_state(video_file):

    while video_file.state.name == "PROCESSING":
        print('.', end='')
        time.sleep(10)
        video_file = genai.get_file(video_file.name)
    return video_file

def process_video(uploaded_video, prompt):

    # Cria um arquivo temporário
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
        tmp_file.write(uploaded_video.read())  # Escreve o conteúdo do vídeo no arquivo temporário
        tmp_file_path = tmp_file.name

    try:
        video_file = upload_video(tmp_file_path)
        video_file = check_video_state(video_file)
        
        if video_file.state.name == "FAILED":
            raise ValueError(f"Video processing failed: {video_file.state.name}")
        
        response = model.generate_content([prompt, video_file],request_options={"timeout": 600})

        return response.text

    finally:
        os.remove(tmp_file_path)
