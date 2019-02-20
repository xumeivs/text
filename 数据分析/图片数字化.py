from PIL import Image
im1=Image.open('F:/数据分析/素材/1.jpg')
im2=Image.open('F:/数据分析/素材/2.jpg')
im3=Image.open('F:/数据分析/素材/3.jpg')
im4=Image.open('F:/数据分析/素材/4.jpg')
im5=Image.open('F:/数据分析/素材/5.jpg')
im6=Image.open('F:/数据分析/素材/6.jpg')
im7=Image.open('F:/数据分析/素材/7.jpg')
im8=Image.open('F:/数据分析/素材/8.jpg')
im9=Image.open('F:/数据分析/素材/9.jpg')
fh1=open('F:/数据分析/素材/text/1.txt','a')
fh2=open('F:/数据分析/素材/text/2.txt','a')
fh3=open('F:/数据分析/素材/text/3.txt','a')
fh4=open('F:/数据分析/素材/text/4.txt','a')
fh5=open('F:/数据分析/素材/text/5.txt','a')
fh6=open('F:/数据分析/素材/text/6.txt','a')
fh7=open('F:/数据分析/素材/text/7.txt','a')
fh8=open('F:/数据分析/素材/text/8.txt','a')
fh9=open('F:/数据分析/素材/text/9.txt','a')
width=im1.size[0]
height=im1.size[1]
for i in range(0,width):
    for j in range(0,height):
        cl1=im1.getpixel((i,j))
        sumcl1=cl1[0]+cl1[1]+cl1[2]
        if (sumcl1==0):
            fh1.write('1')
        else:
            fh1.write('0')
    fh2.write('\n')
fh1.close()
for a in range(0,width):
    for b in range(0,height):
        cl2=im2.getpixel((a,b))
        sumcl2=cl2[0]+cl2[1]+cl2[2]
        if (sumcl2==0):
            fh2.write('1')
        else:
            fh2.write('0')
    fh2.write('\n')
fh2.close()
for c in range(0,width):
    for d in range(0,height):
        cl3=im3.getpixel((c,d))
        sumcl3=cl3[0]+cl3[1]+cl3[2]
        if (sumcl3==0):
            fh3.write('1')
        else:
            fh3.write('0')
    fh3.write('\n')
fh3.close()
for e in range(0,width):
    for f in range(0,height):
        cl4=im4.getpixel((e,f))
        sumcl4=cl4[0]+cl4[1]+cl4[2]
        if (sumcl4==0):
            fh4.write('1')
        else:
            fh4.write('0')
    fh4.write('\n')
fh4.close()
for g in range(0,width):
    for h in range(0,height):
        cl5=im5.getpixel((g,h))
        sumcl5=cl5[0]+cl5[1]+cl5[2]
        if (sumcl5==0):
            fh5.write('1')
        else:
            fh5.write('0')
    fh5.write('\n')
fh5.close()
for k in range(0,width):
    for l in range(0,height):
        cl6=im6.getpixel((k,l))
        sumcl6=cl6[0]+cl6[1]+cl6[2]
        if (sumcl6==0):
            fh6.write('1')
        else:
            fh6.write('0')
    fh6.write('\n')
fh6.close()
for m in range(0,width):
    for n in range(0,height):
        cl7=im7.getpixel((m,n))
        sumcl7=cl7[0]+cl7[1]+cl7[2]
        if (sumcl7==0):
            fh7.write('1')
        else:
            fh7.write('0')
    fh7.write('\n')
fh7.close()
for o in range(0,width):
    for p in range(0,height):
        cl8=im8.getpixel((o,p))
        sumcl8=cl8[0]+cl8[1]+cl8[2]
        if (sumcl8==0):
            fh8.write('1')
        else:
            fh8.write('0')
    fh8.write('\n')
fh8.close()
for q in range(0,width):
    for r in range(0,height):
        cl9=im9.getpixel((q,r))
        sumcl9=cl9[0]+cl9[1]+cl9[2]
        if (sumcl9==0):
            fh9.write('1')
        else:
            fh9.write('0')
    fh9.write('\n')
fh9.close()
            
            
