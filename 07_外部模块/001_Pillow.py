from PIL import Image
from PIL import ImageFilter

_DEBUG_00 = False

if _DEBUG_00:
    # 打开一个jpg图像,注意当前路径
    image_00 = Image.open("../0001.jpg")
    # 获取图像的尺寸
    index_00, index_01 = image_00.size
    print(index_00, index_01)

    # 缩放到50%
    image_00.thumbnail((index_00 / 2, index_01 / 2))
    image_00.save("../0003.jpg")

    # 打开jpg图像文件,注意为当前路径:
    image_01 = Image.open("../0002.jpg")
    # 应用模糊滤镜
    index_02 = image_01.filter(ImageFilter.BLUR)
    index_02.save("../0004.jpg")

    image_02 = Image.open(r"../0001.jpg")
    image_02.rotate(45).show()

    from PIL import Image, ImageDraw, ImageFont, ImageFilter

    import random


    # 随机字母:
    def rndChar():
        return chr(random.randint(65, 90))


    # 随机颜色1:
    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


    # 随机颜色2:
    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save('../0005.jpg')
