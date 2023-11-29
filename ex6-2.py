import json
import zipfile
import tkinter as tk

with zipfile.ZipFile("kabeposter.zip", 'r') as zip_file:
    with zip_file.open('kabeposter/kabeposter_000000000000_keypoints.json', 'r') as f:
        kabeposter_data = json.load(f)

root = tk.Tk()
root.title("Image")
canvas = tk.Canvas(root, width=1400, height=1300)
canvas.pack()        
        
for person_idx in range(2): 
    person_keypoints = kabeposter_data['people'][person_idx]['pose_keypoints_2d']
    
    right_shoulder_x = person_keypoints[6]
    right_shoulder_y = person_keypoints[7]
    
    left_shoulder_x = person_keypoints[15]
    left_shoulder_y = person_keypoints[16]

    neck_x = person_keypoints[3]
    neck_y = person_keypoints[4]    

    right_shoulder_line = canvas.create_line(right_shoulder_x, right_shoulder_y, neck_x, neck_y, fill="red", width=2)
    left_shoulder_line = canvas.create_line(left_shoulder_x, left_shoulder_y, neck_x, neck_y, fill="blue", width=2)

root.mainloop()


