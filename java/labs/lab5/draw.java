
import java.awt.*;
import java.awt.event.*;
import java.applet.*;

public class draw extends Applet implements ActionListener
{
	Button add, subtract, multiply, divide, equals, clear;
	TextField result;
	Label l1, l2;
	Button b0, b1, b2, b3, b4, b5, b6, b7, b8, b9;

	public void init()
	{
		setBackground(Color.BLACK);
		setForeground(Color.CYAN);

	  	b0=new Button("0");
		b1=new Button("1");
		b2=new Button("2");
	  	b3=new Button("3");
	  	b4=new Button("4");
 	 	b5=new Button("5");
  		b6=new Button("6");
  		b7=new Button("7");
 	 	b8=new Button("8");
	  	b9=new Button("9");

		b1.addActionListener(this);
	 	b2.addActionListener(this);
		b3.addActionListener(this);
		b4.addActionListener(this);
		b5.addActionListener(this);
		b6.addActionListener(this);
		b7.addActionListener(this);
		b8.addActionListener(this);
	  	b9.addActionListener(this);
		b0.addActionListener(this);
		
		add = new Button("+");
		add.setSize(25,25);
		add.addActionListener(this);
		add (add);

		subtract = new Button("-");
		subtract.setSize(25,25);
		subtract.addActionListener(this);
		add (subtract);

		multiply = new Button("*");
		multiply.setSize(25,25);
		multiply.addActionListener(this);
		add (multiply);

		divide = new Button("/");
		divide.setSize(25,25);
		divide.addActionListener(this);
		add(divide);

		result = new TextField("Output Here");
		result.setEditable(false);
		add (result);



	}

	// public void start()
	// {

	// }

	// public void stop()
	// {

	// }

	// public void destroy()
	// {

	// }

	// @Override
	public void paint(Graphics g)
	{

		g.setColor(Color.CYAN);
		g.drawString("Hello World!", 10, 10);
	}

	public void actionPerformed(ActionEvent e)
	{
		
	}
}

//http://javacodesme.blogspot.com/2013/12/simple-calculator-using-applet.html
