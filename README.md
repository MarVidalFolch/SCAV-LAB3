# SCAV-LAB3

## Mar Vidal-Folch Angerri - NIA: 204751

In this lab we have worked with mp4 containers. 

### Exercise 1
---
In this exercise, we have cut the BBB video, created a video strem, a mono audio stream, a low bit rate aduio stream and a subtitles stream. Then, we have packaged everything in a .mp4. To do so, we have created different funtions: to cut the original video, to create the different video and audio tracks, to add subtitles to the mp4 andanother one to pack it all. When calling the different functions, some outputs have been created (video and ausio files) that can be fount in ex1 folder. In the same folder, you can find a screenshot of the terminal after the operation 'ffmpeg -i final_container.mp4' where the different streams are shown. 

### Exercise 2
---
In this exercise, we have automatized the creation of the container so the user can choose between some options:
- Option 1: create a container with only a video stream. This option is equivalent as getting a video and only conserving the video stream.
- Option 2: cretae a container with a video and a mono autout streams. 
- Option 3: create a container with a video, a mono audio and a subtitles streams.

In all options, the user is able to choose the original file from which the streams will be selected, the name of the output streams seperately and the name of the final output container. In the ex2 folder you can find the python script and screenshots showing the terminal outputs for each option. 


### Exercise 3
---
In this exercise, we let the user select any container. Then, for the given container, the python scripts outputs the different broadcasting standards that fit with it. In order to do it, we use ffprobe to get the codec names of the container. Then, we store in different arrays the video and audio codec names. Then, we check if those names are in the different type of brodacasting standards. If so, we append the broadcasting standards in a new array. Finally, we return this array or an ERROR (if it hasn't fitted any). In ex3 folder you can find the script and a screenshot of the results of an example done. 

### Exercise 4
---
The goal of this exercise is to create a python testing script which generates containers to launch against exercise 3. In order to generate them we will use exercise 2. So, to use ex2 and ex3 to implement the script, we have used them as modules and imported them to ex4.py in order to use their functions. Doing so, we have been able to combine the exercises and obtain the desired results. We have done a text and obtained the same result that we had in ex2 and 3. In the ex4 folder you can find the python script implemented. 
### Exercise 5
---
In this exercise we have created a new python script to integrate all previous exercises in a class. 
