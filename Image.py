from PIL import Image, ImageChops

#Разница в процентах
i1 = Image.open("11111.png")
i2 = Image.open("22222.png")
assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."

pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1 - p2) for p1, p2 in pairs)
else:
    dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

ncomponents = i1.size[0] * i1.size[1] * 3
print("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)

#Разница в картинке
point_table = ([0] + ([255] * 255))

def black_or_b(a, b):
       diff = ImageChops.difference(a, b)
       diff = diff.convert('L')
       diff = diff.point(point_table)
       new = diff.convert('RGB')
       new.paste(b, mask=diff)
       return new

a = Image.open('11111.png')
b = Image.open('22222.png')
c = black_or_b(a, b)
c.save('333.png')