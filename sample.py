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
    copy_file("Original_Images/Images_36ppi/36ppi_test/c1", "Original_hybrid/test/c1/", 0)  # 分割训练集
    copy_file("Original_Images/Images_36ppi/36ppi_test/c6000", "Original_hybrid/test/c6000/", 0)
    copy_file("Original_Images/Images_54ppi/54ppi_test/c1", "Original_hybrid/test/c1/", 1/3)
    copy_file("Original_Images/Images_54ppi/54ppi_test/c6000", "Original_hybrid/test/c6000/", 1/3)
    copy_file("Original_Images/Images_72ppi/72ppi_test/c1", "Original_hybrid/test/c1/", 2/3)
    copy_file("Original_Images/Images_72ppi/72ppi_test/c6000", "Original_hybrid/test/c6000/", 2/3)
    copy_file("Aligned_Images/Images_36ppi/36ppi_test/c1", "Aligned_hybrid/test/c1/", 0)
    copy_file("Aligned_Images/Images_36ppi/36ppi_test/c6000", "Aligned_hybrid/test/c6000/", 0)
    copy_file("Aligned_Images/Images_54ppi/54ppi_test/c1", "Aligned_hybrid/test/c1/", 1/3)
    copy_file("Aligned_Images/Images_54ppi/54ppi_test/c6000", "Aligned_hybrid/test/c6000/", 1/3)
    copy_file("Aligned_Images/Images_72ppi/72ppi_test/c1", "Aligned_hybrid/test/c1/", 2/3)
    copy_file("Aligned_Images/Images_72ppi/72ppi_test/c6000", "Aligned_hybrid/test/c6000/", 2/3)
    copy_file("Original_Images/Images_36ppi/36ppi_train/c1", "Original_hybrid/train/c1/", 0)  # 分割训练集
    copy_file("Original_Images/Images_36ppi/36ppi_train/c6000", "Original_hybrid/train/c6000/", 0)
    copy_file("Original_Images/Images_54ppi/54ppi_train/c1", "Original_hybrid/train/c1/", 1/3)
    copy_file("Original_Images/Images_54ppi/54ppi_train/c6000", "Original_hybrid/train/c6000/", 1/3)
    copy_file("Original_Images/Images_72ppi/72ppi_train/c1", "Original_hybrid/train/c1/", 2/3)
    copy_file("Original_Images/Images_72ppi/72ppi_train/c6000", "Original_hybrid/train/c6000/", 2/3)
    copy_file("Aligned_Images/Images_36ppi/36ppi_train/c1", "Aligned_hybrid/train/c1/", 0)
    copy_file("Aligned_Images/Images_36ppi/36ppi_train/c6000", "Aligned_hybrid/train/c6000/", 0)
    copy_file("Aligned_Images/Images_54ppi/54ppi_train/c1", "Aligned_hybrid/train/c1/", 1/3)
    copy_file("Aligned_Images/Images_54ppi/54ppi_train/c6000", "Aligned_hybrid/train/c6000/", 1/3)
    copy_file("Aligned_Images/Images_72ppi/72ppi_train/c1", "Aligned_hybrid/train/c1/", 2/3)
    copy_file("Aligned_Images/Images_72ppi/72ppi_train/c6000", "Aligned_hybrid/train/c6000/", 2/3)
    print('Seg over')
