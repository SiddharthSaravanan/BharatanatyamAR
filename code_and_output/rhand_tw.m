function void = rhand_tw(x)		
axis([0 6 0 8]);
hold on
r_h_x=x(4);
r_h_y=x(5);
r_h_z=x(6);
	
x1=1.9;
y1=3;			
if(r_h_x==4)
	x2=1;				
elseif(r_h_x==3)
	x2=1.2;	
elseif(r_h_x==2)
	x2=1.5;	
elseif(r_h_x==1)
	x2=1.8;
elseif(r_h_x==0)
	x2=2;
elseif(r_h_x==-1)
	x2=2.15;	
elseif(r_h_x==-2)
	x2=2.35;		
else
	x2=2.5;
end

	
if(r_h_y==4)
	y2=4;
elseif(r_h_y==3)
	y2=3.7;
elseif(r_h_y==2)
	y2=3.5;
elseif(r_h_y==1)
	y2=3.3;
elseif(r_h_y==0)
	y2=3;
elseif(r_h_y==-1)
	y2=2.7;
elseif(r_h_y==-2)
	y2=2.5;
elseif(r_h_y==-3)
	y2=2.3;
else
	y2=2;
end

%Elbow moments
r_e=x(7);
m=r_h_y;				%l_h_y COMES INTO PICTURE AS ANGLE WRT SHOULDER is projection of y axis

if (m==0)						%means angle of shoulder is 
		
	if (r_e==1)		%45 degree
		x3=x2-0.7;
		y3=y2+0.5;
	elseif(r_e==0)		%0deg
		x3=x2-1;
		y3=y2;
	elseif(r_e==2)		%90 deg
		x3=x2;
		y3=y2+1;
	else			%135deg
		x3=x2+0.5;
		y3=y2+0.3;
		
    end
	

elseif (m==1)		%means 30deg
	
	if(r_e==0)
		x3=x2-0.8;
		y3=y2+0.4;
	elseif(r_e==1)
		x3=x2-0.3;
		y3=y2+0.6;
	elseif(r_e==2)
		x3=x2+0.3;
		y3=y2+0.6;
	else
		x3=x2+0.5;
		y3=y2+0.3;		
    end
		

elseif(m==2)		%means 45 deg
	
	if(r_e==0)
		x3=x2-0.8;
		y3=y2+0.4;
	elseif(r_e==1)
		x3=x2;
		y3=y2+0.7;
	elseif(r_e==2)
		x3=x2+0.5;
		y3=y2+0.6;
	else
		x3=x2+0.5;
		y3=y2;		
    end
elseif(m==3)		%means 60 deg
	
	if(r_e==0)
		x3=x2-0.5;
		y3=y2+0.6;
	elseif(r_e==1)
		x3=x2+0.2;
		y3=y2+0.6;
	elseif(r_e==2)
		x3=x2+0.5;
		y3=y2+0.4;
	else
		x3=x2+0.6;
		y3=y2-0.2;		
    end


elseif(m==4)		%means 90 deg
	
	if(r_e==0)
		x3=x2;
		y3=y2+1;
	elseif(r_e==1)
		x3=x2+0.3;
		y3=y2+0.7;
	elseif(r_e==2)
		x3=x2+0.7;
		y3=y2;
	else
		x3=x2+0.3;
		y3=y2-0.7;		
    end

elseif(m==-1)		%means -30 deg
	
	if(r_e==0)
		x3=x2-0.8;
		y3=y2-0.8;
	elseif(r_e==1)
		x3=x2-0.6;
		y3=y2-0.6;
	elseif(r_e==2)
		x3=x2+0.4;
		y3=y2-0.6;
	else
		x3=x2+0.5;
		y3=y2+0.3;		
    end

elseif(m==-2)		%means -45 deg
	
	if(r_e==0)
		x3=x2-0.8;
		y3=y2-0.8;
	elseif(r_e==1)
		x3=x2;
		y3=y2-1;
	elseif(r_e==2)
		x3=x2+0.5;
		y3=y2-0.6;
	else
		x3=x2+0.5;
		y3=y2+0.5;		
    end


elseif(m==-3)		%means -60 deg
	
	if(r_e==0)
		x3=x2-0.8;
		y3=y2-0.8;
	elseif(r_e==1)
		x3=x2+0.2;
		y3=y2-1;
	elseif(r_e==2)
		x3=x2+0.5;
		y3=y2-0.3;
	else
		x3=x2+0.4;
		y3=y2+0.6;		
    end

elseif(m==-4)		%means -90 deg
	
	if(r_e==0)
		x3=x2;
		y3=y2-0.8;
	elseif(r_e==1)
		x3=x2+0.2;
		y3=y2-0.5;
	elseif(r_e==2)
		x3=x2-0.8;
		y3=y2;
	else
		x3=x2+0.6;
		y3=y2+0.8;		
    end
end
	
%hastas
		
r_w=x(8);
r_fg=x(3);

	
if(r_w==1)		%means wrist facing downwards
	if(r_fg==0)	%pataka
			x4=x3;
			y4=y3-0.2;
            x6=x3;
			x5=x6;
            y6=y3;
			y5=y6;
            
	elseif(r_fg==2)	%kartari
			x4=x3;
			y4=y3-0.2;
			x5=x3+0.2;
			x6=x3;
			y5=y3-0.2;
			y6=y3;	
	else  %ardha
			x4=x3+0.25;
			x5=x3+0.15;
			x6=x3+0.2;
			y4=y3-0.2;
			y5=y3-0.2;
			y6=y3-0.2;
    end
else				%downward
	if(r_fg==0)	%pataka
			x4=x3;
			y4=y3+0.2;
            x6=x3;
			x5=x6;
            y6=y3;
			y5=y6;
	elseif(r_fg==2)	%kartari
			x4=x3;
			y4=y3+0.2;

			x5=x3-0.2;
			y5=y3+0.2;
			x6=x3;			
			y6=y3;	
	else  %ardha
			x4=x3-0.2;
			x5=x3-0.25;
			x6=x3-0.15;
			y4=y3+0.2;
			y5=y3+0.2;
			y6=y3+0.2;	
    end
end


%shoulder jerks
r_sj=x(10);
if(r_sj==1)			%pulling in
	x1=x1+0.2;
	x2=x2+0.2;
	x3=x3+0.2;
	x4=x4+0.2;
elseif(r_sj==-1)		%pushing out
	x1=x1-0.2;
	x2=x2-0.2;
	x3=x3-0.2;
	x4=x4-0.2;
end


%front and back will have same projections. Thus colour used to distinguish them.
%{
if(r_h_z==0)
	plot([x1,x2,x3,x4],[y1,y2,y3,y4],'r');	%none
elseif(r_h_z==1)
	plot([x1,x2,x3,x4],[y1,y2,y3,y4],'b-x');	%front
else
	plot([x1,x2,x3,x4],[y1,y2,y3,y4],'g-x');	%back
endif
%}

w_tw=x(19);
if(w_tw==1)
	x1=x1+0.5;
	x2=x2+0.5;
	x3=x3+0.5;
	x4=x4+0.5;
	plot([2,3],[2,3.8]);
elseif(w_tw==-1)
	x1=x1-0.5;
	x2=x2-0.5;
	x3=x3-0.5;
	x4=x4-0.5;
	plot([2,1],[2,3.8]);
else
	plot([2,2],[2,4])

end

plot([x1,x2,x3],[y1,y2,y3],'r');	%none
plot([x3,x4],[y3,y4],'r');
plot([x3,x5],[y3,y5],'r');
plot([x3,x6],[y3,y6],'r');

%print -dpng 'handposn.png';
end
