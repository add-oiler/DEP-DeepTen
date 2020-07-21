% 将align后的bmp文件转为可用pca降维的vec*n矩阵

clear
close all

load hs
c1_name = dir('ppi72\c1\*bmp');
c6000_name = dir('ppi72\c6000\*bmp');
total = numel(c1_name) + numel(c6000_name);

for p=1:total
    fprintf('%.2f%%\n',100 * p / total);
    if p <= numel(c1_name)
        img = imread(['ppi72\c1\' c1_name(p).name]);
    else
        img = imread(['ppi72\c6000\' c6000_name(p - numel(c1_name)).name]);
    end
    shape = size(img);
    res = zeros(1);
    cnt = 0;
    for k = 1:3
        for i = 1:shape(1)
            for j = 1:shape(2)
                if hs(i,j) == 0
                    cnt = cnt + 1;
                    res(cnt) = img(i,j,k);
                end
            end
        end
    end
    if p == 1
        ppi72_c1 = res;
    elseif (1 < p) && (p <= numel(c1_name))
        ppi72_c1 = [ppi72_c1;res]; % How I wish I knew how to allocate memory.
    elseif p == numel(c1_name) + 1
        ppi72_c6000 = res;
    else
        ppi72_c6000 = [ppi72_c6000;res];
    end
end

save('ppi72_c1.mat','ppi72_c1','-v7.3');
save('ppi72_c6000.mat','ppi72_c6000','-v7.3');
