import java.applet.*;
import java.awt.*;
import java.awt.event.*;

public class Man extends Applet implements ActionListener
{

	int x1=200, x2=200, y1=150, y2=300;
	int choice = 1, bl = 1, r =1;
	Button next, prev, opt, blink, speak;

	public void init()
	{
		prev = new Button("<--");
		prev.addActionListener(this);
		add(prev);
		next = new Button("-->");
		next.addActionListener(this);
		add(next);
		opt = new Button("?");
		opt.addActionListener(this);
		add(opt);
		blink = new Button("^^");
		blink.addActionListener(this);
		add(blink);
		speak = new Button(":D");
		speak.addActionListener(this);
		add(speak);
	}

	public void paint(Graphics g)
	{
		setBackground(Color.BLACK);
		setForeground( Color.WHITE );
		g.setColor(Color.WHITE);
		g.drawLine(x1,y1,x2,y2);
		if (choice==1)
		{	
			g.drawLine(x1, y1+50, x2+75, y1-20); //right side hand
			g.drawLine(x1-75, y1-20, x2, y1+50); //left
		}
		else if (choice==2) 
		{
			g.drawLine(x1, y1+50, x2+75, y1+120); //right side hand
			g.drawLine(x1-75, y1+120, x2, y1+50); //left
		}
		g.drawLine(x2, y2, x2+75, y2+75); //right side leg
		g.drawLine(x2-75,y2+75, x2, y2); //left

		g.fillArc(x1-35, y1-70, 70, 70, 0, 360);
		
		g.setColor(Color.BLACK);
		if (bl == 1)
		{
			g.fillArc(x1-22, y1-50, 15, 15, 0, 360);
			g.fillArc(x1+7, y1-50, 15, 15, 0, 360);
		}
		else if (bl == 2)
		{
			g.drawArc(x1-22, y1-50, 15, 15, 0, -180);
			g.drawArc(x1+7, y1-50, 15, 15, 0, -180);	
		}

		if (r == 1)
			g.drawArc(x1-22, y1-40, 45, 30, 0, -180);
		else if (r == 2)
			g.fillArc(x1-22, y1-40, 45, 30, 0, -180);
	}

	public void actionPerformed(ActionEvent ae)
	{
		String str=ae.getActionCommand();
		if (str.equals("-->"))
		{	
			x1+=50;
			x2+=50;
			repaint();
		}
		else if (str.equals("<--"))
		{
			x1-=50;
			x2-=50;
			repaint();
		}
		else if (str.equals("?"))
		{
			if (choice == 1)
				choice = 2;
			else if (choice == 2)
				choice = 1;
			repaint();
		}
		else if (str.equals("^^"))
		{
			if (bl == 1)
				bl = 2;
			else if (bl == 2)
				bl = 1;
			repaint();
		}
		else if (str.equals(":D"))
		{
			if (r == 1)
				r = 2;
			else if (r == 2)
				r = 1;
			repaint();
		}
	}
}