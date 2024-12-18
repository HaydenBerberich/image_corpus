import argparse

# Parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Process images for an image corpus.')
    parser.add_argument('-a', '--aspect', action='store_true', help='Preserve aspect ratio')
    parser.add_argument('-g', '--grayscale', action='store_true', help='Save as grayscale')
    parser.add_argument('-r', '--rows', type=int, default=480, help='Number of rows in output image')
    parser.add_argument('-c', '--cols', type=int, default=640, help='Number of columns in output image')
    parser.add_argument('-t', '--type', choices=['jpg', 'tif', 'bmp', 'png'], help='Output image type')
    parser.add_argument('indir', type=str, help='Input directory')
    parser.add_argument('outdir', type=str, nargs='?', default=None, help='Output directory')
    return parser.parse_args()