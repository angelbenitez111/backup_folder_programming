from moviepy import *
from moviepy.video.io.VideoFileClip import VideoFileClip

video_input = "Gen V - Ya disponible _ Prime Video.mp4"

video_output = "prueba.mp4"


# Cargar el video de entrada
clip = VideoFileClip(video_input)

# Redimensionar el video a 480p (854x480)
resized_clip = clip.resize(height=480)

# Guardar el video redimensionado
resized_clip.write_videofile(video_output, codec="libx264")

# Cerrar el clip original y el clip redimensionado
clip.close()
resized_clip.close()
