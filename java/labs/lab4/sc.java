class SingleObject {
	private static SingleObject instance = new SingleObject();
	private SingleObject(){}
	public static SingleObject getInstance() {
		return instance;
				}

	public void showMessage	() {
		System.out.println("Hello World!");
		}
	}
public class sc {
	public static void main(String args[]) {
		SingleObject o1 =SingleObject.getInstance();
		o1.showMessage();
	}
}
