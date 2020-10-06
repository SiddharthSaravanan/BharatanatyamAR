function void=rleg(x)
plot([1.9,2.1],[2,2],'r');
l_lx=x(23);
l_lz=x(24);
l_ly=x(25);
l_an=x(21);
l_kn=x(22);
x1=1.9;
y1=2;

if(l_lx==0)
	x2=1.9;
elseif(l_lx==1)
	x2=1.8;
elseif(l_lx==2)
	x2=1.7;
elseif(l_lx==3)
	x2=1.6;
elseif(l_lx==4)
	x2=1.5;
elseif(l_lx==-1)
	x2=2;
elseif(l_lx==-2)
	x2=2.1;
end
	
if(l_ly==0)		%touching ground
	y2=1;
else			%above ground
	y2=1.2;
end

%take slope and change.
if(x2==x1)

	if(l_kn==0)
		x3=x2;
		y3=y2-0.6;
	elseif(l_kn==1)
		x3=x2-0.2;
		y3=y2-0.8;
	else
		x3=x2-0.4;
		y3=y2-0.6;
	end
elseif(((y2-y1)/(x2-x1))>0)		%positive slope
	if(l_kn==0)
		x3=x2-0.2;
		y3=y2-0.4;
	elseif(l_kn==1)
		x3=x2;
		y3=y2-0.4;
	else
		x3=x2+0.4;
		y3=y2+0.1;
	end
else
	if(l_kn==0)
		x3=x2+0.2;
		y3=y2-0.4;
	elseif(l_kn==1)
		x3=x2;
		y3=y2-0.4;
	else
		x3=x2-0.4;
		y3=y2+0.1;
	end
end

if(l_an==0)
	x4=x3;
	y4=y3-0.2;
elseif(l_an==-1)
	x4=x3-0.2;
	y4=y3-0.1;
else
	x4=x3+0.2;
	y4=y3-0.1;
end

plot([x1,x2,x3,x4],[y1,y2,y3,y4],'r');


end