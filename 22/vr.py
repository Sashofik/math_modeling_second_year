from PIL import Image, ImageDraw

# Create an image
im = Image.new("RGB", (200,200), "white")

# Create a draw object
draw = ImageDraw.Draw(im)

# Define the color stops
color_stops = [(0, (255, 0, 0)), (0.5, (0, 255, 0)), (1, (0, 0, 255))]

# Draw the pie slice
for i, color_stop in enumerate(color_stops):
    if i == 0:
        start = 0
    else:
        start = color_stops[i-1][0]
    end = color_stop[0]
    draw.pieslice([50, 50, 150, 150], start*360, end*360, fill=color_stop[1])

# Show the image
im.show()
print("Circular gradient created")