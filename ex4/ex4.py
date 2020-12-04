import ex2
import ex3

# generate container using ex2:
container = ex2.menu()

# find broadcasting standard
video_codec, audio_codec = ex3.split_video_audio(container)
brod_standards_array = ex3.find_b_standard(video_codec, audio_codec)
print('The container fits in the following broadcasting standards: ', brod_standards_array)

