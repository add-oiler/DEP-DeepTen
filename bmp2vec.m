clear
close all

load hs

% rgb = imread('DiabetesMellitus.bmp');
rgb = imread('Healthy.bmp');
shape = size(rgb);

%{
for i = 1:217
    for j = 1:243
        is_bg = 1;
        for k = 1:3
            if rgb(i,j,k) ~= 255
                is_bg = 0;
                break;
            end
        end
        if is_bg == 1
            for k = 1:3
                hs(i,j,k) = 1;
            end
        end
    end
end
%}

res = zeros(1);
cnt = 1;

for k = 1:3
    for i = 1:shape(1)
        for j = 1:shape(2)
            if hs(i,j) == 0
                res(cnt) = rgb(i,j,k);
                cnt = cnt + 1;
            end
        end
    end
end

                
    
            
    
