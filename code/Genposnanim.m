function void = Genposnanim()  	%taking x as a row matrix

% f=fopen('input.txt');
f=fopen('inputanim.txt');

x=fscanf(f,"%d",1);	%first argument in a file should be the no. of beats in a sequence
noofvectors=x*30;
for i=1:x
for j=1:30
ip(i,j)=fscanf(f,"%d",1);
endfor
endfor

sss=size(ip(1,:));

%axis([0 6 0 8]);
%s1=sprintf("figure %d",x);
%title(s1);


%axis([0 6 0 8]);
%hold on

%x=[0,0,2,-1,2,0,1,0,-1,-1,4,3,0,1,3,0,0,0,0,0,0,1,0,0,0,2,0,3,0,-3];

%x(19)=1;	%twist Incorporated
#{
[x(1),x(2)]=deal(1,1);  %head
3 to 10=rhand
11 to 18=lhand
19,20=waist
21to 25=rleg
26 to 30=lleg
#}

cols=ceil(x/2);
row=2;
for i=1:x 
  newplot
	%subplot(row,cols,i)
	rhand_tw(ip(i,:));
	lhand_tw(ip(i,:));
	head_tw(ip(i,:));
	lleg(ip(i,:));
	rleg(ip(i,:));
	s1=sprintf("Beat %d",i);
	title(s1);
  eval(sprintf("print -dpng 'Genposanim%d.png'",i));
  pause(1);
  hold off
endfor



endfunction
	
