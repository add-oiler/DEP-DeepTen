import os
import shutil


def move_file(path, p1, p2):
    # path_xml = "36ppi/c1"
    # filelist = os.listdir(path_xml)
    # path1 = "36ppi_train/c1"
    # path2 = "36ppi_test/c1"

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
    move_file("36ppi/c1", "36ppi_train/c1/", "36ppi_test/c1/")  # 分割训练集
    move_file("36ppi/c6000", "36ppi_train/c6000/", "36ppi_test/c6000/")
    print('Seg over')
