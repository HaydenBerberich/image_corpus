import os
import datetime

# Save metadata to a text file
def save_metadata(metadata, output_dir):
    try:
        with open(os.path.join(output_dir, "metadata.txt"), "w") as f:
            # Print the header
            print(
                f"{'Filename':<20} {'Path':<65} {'Rows':<10} {'Cols':<10} {'Type':<10} "
                f"{'Date of Acquisition':<20} {'Modality of Acquisition':<25} "
                f"{'Copyright Owner':<20} {'Image Annotation':<30} {'Source':<10}",
                file=f
            )
            
            today = datetime.date.today().strftime("%Y-%m-%d")
            metadata_sorted = sorted(metadata, key=lambda x: x['filename'])
            
            # Print each metadata entry
            for data in metadata_sorted:
                print(
                    f"{data['filename']:<20} {data['path']:<65} {data['rows']:<10} "
                    f"{data['cols']:<10} {data['type']:<10} {today:<20} {'Camera':<25} ",
                    file=f
                )
    except Exception as e:
        print(f"Error saving metadata: {e}")