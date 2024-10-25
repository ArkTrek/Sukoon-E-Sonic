from moviepy.editor import VideoFileClip, AudioFileClip
import os

def combine_gif_and_audio(gif_path, audio_path, output_path):
    # Load the GIF
    gif_clip = VideoFileClip(gif_path)

    # Load the audio
    audio_clip = AudioFileClip(audio_path)

    # Set the audio to the GIF clip
    video_with_audio = gif_clip.set_audio(audio_clip)

    # Loop the video (optional, depending on how long you want the video)
    duration = audio_clip.duration
    video_with_audio = video_with_audio.loop(duration=duration)

    # Write the output to a file with a codec that supports transparency
    video_with_audio.write_videofile(output_path, codec='libxvid', audio_codec='aac', preset='medium', fps=30)

    # Close the clips
    gif_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    # Define paths for GIF, audio file, and output video
    gif_file = "static/images/sonic-idle.gif"  # Change this to your GIF file path
    audio_file = "static/audio/sonic-theme.mp3"  # Change this to your MP3 file path
    output_file = "static/video/sonic-idle.mp4"  # Change this to your desired output video file path

    # Check if the files exist
    if not os.path.exists(gif_file):
        print(f"GIF file not found: {gif_file}")
    elif not os.path.exists(audio_file):
        print(f"Audio file not found: {audio_file}")
    else:
        # Combine GIF and audio
        combine_gif_and_audio(gif_file, audio_file, output_file)
        print(f"Video created successfully: {output_file}")
