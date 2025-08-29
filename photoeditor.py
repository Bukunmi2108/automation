from PIL import Image, ImageOps

size = (100, 150)

with Image.open("asset/man.jpg") as im:
  """
  Function to reduce the size of an image to a specified size."""
  ImageOps.cover(im, size).save("asset/man_resize.jpg")