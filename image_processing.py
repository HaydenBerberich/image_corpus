import os
import cv2

# Process an image
def process_image(image_path, args):
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or unable to read")

        # Convert to grayscale if the flag is set
        if args.grayscale:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Resize the image while preserving the aspect ratio if the flag is set
        if args.aspect:
            h, w = image.shape[:2]
            aspect_ratio = w / h
            if args.cols / aspect_ratio <= args.rows:
                new_w = args.cols
                new_h = int(args.cols / aspect_ratio)
            else:
                new_h = args.rows
                new_w = int(args.rows * aspect_ratio)
            image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
        else:
            # Resize the image to the specified dimensions
            image = cv2.resize(image, (args.cols, args.rows))

        return image
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

# Save an image
def save_image(image, output_path, image_type):
    try:
        if image_type:
            output_path = f"{os.path.splitext(output_path)[0]}.{image_type}"
        cv2.imwrite(output_path, image)
    except Exception as e:
        print(f"Error saving image {output_path}: {e}")