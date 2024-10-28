%ha duplazodik, felezodik, megmarad
x=2; %petak szama kezdetkor
t=3; %hany ev
v=[3 1 0.5]; %valtozekonysag, jelen esetben duplaja, megmarad, felere csokken
h=length(v); %igazabol valoszinusege, 1/h, jelen esetben 1/3
% varhato ertek
varhatoertekpetak=x*(1/h*v(1)+1/h*v(2)+1/h*v(3))^t
% szorasnegyzet
szoraspetak=(x^2)*((1/h*v(1)^2+1/h*v(2)^2+1/h*v(3)^2)^t - (1/h*v(1)+1/h*v(2)+1/h*v(3))^(t*2))

%lottos
lottoara=250;
lottoszamok=[1300 16000 1100000 1600000000];
p2=nchoosek(5,2)*nchoosek(85,3)/nchoosek(90,5);
p3=nchoosek(5,3)*nchoosek(85,2)/nchoosek(90,5);
p4=nchoosek(5,4)*nchoosek(85,1)/nchoosek(90,5);
p5=nchoosek(5,5)*nchoosek(85,0)/nchoosek(90,5);
varhato=p2*lottoszamok(1)+p3*lottoszamok(2)+p4*lottoszamok(3)+p5*lottoszamok(4)-lottoara

%gepes selejt
alkatreszek=[360 160 390 590]; %alkatreszek sorban
selejtp=[0.06 0.06 0.04 0.05]; %selejtek aranya
ossz=sum(alkatreszek);
pr=alkatreszek(1)/ossz*selejtp(1)+alkatreszek(2)/ossz*selejtp(2)+alkatreszek(3)/ossz*selejtp(3)+alkatreszek(4)/ossz*selejtp(4)
melyikgep=2; %ide kell h melyik gep a masodik cuccnal
pgi=alkatreszek(melyikgep)/ossz;
pjgi=1-selejtp(melyikgep);
pj=1-pr;
pgij=pgi*pjgi/pj
