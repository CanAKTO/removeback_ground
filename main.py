from rembg import remove
input_file = "image.jpeg"
output_file = "output.png"

with open(input_file, "rb") as i:
    with open(output_file , "wb") as o :
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)

