# Veg_Biryani
Obstacle Detection and Dynamic Path Planning for Autonomous Off Road Navigation

**#Heatmap bumpy stitched.mp4**

We stitched together around 180 images to get a heatmap of our bumpy road simulation. The composed video shows the bumpiness the vehicle encounters. The orange denotes rough terrain, blue is the sky

**#Dashcam bumpy.mp4**

Video from the MAVS simulator showing a bumpy terrain

**#Heatmap forest stitched.mp4**

We stitched together images to get a heatmap of our forest environment simulation. The composed video shows the various obstacles' the vehicle encounters. The orange denotes rough terrain, blue is the sky, light green is heavy vegetation, dark green is light vegetation and yellow is the smoother terrain

**#Dashcam forest.mp4**

Video from the MAVS simulator showing a forest environment

**#Heatmap city stitched.mp4**

We stitched together images to get a heatmap of our city environment simulation. The composed video shows a relatively dark scene implying that the roads are well defined and hence no obstacles are detected

**#Dashcam city.mp4**

Video from the MAVS simulator showing a city environment

**#00719_top_lidar.pts**

Lidar output from the MAVS simulator. Output is provided in the x y z r g b format. This is an output from only 1 frame of the video. So considerable amount of data can be obtained from relatively short time.

**#RL_Testcode.py**

So we tried to pre process the heat map image and get the program to detect the yellow path which is the best route, free from most rough terrain. We still quite haven't reached the RL part of the code but we are looking at using PPO (Proximal Policy Optimization) model. We are attching the outputs obtained till now. But the pre processing is not working right

![WhatsApp Image 2024-04-20 at 03 43 36](https://github.com/Anuzzzzzzz/Veg_Biryani/assets/148976244/262187a6-6b54-4ec2-91fa-628bfe6c4cf0)

![WhatsApp Image 2024-04-20 at 03 43 45](https://github.com/Anuzzzzzzz/Veg_Biryani/assets/148976244/d5f6e38b-54ad-4a05-b64f-912b6b612623)

![WhatsApp Image 2024-04-20 at 07 10 31](https://github.com/Anuzzzzzzz/Veg_Biryani/assets/148976244/c348450c-416b-4e7f-95b4-c4d0882206d9)


