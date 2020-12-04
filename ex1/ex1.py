import subprocess


# function to cut the video
def cut_video_1min(video, output):
    command = f"ffmpeg -ss 00:00:0.0 -i {video} -c copy -t 00:01:00.0 {output}"
    subprocess.call(command, shell=True)


cut_video_1min('BBB.mp4', 'video.mp4')


# create the different tracks that the container will have
def create_tracks(video, vid_1min, audio_mono, audio_low_rate):
    # video: first minute without audio
    command = f"ffmpeg -i {video} -vcodec copy -an {vid_1min}"  # mp4 output
    subprocess.call(command, shell=True)
    # audio: first audio minute in mono track
    command = f"ffmpeg -i {video} -ac 1 {audio_mono}"  # aac output
    subprocess.call(command, shell=True)
    # audio: first audio minute in lowe rate
    command = f"ffmpeg -i {video} -codec:a libmp3lame -b:a 64k {audio_low_rate}"  # aac
    # output setting bit rate to 64 kbits/s
    subprocess.call(command, shell=True)


create_tracks('video.mp4', 'vid_1min.mp4', 'audio_mono.aac', 'audio_low_rate.ac3')


# create a function to add the subtitles to the mp4 container
def add_subtitles(input, subtitles, out):
    command = f"ffmpeg -i {input}  -f srt -i {subtitles} -c:s mov_text -metadata:s:s:1 language=eng {out}"  # mp4 output
    subprocess.call(command, shell=True)


# pack the different streams
def pack_container(vid_1min, audio_mono, audio_low_rate, output_container, BBBsubtitles, final_container):
    command = f"ffmpeg -i {vid_1min}  -i {audio_mono} -i {audio_low_rate}   -map 0 -map 1 -map 2 {output_container}"  # mp4 output
    subprocess.call(command, shell=True)
    add_subtitles(output_container, BBBsubtitles, final_container)


pack_container('vid_1min.mp4', 'audio_mono.aac', 'audio_low_rate.ac3', 'output_container.mp4', 'BBBsubtitles.srt',
               'final_container.mp4')
