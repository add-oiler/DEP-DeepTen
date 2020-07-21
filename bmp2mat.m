clear
close all

rgb = imread('Healthy.bmp');
shape = size(rgb);
hs = zeros(shape(1),shape(2));

for i = 1:shape(1)
    for j = 1:shape(2)
        is_bg = 1;
        for k = 1:3
            if rgb(i,j,k) ~= 255
                is_bg = 0;
                break;
            end
        end
        if is_bg == 1
            hs(i,j) = 1;
        end
    end
end

save hs
