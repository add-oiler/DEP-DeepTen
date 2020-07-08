import os
import shutil


def move_file(path, p1, p2):
    os.mkdir(p1)
    os.mkdir(p2)
    path_xml = path
    filelist = os.listdir(path_xml)
    path1 = p1
    path2 = p2
    ratio = 0.5

    file_cnt = len(filelist)
    cnt = 0

    print(file_cnt)

    for files in filelist:
        filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
        filename0 = os.path.splitext(files)[0]  # 读取文件名
        if cnt < file_cnt * ratio:
            full_path = os.path.join(path, files)
            despath = path1 + filename0 + '.bmp'
            shutil.move(full_path, despath)

        else:
            full_path = os.path.join(path, files)
            despath = path2 + filename0 + '.bmp'
            shutil.move(full_path, despath)

        cnt += 1


if __name__ == '__main__':
    dir_name = input("Folder: ")
    os.mkdir(dir_name + "_train")
    os.mkdir(dir_name + "_test")
    move_file(dir_name + "/c1", dir_name + "_train/c1/", dir_name + "_test/c1/")  # 分割训练集
    move_file(dir_name + "/c6000", dir_name + "_train/c6000/", dir_name + "_test/c6000/")
    print('Seg over')
    
