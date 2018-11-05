import java.io.*; 

class bufferio
{
	public static void main(String[] args)throws IOException
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		String s = in.readLine();
		char c = in.readLine().charAt(0);
		int i = Integer.parseInt(in.readLine());
		float f = Float.parseFloat(in.readLine());
		boolean b = true;

		System.out.println(s);
		System.out.println(c);
		System.out.println(i);
		System.out.println(f);
		System.out.println(b);

	}
}