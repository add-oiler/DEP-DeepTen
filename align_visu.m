clear
close all
clc
data_name=dir('random_sample\l002-e70\*txt');
for i=1:numel(data_name)
    disp(data_name(i).name);
    data=load(['random_sample\l002-e70\' data_name(i).name]);
    sz=size(data);
    epoch=linspace(1,sz(1),sz(1));
    temp=data(:,2);
    if temp(1)<50
        acc=data(:,1);
    else
        acc=data(:,2);
    end
    subplot(1,2,1), plot(epoch,acc),xlabel('Epoch'),ylabel('Accuracy');
    hold on;
end
title('learning rate = 0.02, epoch = 70');
legend('Original','Aligned');
hold off;

data_name=dir('random_sample\l0035-e50\*txt');
for i=1:numel(data_name)
    disp(data_name(i).name);
    data=load(['random_sample\l0035-e50\' data_name(i).name]);
    sz=size(data);
    epoch=linspace(1,sz(1),sz(1));
    temp=data(:,2);
    if temp(1)<50
        acc=data(:,1);
    else
        acc=data(:,2);
    end
    subplot(1,2,2), plot(epoch,acc),xlabel('Epoch'),ylabel('Accuracy');
    hold on;
end
title('learning rate = 0.035, epoch = 50');
legend('Original','Aligned');
hold off;
