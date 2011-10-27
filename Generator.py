import Image

class Generator(object):
	"""
	A generator class.
	That comes with required and optional parameter.
	"""
	def __init__(self, input_filename):
		self.input_filename = input_filename
		self.stop_size = (16, 16)
		self.max_depth = None
		self.tile_size = None
	
	
	def should_create_tiles(self):
		return (not self.tile_size is None)
	
		
	def has_max_depth(self):
		return (not self.max_depth is None)
	
	
	def set_stop_size(self, size):
		"""
		For your convenience. Sets the two dimentional stop size 
		to the single value provided. Also ensured int type.
		"""
		self.stop_size = int(size), int(size)
	
		
	def generate(self, output_dir, output_filename, output_posfix):
		input_img = Image.open(self.input_filename)
		
		if(not input_img):
			raise "can't load image: " + self.input_filename
			
		print "loading input image DONE"
			
		# ensure correct type
		self.stop_size = ( int(self.stop_size[0]), int(self.stop_size[1]) )
		
		size = input_img.size
		level = 0
		
		print "generating mip maps for " + str(self.input_filename)
		print "into output directory " + str(output_dir)
		print "image info: ", input_img.format, size, input_img.mode
		print "will stop at size ", self.stop_size
		
		while(size >= self.stop_size):
			if(self.has_max_depth() and level >= self.max_depth):
				# skipp loop as soon as we mit the max depth
				break
			
			print size
			
			print "creating thumbnail"
			input_img.thumbnail(size, Image.ANTIALIAS)
			print "creating thumbnail DONE"
			
			save_as = str(output_dir + "/" + output_filename + "L" + str(level))
			file_extention = str("." + output_posfix)
			
			tile_cound = 0
			if(self.should_create_tiles()):
				print "save thumbnail as tiles"
				# create tiles
				
				total_tile_count = (size[1] / float(self.tile_size)) * (size[0] / float(self.tile_size))
				
				yi = 0
				for y in range(0, size[1], self.tile_size):
					xi = 0
					for x in range(0, size[0], self.tile_size):
						box = (x, y, x + self.tile_size, y + self.tile_size)
						
						# print "creating tail " + str(tile_cound)
						tile_image = input_img.crop(box)
						# print "creating tail " + str(tile_cound) + " DONE"
						
						filename = save_as + "T" + str(yi) + "_" + str(xi) + file_extention
						tile_image.save(filename, output_posfix)
						
						progress = (float(tile_cound) / float(total_tile_count)) * 100
						print filename + " SAVED " + str(int(progress)) + " % level progress"
						
						del tile_image
						
						tile_cound = tile_cound + 1
						xi = xi + 1
					yi = yi + 1
			else:
				# we don't need to create tiles so just save this new mipmap level
				input_img.save(save_as + file_extention, output_posfix)
			
			size = ( size[0] / 2, size[1] / 2 )
			level = level + 1
			print "----------- next mipmap level -----------"
			
		print "done"
	
	


