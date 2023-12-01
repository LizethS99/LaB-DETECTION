from PIL import Image

# Converts image to grayscale
inputImage = Image.open("IMD004.bmp").convert('L')   
outputImage = Image.new('L', inputImage.size)

width, height = inputImage.size

# We first need to find the minimum and maximum pixel intensities
minIntensity = 255
maxInsenity = 0

for x in range(width):
    for y in range(height):
        intensity = inputImage.getpixel((x,y))

        minIntensity = min(minIntensity, intensity)
        maxInsenity = max(maxInsenity, intensity)

print("Minimum Pixel Intensity: " + str(minIntensity))
print("Maximum Pixel Intensity: " + str(maxInsenity))

# Now, we'll go through the image again and update all of the pixel values to their new
# position on the scaled histogram
for x in range(width):
    for y in range(height):
        intensity = inputImage.getpixel((x,y))
        
        # This normalization process returns an intensity from 0 - 1 so we need to multiply by 255
        newIntensity = 255 * ((intensity - minIntensity) / (maxInsenity - minIntensity))
        outputImage.putpixel((x,y), int(newIntensity))

outputImage.save('contrastStretched.jpg')
