import os
import tqdm

objs=[12,18,33]

image_mode=f"SEE-Single-View"
folder_name=f"Multiview-SEE"
model=f"/media/guilherme/SSD/unet-data/SEE-Combined-Data/checkpoints/combined_withbase.pth"

#model=f"/media/guilherme/SSD/unet-data/{image_mode}/checkpoints/SideBySideBase.pth"
#model=f"/media/guilherme/SSD/unet-data/{image_mode}/checkpoints/Stacked_withbase.pth"
#model=f"regression.pth"

try:
    os.mkdir(f"{image_mode}")
except:
    pass
#folder_path = f'/media/guilherme/SSD/unet-data/{image_mode}/imgs/'
folder_path = f'/media/guilherme/SSD/unet-data/{image_mode}/imgs/'
file_list=[]

if not os.path.isdir(folder_path):
    print(f"Error: The folder at '{folder_path}' does not exist.")
else:
    #Loop through each file and subfolder in the directory
    print(f"Reading files from: {folder_path}\n")
    for filename in tqdm.tqdm(os.listdir(folder_path)):

        filename_parse=parts = filename.split('-')
        #print(filename_parse)
        mission=filename_parse[0]
        auv=filename_parse[2]
        img=filename_parse[3]
        if int(auv) in objs:
        
            try:
                os.mkdir(f"{folder_name}/{mission}-{auv}/")
            except:
                pass
        
            output_path=f"{folder_name}/{mission}-{auv}/{img}"
            file_path = os.path.join(folder_path, filename)

            comand=f"python3 predict.py -m {model} -c 20 --i {file_path} --o {output_path}"
            os.system(comand)