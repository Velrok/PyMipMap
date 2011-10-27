import sys
import Generator

def usage():
	print """
Usage: PyMipMap [OPTIONS]
	-i <input_image> 						REQUIRED
	-d <output_dir> 						uses working dir as default value
	-o <output_image_prefix>		REQUIRED
	-f <output_postfix>					example: png jpg
	
	--max-depth <i> 				Stops after creating the i'th level.
	--stop-at-size <size>		Stops if the image whould have a smaller dimention than <size>.
"""

def main(argv):
	Generator.generate("/Users/velrok/Desktop/chess-board-27f0cf.jpg", "/Users/velrok/Desktop/output", "chess", "png")
	# try:                                
	# 	opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
	# except getopt.GetoptError:
	# 	usage()
	# 	sys.exit(2)


if __name__ == "__main__":
	main(sys.argv[1:])