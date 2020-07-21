clear
close all
load ppi72_c1
load ppi72_c6000

data=[ppi72_c1; ppi72_c6000];
label=ones(size(data,1),1);
label(1:size(ppi72_c1,1))=0;

dim=300;
w=pca(data);
data=data*w(:,1:dim); % pca reduction
%{
figure
plot(data(label==0,1),data(label==0,2),'b.'); hold on
plot(data(label==1,1),data(label==1,2),'r.'); hold off
legend('ppi72 c1','ppi72 c6000');
%}
save('ppi72_pca.mat','data','-v7.3');
