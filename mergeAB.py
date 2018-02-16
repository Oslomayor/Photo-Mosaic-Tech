# 融合两张图片
# 注意两张图片的尺寸要相同
# 可配合 Foto-Mosaik-Edda 软件使用
# RGBA模式下，一张图片映射一个列表，列表的元素是四元组(R,G,B,A)
# R = Red, G = Green, B = Blue, A = Alpha(anti-transparence)
from PIL import Image

def mergeAB(srcA,srcB,dstAB):
    imgA = Image.open(srcA).convert("RGBA")
    imgB = Image.open(srcB).convert("RGBA")
    datasA = imgA.getdata()
    datasB = imgB.getdata()
    newData = list()
    # 建立一个缓存列表
    temp = list([0,0,0,0])
    for dataA,dataB in zip(datasA,datasB):
        # 每个像素点的4通道融合
        for i in range(0,4):
            # 调节权重
            temp[i] = int(dataA[i]*0.7 + dataB[i]*0.3)
        # 图片列表的元素是四元组
        newData.append(tuple(temp))
    imgA.putdata(newData)
    # imgA.show()
    imgA.save(dstAB)

content = r"C:\Users\Denis\Desktop\TEMP\R2\\"
mergeAB(content+"rawA.jpg",content+"rawB.jpg",content+"AB.png")
        
