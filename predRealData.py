import os
import tqdm

image_folder_path=f"/home/guilherme/Documents/SEE-Dataset/SEE-Real-Data/multi-view/imgs_filter/"
image_folder_output=f"/home/guilherme/Documents/SEE-Dataset/SEE-Real-Data/multi-view/imgs_combined_multiview/"

model=f"/media/guilherme/SSD/unet-data/SEE-Combined-Data/checkpoints/combined_withbase.pth"

if not os.path.isdir(image_folder_path):
    print(f"Error: The folder at '{image_folder_path}' does not exist.")
else:
    #Loop through each file and subfolder in the directory
    #print(f"Reading files from: {folder_path}\n")
    for filename in tqdm.tqdm(os.listdir(image_folder_path)):

        # filename_parse=parts = filename.split('-')
        # #print(filename_parse)
        # mission=filename_parse[0]
        # auv=filename_parse[2]
        # img=filename_parse[3]
        # if int(auv) in objs:
        
        #     try:
        #         os.mkdir(f"{folder_name}/{mission}-{auv}/")
        #     except:
        #         passimage_folder_output
        
            output_path=f"{image_folder_output}{filename}"
            file_path = os.path.join(image_folder_path, filename)

            comand=f"python3 predict.py -m {model} -c 20 --i {file_path} --o {output_path}"
            os.system(comand)