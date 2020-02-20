clear;
clc;
PZ=0.8;
tic
for miu=0.1:0.1:0.8
    mytext=['groundmiu' num2str(miu*10) '.csv'];
    ground=dlmread(mytext);
    lg=length(ground);
    adjZmat=zeros(lg*15,2);
    noG=sum(ground);
    a=1;                  % community           
    counter=0;
    for i=1:lg            % Member
        for j=i+1:noG(a)
            if rand<PZ
                counter=counter+1;
                adjZmat(counter,:)=[i,j];
                counter=counter+1;
                adjZmat(counter,:)=[j,i];
            end
        end
        for j=j+1:lg
            if rand>PZ
                counter=counter+1;
                adjZmat(counter,:)=[i,j];
                counter=counter+1;
                adjZmat(counter,:)=[j,i];
            end
        end
    end
    mytext=['ZAVbLFRmiu' num2str(miu*10) '.csv'];
    adjZmat=adjZmat(adjZmat(:,1)>0,:);
    csvwrite(mytext,adjZmat)
end
toc
