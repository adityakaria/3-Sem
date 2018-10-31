//Create a droid using OOP in Java

class droid
{
  int batteryLevel;

  public droid()
  {
    batteryLevel = 100;
  }

  public void activate()
  {
    System.out.println("Activated. How can I help you?");
    //battery discharging
    batteryLevel -= 5;
    System.out.println("Battery level is: " + batteryLevel + " percent.");
  }

  public void chargeBattery(int hours)
  {
    System.out.println("Droid charging...");
    batteryLevel += hours;

    if (batteryLevel > 100) //to prevent overcharging
    {
      batteryLevel = 100;
    }

    System.out.println("Battery level is: " + batteryLevel + " percent.");
  }

  public int checkBatteryLevel()
  {
    System.out.println("Battery level is: " + batteryLevel + " percent.");
    return batteryLevel;
  }

  public void hover(int feet)
  {
    if (feet > 2)
      System.out.println("Error! I cannot hover above 2 feet.");
    else
      System.out.println("Hovering...");
      batteryLevel -= 20; //bsttery discharging
      System.out.println("Battery level is: " + batteryLevel + " percent.");
  }
}

class runner
{
	public static void main(String[] args)
 	{
    	droid myDroid = new droid();
		myDroid.activate();
    	myDroid.chargeBattery(5);
    	myDroid.hover(2);
	}
}