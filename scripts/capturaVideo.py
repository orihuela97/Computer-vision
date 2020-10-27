import airsim
from datetime import datetime
import tempfile
import pprint
from cv2 import cv2
import os

'''
Simple script with settings to create a high-resolution camera, and fetching it

Settings used-
{
    "SettingsVersion": 1.2,
    "SimMode": "Multirotor",
    "Vehicles" : {
        "Drone1" : {
            "VehicleType" : "SimpleFlight",
            "AutoCreate" : true,
            "Cameras" : {
                "high_res": {
                    "CaptureSettings" : [
                        {
                            "ImageType" : 0,
                            "Width" : 4320,
                            "Height" : 2160
                        }
                    ],
                    "X": 0.50, "Y": 0.00, "Z": 0.10,
                    "Pitch": 0.0, "Roll": 0.0, "Yaw": 0.0
                },
                "low_res": {
                    "CaptureSettings" : [
                        {
                            "ImageType" : 0,
                            "Width" : 256,
                            "Height" : 144
                        }
                    ],
                    "X": 0.50, "Y": 0.00, "Z": 0.10,
                    "Pitch": 0.0, "Roll": 0.0, "Yaw": 0.0
                }
            }
        }
    }
}
'''

client = airsim.VehicleClient()
client.confirmConnection()
framecounter = 1
prevtimestamp = datetime.now()
tmp_dir = os.path.join(tempfile.gettempdir(), "airsim_drone")
print ("Saving images to %s" % tmp_dir)
try:
    
    os.makedirs(os.path.join(tmp_dir, "DataSet"))
   

except OSError:
    if not os.path.isdir(tmp_dir):
        raise
while(framecounter <= 500):
    """if framecounter%150 == 0:
        responses = client.simGetImages([airsim.ImageRequest("high_res", airsim.ImageType.Scene)])

        for i, response in enumerate(responses):
            
            print("Type %d, size %d, pos %s" % (response.image_type, len(response.image_data_uint8), pprint.pformat(response.camera_position)))
            airsim.write_file(os.path.normpath(os.path.join(tmp_dir, "DataSet",  str(framecounter) + '.png')), response.image_data_uint8)

        
        print("High resolution image captured.")

    if framecounter%30 == 0:
        now = datetime.now()
        print(f"Time spent for 30 frames: {now-prevtimestamp}")
        prevtimestamp = now"""
   
    responses = client.simGetImages([airsim.ImageRequest("front_left_custom", airsim.ImageType.Scene)])

    for i, response in enumerate(responses):
            
        print("Type %d, size %d, pos %s" % (response.image_type, len(response.image_data_uint8), pprint.pformat(response.camera_position)))
        airsim.write_file(os.path.normpath(os.path.join(tmp_dir, "DataSet",  str(framecounter) + '.png')), response.image_data_uint8)


    framecounter += 1
