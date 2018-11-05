interface shape {
	public void draw();
		}

class rectangle implements shape {
	public void draw() {
		System.out.println(" Inside Rectangle :: draw() method ");
		}
	}

class square implements shape {
	public void draw() {
		System.out.println(" Inside Square :: draw() method ");
		}
	}

class circle implements shape {
	public void draw() {
		System.out.println(" Inside Circle :: draw() method ");
		}
	}

interface color {
	public void fill();
	}

class red implements color {
	public void fill() {
		System.out.println(" Inside Red :: fill() method ");
		}
	}

class green implements color {
	public void fill() {
		System.out.println(" Inside Green :: fill() method ");
		}
	}

class blue implements color {
	public void fill() {
		System.out.println(" Inside Blue :: fill() method ");
		}
	}

abstract class AbstractFactory {
	abstract color getcolor(String c);
	abstract shape getshape(String s);
			}

class shapefactory extends AbstractFactory {
	shape getshape(String s) {
		if(s==null)
			return null;
		if(s.equalsIgnoreCase("Circle"))
			return new circle();
		if(s.equalsIgnoreCase("Square"))
			return new square();
		if(s.equalsIgnoreCase("rectangle"))
			return new rectangle();
		return null;
		}
	
		color getcolor(String s) {
			return null;
			}
				
	}

class colorfactory extends AbstractFactory {
	color getcolor(String s) {
		if(s==null)
			return null;
		if(s.equalsIgnoreCase("Red"))
			return new red();
		if(s.equalsIgnoreCase("Blue"))
			return new blue();
		if(s.equalsIgnoreCase("Green"))
			return new green();
		return null;
		}
	shape getshape(String s) {
		return null;
		}
	}


class fp {
	public static AbstractFactory getFactory(String s) {
		if(s.equalsIgnoreCase("shape"))
			return new shapefactory();
		if(s.equalsIgnoreCase("color"))
			return new colorfactory();
		return null;
		}
	}


public class am {
	public static void main(String args[]) {
		AbstractFactory f1 = fp.getFactory("Shape");
		shape s1=f1.getshape("Circle");
		s1.draw();
		shape s2=f1.getshape("rectangle");
		s2.draw();
		shape s3=f1.getshape("Square");
		s3.draw();
		AbstractFactory cf=fp.getFactory("Color");
		color c1=cf.getcolor("red");
		c1.fill();
		color c2=cf.getcolor("blue");
		c2.fill();
		color c3 = cf.getcolor("green");
		c3.fill();
	}
	}



















































