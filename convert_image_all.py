from PIL import Image
import os

resolutions = [240, 260, 300, 380, 456, 528, 600]
#resolutions = [224, 240, 260, 300, 380, 456, 528, 600]

for res in resolutions:
    #Define source and destination directories
    DATA_SRC = 'data'
    DATA_DST = 'data_' + str(res)

    path = os.walk(DATA_SRC)
    for root, directories, _ in path:
        for directory in directories:
            new_path = os.path.join(DATA_DST,directory)
            os.makedirs(new_path)
            
            

path = os.walk(DATA_SRC)
for root, directories, files in path:
    for file in files:
        input_file = os.path.join(root, file)
        input_dir = os.path.dirname(input_file).split('/')[-1]

        # Read in image
        print('[INFO] Reading {}'.format(input_file))
        img = Image.open(input_file)
        rgb_im = img.convert('RGB')

        for res in resolutions:
            # Form the string to the output directory
            DATA_DST = 'data_' + str(res)
            output_dir = os.path.join(DATA_DST, input_dir)
            output_file = os.path.join(DATA_DST, input_dir, str(res)+'_'+file)


            print('[INFO] Resizing')
            resized_img = rgb_im.resize((res,res))

            print('[INFO] Saving {}'.format(output_file))
            resized_img.save(output_file)
