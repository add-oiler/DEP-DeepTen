import os
import shutil


def copy_file(pfrom, pto, rt):
    path_from = pfrom
    filelist = os.listdir(path_from)
    path_to = pto
    ratio = rt

    file_cnt = len(filelist)
    cnt = 0

    print(file_cnt)

    for files in filelist:
        filename = os.path.splitext(files)[0]  # 读取文件名
        if file_cnt * ratio <= cnt < file_cnt * (ratio + 1/3):
            cnt += 1
            full_path = os.path.join(pfrom, files)
            despath = path_to + filename + '.bmp'
            shutil.copyfile(full_path, despath)

        else:
            cnt += 1
            continue


if __name__ == '__main__':
    fcondition = ["Original", "Aligned"]
    fppi = ["36", "54", "72"]
    ftype = ["train", "test"]
    fclass = ["c1", "c6000"]
    fratio = [0, 1/3, 2/3]
    for cdt in fcondition:
        for ppi in fppi:
            for tp in ftype:
                for cls in fclass:
                    if ppi == "36":
                        rto = fratio[0]
                    if ppi == "54":
                        rto = fratio[1]
                    else:
                        rto = fratio[2]
                    copy_file(cdt + "_Images/Images_" + ppi + "ppi/" + ppi + "ppi_test/" + cls, cdt + "_hybrid/" + tp +
                              "/" + cls + "/", rto)  # 分割训练集
    # copy_file("Original_Images/Images_36ppi/36ppi_test/c6000", "Original_hybrid/test/c6000/", 0)
    print('Seg over')
