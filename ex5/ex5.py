import subprocess


class LAB3:

    def ex2(self):
        def video_stream():
            original = input('Enter the name of the original file in order to get the video (name + .file_type): ')
            container = input('Enter the name of the container you want to add the video (name + .file_type): ')
            command = f"ffmpeg -i {original} -vcodec copy -an {container}"
            subprocess.call(command, shell=True)
            return container

        def video_audio_streams():
            original_video = input(
                'Enter the name of the original file in order to get the video (name + .file_type): ')
            video = input('Enter the name of the video output file that will be added to the container (name + '
                          '.file_type): ')
            original_audio = input(
                'Enter the name of the original file in order to get the audio (name + .file_type): ')
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

        def menu():
            option = input(
                'You are able to add 1 video stream, 1 audio stream and 1 subtitles stream: \n Enter a number to create '
                'container with: \n"1" Only a video stream. \n"2" A video and a mono audio streams. \n"3" A video, '
                'mono audio '
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

    def ex3(self):
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

        container = input(
            'Enter the name of the container you want to fit into a broadcasting standards: ')  # let the user
        # select the container

        video_codec, audio_codec = split_video_audio(container)  # split the video and audio codecs in different arrays

        brod_standards_array = find_b_standard(video_codec, audio_codec)  # find the broadcasting standards that fit
        print('The container fits in the following broadcasting standards: ', brod_standards_array)  # print the result


LAB3 = LAB3()


class LAB3:
    option = input('Select the exercise you want to perform: \n"2" for exercise 2 \n"3" for exercise 3\nYou option: ')
    if option == "2":
        LAB3.ex2()
        print('FINISHED')

    elif option == "3":
        LAB3.ex3()
        print('FINISHED')
