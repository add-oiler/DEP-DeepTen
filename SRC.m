function [acc_max, lbd_opt] = SRC(DATA,LABEL,INDICES)
ClassName = unique(LABEL);
class_num = length(ClassName);
K = max(INDICES);
acc_max = 0;
for lbd = [.01 .1 1 5]
    ACC = zeros(1,K);
    for k = 1:K
        test = (INDICES==k);
        train = ~test;
        group = LABEL(train);
        label = LABEL(test);
        
        TRAINING = DATA(train,:);
        SAMPLE = DATA(test,:);  
        
        coef = LASSO(TRAINING',SAMPLE','lambda',lbd);
        coef = coef';
        residual = zeros(size(SAMPLE,1),class_num);
        CLASS = ones(size(SAMPLE,1),1);
        for j = 1:size(SAMPLE,1)
            for c = 1:class_num
                index = find(group==ClassName(c));
                residual(j,c) = norm(coef(j,index)*TRAINING(index,:)-SAMPLE(j,:));
            end
            idx = find(residual(j,:)==min(residual(j,:)),1);
            CLASS(j) = ClassName(idx);
        end
        ACC(k) = sum(CLASS==label)/length(label)*100;
    end  
    acc = mean(ACC);
    if acc > acc_max
        acc_max = acc;
        lbd_opt = lbd;
    end
end