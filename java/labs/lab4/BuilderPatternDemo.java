import java.util.ArrayList;
import java.util.List;

interface Item {
   public String name();
   public Packing packing();
   public float price();	
}



interface Packing {
  public String pack();
}



class Wrapper implements Packing {

   public String pack() {
      return "Wrapper";
   }
}

class Bottle implements Packing {

   public String pack() {
      return "Bottle";
   }
}

abstract class Burger implements Item {

   
   public Packing packing() {
      return new Wrapper();
   }

   
   public abstract float price();
}

abstract class ColdDrink implements Item {

	public Packing packing() {
       return new Bottle();
	}

	public abstract float price();
}

class VegBurger extends Burger {

   public float price() {
      return 25.0f;
   }

   public String name() {
      return "Veg Burger";
   }
}


class ChickenBurger extends Burger {

   public float price() {
      return 50.5f;
   }

   public String name() {
      return "Chicken Burger";
   }
}

class Coke extends ColdDrink {

   public float price() {
      return 30.0f;
   }

   public String name() {
      return "Coke";
   }
}


class Pepsi extends ColdDrink {

   public float price() {
      return 35.0f;
   }

   public String name() {
      return "Pepsi";
   }
}


class Meal {
   private List<Item> items = new ArrayList<Item>();	

   public void addItem(Item item){
      items.add(item);
   }

   public float getCost(){
      float cost = 0.0f;
      
      for (Item item : items) {
         cost += item.price();
      }		
      return cost;
   }

   public void showItems(){
   
      for (Item item : items) {
         System.out.print("Item : " + item.name());
         System.out.print(", Packing : " + item.packing().pack());
         System.out.println(", Price : " + item.price());
      }		
   }	
}

class MealBuilder {

   public Meal prepareVegMeal (){
      Meal meal = new Meal();
      meal.addItem(new VegBurger());
      meal.addItem(new Coke());
      return meal;
   }   

   public Meal prepareNonVegMeal (){
      Meal meal = new Meal();
      meal.addItem(new ChickenBurger());
      meal.addItem(new Pepsi());
      return meal;
   }
}
public class BuilderPatternDemo {
   public static void main(String[] args) {
   
      MealBuilder mealBuilder = new MealBuilder();

      Meal vegMeal = mealBuilder.prepareVegMeal();
      System.out.println("Veg Meal");
      vegMeal.showItems();
      System.out.println("Total Cost: " + vegMeal.getCost());

      Meal nonVegMeal = mealBuilder.prepareNonVegMeal();
      System.out.println("\n\nNon-Veg Meal");
      nonVegMeal.showItems();
      System.out.println("Total Cost: " + nonVegMeal.getCost());
   }
}


