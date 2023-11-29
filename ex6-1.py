import json
import zipfile

with zipfile.ZipFile("kabeposter.zip", 'r') as zip_file:
    with zip_file.open('kabeposter/kabeposter_000000000000_keypoints.json', 'r') as f:
        kabeposter_data = json.load(f)
        
for person_idx in range(2): 
    person_keypoints = kabeposter_data['people'][person_idx]['pose_keypoints_2d']
    
 
    nose_x = person_keypoints[0]
    nose_y = person_keypoints[1]
    nose_confidence = person_keypoints[2]
    
    
    neck_x = person_keypoints[3]
    neck_y = person_keypoints[4]
    neck_confidence = person_keypoints[5]

    print("No.{} 鼻| X座標:{}, Y座標:{}, 信頼度:{}".format(person_idx+1,nose_x, nose_y, nose_confidence))
    print("No.{} 首| X座標:{}, Y座標:{}, 信頼度:{}".format(person_idx+1,neck_x, neck_y,neck_confidence))
    

