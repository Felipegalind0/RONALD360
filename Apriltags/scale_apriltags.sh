#!/bin/bash
echo "Welcome to the Apriltag(or any PNG) batch scaling utility."
echo "Enter the path of the input directory:"
read input_dir

output_dir="${input_dir}_900"
echo $output_dir

echo "Creating output directory if it does not exist..."
mkdir -p "$output_dir"

for file in $input_dir/*.png; do
  echo "Converting $file"
  convert "$file" -scale 1000% "$output_dir/$(basename ${file%.*})_900.png"
  echo "Converted image saved as $output_dir/$(basename ${file%.*})_900.png"
done

echo "Conversion complete!"
