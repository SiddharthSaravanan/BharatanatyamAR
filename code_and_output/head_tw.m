function void = head_tw(x)
sb_o=x(2);
sb_m=x(1);

if (sb_o==0)			%means straight facing
	if(sb_m==0)
		t=linspace(0,2*pi,100);
		circx=2+0.5*cos(t);         
		circy=4.5+0.5*sin(t);
		x1=0;
        x2=0;
		y1=0;
        y2=0;
		%plot(circx,circy);				
		
	elseif(sb_m==-1)
		t=linspace(0,-pi,100);
		circx=2+0.5*cos(t);         
		circy=4.5+0.5*sin(t);
		%plot(circx,circy);	
		
		
		[x1,x2]=deal(1.5,2.5);
		[y1,y2]=deal(4.5,4.5);
	else
		t=linspace(0,pi,100);
		circx=2+0.5*cos(t);         
		circy=4.5+0.5*sin(t);
		%plot(circx,circy);
		
		[x1,x2,y1,y2]=deal(1.5,2.5,4.5,4.5);	
    end
elseif(sb_o==-1)
	if(sb_m==0)
		t=linspace(-pi/2,pi/2,100);
		circx=2+0.5*cos(t);         
		circy=4.5+0.5*sin(t);
		%plot(circx,circy);		
		
		[x1,x2,y1,y2]=deal(2,2,4,5);
	
		
	elseif(sb_m==-1)
		t=linspace(-pi/4,3*pi/4,100);
		circx=2+0.5*cos(t);         
		circy=4.5+0.5*sin(t);
		%plot(circx,circy);	
		
		[x1,x2,y1,y2]=deal(2.35,1.65,4.15,4.85);
	else
		t=linspace(-3*pi/4,pi/4,100);
		circx=2+0.5*cos(t);         
		circy=4.5+0.5*sin(t);
		%plot(circx,circy);
		
		[x1,x2,y1,y2]=deal(1.65,2.35,4.15,4.85);
    end

else
	if(sb_m==0)
		t=linspace(pi/2,3*pi/2,100);
		circx=2+0.5*cos(t);         
		circy=4.5+0.5*sin(t);
		%plot(circx,circy);	
		
		[x1,x2,y1,y2]=deal(2,2,4,5);
		
	elseif(sb_m==-1)
		t=linspace(pi/4,5*pi/4,100);
		circx=2+0.5*cos(t);         
		circy=4.5+0.5*sin(t);
		%plot(circx,circy);
		
		[x1,x2,y1,y2]=deal(1.65,2.35,4.15,4.85);
	else
		t=linspace(3*pi/4,7*pi/4,100);
		circx=2+0.5*cos(t);         
		circy=4.5+0.5*sin(t);
		%plot(circx,circy);	
		
		[x1,x2,y1,y2]=deal(2.35,1.65,4.15,4.85);
		
	end
end


w_tw=x(19);

if(w_tw==1)
	circx=circx+1;
	x1=x1+1;
	x2=x2+1;
	circy=circy-0.2;
	y1=y1-0.2;
	y2=y2-0.2;
elseif(w_tw==-1)
	circx=circx-1;
	x1=x1-1;
	x2=x2-1;
	circy=circy-0.2;
	y1=y1-0.2;
	y2=y2-0.2;
end


plot(circx,circy);
hold on
plot([x1,x2],[y1,y2],'r');
end
