from PIL import Image
import numpy as np

#read txt file into program
def read(txt_file):
  DNA = ''
  with open(txt_file, 'r') as file:
    DNA = file.readlines()

  temp = ''
  for i in DNA:
    temp += str(i)
  return temp
  
#reading bits from input
def dna_to_bits(dna_in):
  bits = []
  for i in DNA:
    if i == "A" or i == "T":
      bits.append(0)
    elif i == "C" or i == "G":
      bits.append(1)
  return bits
  
#8bits for 0-255, 24bits per pixel
def get_sets(bit_list):
  #8 bit subsets->gets rid of excess
  set = bit_list[:len(bit_list)-(len(bit_list)%8)]
  #turns 8bit subsets into a number then appends them to bit_nums
  bit_nums = []
  for i in range(0, len(set), 8):
    subset = set[i:i+8]
    num = int(''.join([str(i) for i in subset]), 2)
    bit_nums.append(num)
  
  return bit_nums
    
def get_pixels(da_shit):
  #makes da_shit a multiple of 3 (3 8 bit values for RGB)
  da_shit = da_shit[:len(da_shit)-(len(da_shit)%3)]
  pixels = []
  for i in range(0, len(da_shit), 3):
    subset = tuple(da_shit[i:i+3])
    pixels.append(subset)
    
  return pixels

def length_width(pix):
  #find length and width of list 
  #find closest perfect square<---will lose some pixels
  length = len(pix)
  #take sqrt then floor in
  lw = int(np.sqrt(length))
  new_pix = []
  pix = pix[:(length-(length%lw))]
  for i in range(0, len(pix), lw):
    new_pix.append(pix[i:i+lw])
    
  return new_pix
def make_image(pixels, name='new'):
  # Convert the pixels into an array using numpy
  array = np.array(pixels, dtype=np.uint8)
  #print(array)
  # Use PIL to create an image from the new array of pixels
  new_image = Image.fromarray(array)
  new_image.save(f'{name}.bmp')

#finds avg pixel val of all pixels
def avg_pixel_val(pixels):
  avg = lambda x, y: int((x/y)+0.5)
  r, g, b = 0, 0, 0
  length = len(pixels)
  for pixel in pixels:
    r += pixel[0]
    g += pixel[1]
    b += pixel[2]

  return (avg(r, length), avg(g, length), avg(b, length))
  
if __name__ == "__main__":
  
  file_name = input("input text file of DNA values: ")
  DNA = read(file_name)
  bits = dna_to_bits(DNA)
  sets = get_sets(bits)
  pixels = get_pixels(sets)
  make_image(avg_pixel_val(pixels), name='singular')
  #length_width transforms list into 2D list of tuples
  pixels = length_width(pixels)
  make_image(pixels)


