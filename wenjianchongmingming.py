import os

def remove_ad_text(dir2,ad_text):

#如果dir2不是一个有效的目录，直接返回
    if not os.path.isdir(dir2):
        return

    #如果传递的dir2末尾没有路径分隔符，自动加入
    if not dir2.endswith(os.path.sep):
        dir2 += os.path.sep

    #获取目录下所有的子目录以及文件名（返回列表类型）

    names = os.listdir(dir2)

    for name in names:
        #拼接成完整的文件名（包含路径和文件名）
        sub_path = os.path.join(dir2,name)
        #判断该路径是目录还是文件，如果是目录则进行递归

        if os.path.isdir(sub_path):
            remove_ad_text(sub_path,ad_text)
        #将当前文件或目录重命名去掉广告词
        name = name.replace(ad_text,"")
        new_path = os.path.join(dir2,name)
        #文件重命名
        os.rename(sub_path,new_path)


remove_ad_text(r"D:\下载文件","[www.abc.com]")
