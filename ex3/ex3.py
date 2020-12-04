import subprocess


def get_codec_names(video):
    # function that returns the codec names of the input container
    command = f"ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 {video}"
    codec_name = subprocess.check_output(command, shell=True)
    return codec_name


def split_video_audio(container):
    x = get_codec_names(container)  # get video codec and audio codec of the container
    print('codecs names of the container: ', x)  # print the codec names
    codecs = x.splitlines()  # separate the video and the audio codec names in different strings
    video_codec = codecs[0]  # save video codec name in an array
    audio_codec = codecs[1]  # save audio codec name in an array
    return video_codec, audio_codec


def find_b_standard(video_codec, audio_codec):
    # define the different broadcasting standards following the lecture notes
    DVB_video = [b'mpeg2video', b'h264']
    DVB_audio = [b'aac', b'ac3', b'mp3']
    ISDB_video = [b'mpeg2video', b'h264']
    ISDB_audio = [b'aac']
    ATSC_video = [b'mpeg2video', b'h264']
    ASTC_audio = [b'ac3']
    DTMB_video = [b'avs', b'avs+', b'mpeg2video', b'h264']
    DTMB_audio = [b'dra', b'aac', b'ac3', b'mp2', b'mp3']
    broadcasting_standards = []  # init array where to store broadcasting standards that fit
    # check if the video and audio codecs are in each broadcasting standard and, if so, append it to the array
    if video_codec in DVB_video and audio_codec in DVB_audio:
        broadcasting_standards.append('DVB')
    if video_codec in ISDB_video and audio_codec in ISDB_audio:
        broadcasting_standards.append('ISDB')
    if video_codec in ATSC_video and audio_codec in ASTC_audio:
        broadcasting_standards.append('ATSC')
    if video_codec in DTMB_video and audio_codec in DTMB_audio:
        broadcasting_standards.append('DTMB')
    else:
        broadcasting_standards.append("ERROR: it doesn't fit any broadcasting example")

    return broadcasting_standards  # return the array with all possible broadcasting standards


container = input('Enter the name of the container you want to fit into a broadcasting standards: ')  # let the user
# select the container

video_codec, audio_codec = split_video_audio(container)  # split the video and audio codecs in different arrays

brod_standards_array = find_b_standard(video_codec, audio_codec)  # find the broadcasting standards that fit
print('The container fits in the following broadcasting standards: ', brod_standards_array)  # print the result
