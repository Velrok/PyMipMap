import sys
import Generator
import os
import getopt

def usage():
	print """
Usage: PyMipMap [OPTIONS]
  -h --help                   Prints this help.
  
  -i <input_image>            REQUIRED
  -d <output_dir>             uses working dir as default value
  -o <output_image_prefix>    REQUIRED filename base of the output image
  -f <output_postfix>         example: png jpg default: png
	
  -m --max-depth <i>          Stops after creating i images.
  -s --stop-at-size <size>    Stops if the image whould have a smaller dimention 
                              than <size>. Default is 16.
	
  -t --tile-size <tile_size>  If this value is set, all generated images will be 
                              croped into tiles of (tile_size x tile_size).
"""

def main(argv):
	try:                                
		opts, args = getopt.getopt(argv, "hm:s:t:i:d:o:f:", ["help", "max-depth=", "stop-at-size=", "tile-size="])
		
		# set default parameters
		input_image = None
		output_dir = os.getcwd()
		output_image_prefix = None
		output_postfix = "png"
		
		max_depth = None
		stop_size = 16
		tile_size = None
		
		for opt, arg in opts:
			if(opt in ("-h", "--help")):
				usage()
				sys.exit()
			if(opt in ("-m", "--max-depth")):
				max_depth = int(arg)
			if(opt in ("-s", "--stop-at-size")):
				stop_size = arg
			if(opt in ("-t", "--tile-size")):
				tile_size = arg
			if(opt in ("-i")):
				input_image = arg
			if(opt in ("-d")):
				output_dir = arg
			if(opt in ("-o")):
				output_image_prefix = arg
			if(opt in ("-f")):
				output_postfix = arg
		
		if not input_image:
			print 'input image required'
			usage()
			sys.exit(2)
			
		if not output_image_prefix:
			print 'output image prefix required'
			usage()
			sys.exit(2)
			
		g = Generator.Generator(input_image)
		g.set_stop_size(stop_size)
		
		if(max_depth):
			g.max_depth = int(max_depth)
			
		if(tile_size):
			g.tile_size = int(tile_size)
			
		g.generate( output_dir, output_image_prefix, output_postfix )
		
	except getopt.GetoptError:
		usage()
		sys.exit(2)


if __name__ == "__main__":
	main(sys.argv[1:])