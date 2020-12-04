import subprocess


def video_stream():
    original = input('Enter the name of the original file in order to get the video (name + .file_type): ')
    container = input('Enter the name of the container you want to add the video (name + .file_type): ')
    command = f"ffmpeg -i {original} -vcodec copy -an {container}"
    subprocess.call(command, shell=True)
    return container

def video_audio_streams():
    original_video = input('Enter the name of the original file in order to get the video (name + .file_type): ')
    video = input('Enter the name of the video output file that will be added to the container (name + '
                  '.file_type): ')
    original_audio = input('Enter the name of the original file in order to get the audio (name + .file_type): ')
    audio = input('Enter the name of the audio output file that will be added to the container (name + '
                  '.file_type): ')
    container = input('Enter the name of the container you want to add the audio + .mp4: ')
    command = f"ffmpeg -i {original_video} -vcodec copy -an {video}"  # mp4 output
    subprocess.call(command, shell=True)
    command = f"ffmpeg -i {original_audio} -ac 1 {audio}"  # aac output
    subprocess.call(command, shell=True)
    command = f"ffmpeg -i {video}  -i {audio} -map 0 -map 1 {container}"  # mp4 output
    subprocess.call(command, shell=True)
    return container


def video_audio_subtitles():
    subtitles = input('Enter the name of the subtitles file (name + .file_type): ')
    out = input('Enter the name of the final container (name + .file_type): ')
    container = video_audio_streams()
    command = f"ffmpeg -i {container}  -f srt -i {subtitles} -c:s mov_text -metadata:s:s:1 language=eng {out}"
    subprocess.call(command, shell=True)
    return out


# create a menu for the user to choose the desired operation
def menu():
    option = input(
        'You are able to add 1 video stream, 1 audio stream and 1 subtitles stream: \n Enter a number to create '
        'container with: \n"1" Only a video stream. \n"2" A video and a mono audio streams. \n"3" A video, mono audio '
        'and subtitles streams '
        'to the container. \n"4" EXIT.')

    if option == "1":
        video_stream()
        print('FINISHED')

    elif option == "2":
        video_audio_streams()
        print('FINISHED')

    elif option == "3":
        video_audio_subtitles()
        print('FINISHED')

    elif option == "4":
        print('EXIT')


menu()
