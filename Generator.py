import Image

def generate(input_image_filename, output_dir, output_filename, output_posfix):
	input_img = Image.open(input_image_filename)
	if(not input_img):
		raise "can't load image: " + input_image_filename
		
	size = input_img.size
	level = 0
	
	while(size > (8,8)):
		img = input_img.copy()
		img.thumbnail(size, Image.ANTIALIAS)
		img.save(output_dir + "/" + output_filename + "L" + str(level) + "." + output_posfix, output_posfix)
		
		size = size[0] / 2, size[1] / 2
		level = level + 1
		
		print size
		
	pass
