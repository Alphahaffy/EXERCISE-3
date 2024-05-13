import java.util.Scanner;

public class Fighter {
    private String name;
    private int health;
    private int attackPower;

    public Fighter(String name, int health, int attackPower) {
        this.name = name;
        this.health = health;
        this.attackPower = attackPower;
    }

    public void attack(Fighter opponent) {
        opponent.health -= this.attackPower;
        System.out.println(this.name + " attacks " + opponent.name + " for " + this.attackPower + " damage!");
    }

    public boolean isAlive() {
        return this.health > 0;
    }

    public String getName() {
        return name;
    }

    public int getHealth() {
        return health;
    }

    public int getAttackPower() {
        return attackPower;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Fighter 1's name:");
        String name1 = scanner.nextLine();
        System.out.println("Enter Fighter 1's health:");
        int health1 = scanner.nextInt();
        System.out.println("Enter Fighter 1's attack power:");
        int attackPower1 = scanner.nextInt();

        System.out.println("Enter Fighter 2's name:");
        scanner.nextLine(); 
        String name2 = scanner.nextLine();
        System.out.println("Enter Fighter 2's health:");
        int health2 = scanner.nextInt();
        System.out.println("Enter Fighter 2's attack power:");
        int attackPower2 = scanner.nextInt();

        Fighter fighter1 = new Fighter(name1, health1, attackPower1);
        Fighter fighter2 = new Fighter(name2, health2, attackPower2);

        while (fighter1.isAlive() && fighter2.isAlive()) {
            System.out.println("It's " + fighter1.getName() + "'s turn. Press any key to attack!");
            scanner.nextLine(); 
            fighter1.attack(fighter2);
            if (!fighter2.isAlive()) break; 

            System.out.println("It's " + fighter2.getName() + "'s turn. Press any key to attack!");
            scanner.nextLine(); 
            fighter2.attack(fighter1);
        }

        if (fighter1.isAlive()) {
            System.out.println(fighter1.getName() + " wins!");
        } else {
            System.out.println(fighter2.getName() + " wins!");
        }

        scanner.close();
    }
}
