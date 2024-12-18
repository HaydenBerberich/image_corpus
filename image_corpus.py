# Hayden Berberich
# 9-14-2024

import os
from arguments import parse_arguments
from image_processing import process_image, save_image
from metadata import save_metadata

# Main function to process images
def main():
    # Parse command line arguments
    args = parse_arguments()
    if args.indir.endswith('/'):
        args.indir = args.indir[:-1]
    
    if not args.outdir:
        args.outdir = f"{args.indir}.corpus"
    os.makedirs(args.outdir, exist_ok=True)
    
    metadata = []
    # Process each image in the input directory
    for root, _, files in os.walk(args.indir):
        for file in files:
            image_path = os.path.join(root, file)
            image = process_image(image_path, args)
            if image is not None:
                output_path = os.path.join(args.outdir, file)
                save_image(image, output_path, args.type)
                metadata.append({
                    "filename": file,
                    "path": image_path, 
                    "rows": args.rows,
                    "cols": args.cols,
                    "type": args.type if args.type else os.path.splitext(file)[1][1:]
                })
    save_metadata(metadata, args.outdir)

if __name__ == "__main__":
    main()