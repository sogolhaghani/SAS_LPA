clear
clc
tic
nattr=5;
for miu=0.1:0.1:0.8
    mytext=['groundmiu' num2str(miu*10) '.csv'];
    ground=dlmread(mytext);
    [N,Q]=size(ground);    
    nq=sum(ground);
    a=1;
    b=nq(1);
    for i=2:Q
        a=a+nq(i-1);
        b=b+nq(i);
    end
    
    attributes=zeros(N,nattr);
    MeanAttr=floor(nattr*Q*rand(Q,nattr)+1);
    StDeAttr=floor((rand(Q,nattr)+0.5)*10)./10;
    for j=1:nattr
        a=1;
        b=nq(1);
        attributes(a:b,j)=randn(nq(1),1).*StDeAttr(1,j)+MeanAttr(1,j);
        for i=2:Q
            a=a+nq(i-1);
            b=b+nq(i);
            attributes(a:b,j)=randn(nq(i),1).*StDeAttr(i,j)+MeanAttr(i,j);
        end
    end
    attributes=floor(abs(attributes));
    mytext=['ATTRmiu' num2str(miu*10) '.csv'];
    csvwrite(mytext,attributes)
end
toc