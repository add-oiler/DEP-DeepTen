clear
close all
clc
data_name=dir('convergence\*txt');
for i=1:numel(data_name)
    disp(data_name(i).name);
    data=load(['convergence\' data_name(i).name]);
    sz=size(data);
    epoch=linspace(1,sz(1),sz(1));
    temp=data(:,2);
    if temp(1)<50
        loss=data(:,2);
        acc=data(:,1);
    else
        loss=data(:,1);
        acc=data(:,2);
    end
    subplot(2,5,i), plot(epoch,acc),xlabel('Epoch'),ylabel('Accuracy'),title(data_name(i).name);
    subplot(2,5,i+5), plot(epoch,loss),xlabel('Epoch'),ylabel('Loss');
end

