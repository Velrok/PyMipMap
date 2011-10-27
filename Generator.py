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
			
			img = input_img.copy()
			img.thumbnail(size, Image.ANTIALIAS)
			img.save(output_dir + "/" + output_filename + "L" + str(level) + "." + output_posfix, output_posfix)
			
			size = ( size[0] / 2, size[1] / 2 )
			level = level + 1
			
		print "done"
	
	


