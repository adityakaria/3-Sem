interface shape {
	public void draw();
		}

class rectangle implements shape {
	public void draw() {
		System.out.println(" Inside rectangle :: draw() method ");
			}
	}

class circle implements shape {
	public void draw() {
		System.out.println(" Inside Circle :: draw() method ");
		}
	}

class square implements shape {
	public void draw() {
		System.out.println(" Inside Square :: draw() method ");
		}
	}

class shapefactory {
	public shape getShape(String a) {
		if(a==null)
			return null;
		if(a.equalsIgnoreCase("rectangle"))
			return new rectangle();
		if(a.equalsIgnoreCase("square"))
			return new square();
		if(a.equalsIgnoreCase("circle"))
			return new circle();
		return null;
		}
	}

public class fp {
	public static void main(String args[]) {
		shapefactory s1 = new shapefactory();
		shape sh1 = s1.getShape("square");
		sh1.draw();
		shape sh2 = s1.getShape("rectangle");
		sh2.draw();
		shape sh3=s1.getShape("circle");
		sh2.draw();
		}
	}
	
