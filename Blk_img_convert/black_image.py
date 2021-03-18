from PIL import Image
img = Image.open('D:\Python mini projects\Blk_img_convert\profile_dp.jpeg')
bw = img.convert("L")
bw.show()
