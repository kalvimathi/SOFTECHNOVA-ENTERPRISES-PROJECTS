
import java.util.Scanner;
import java.util.Random;

public class SD_JD_TASK3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        boolean playAgain = true;

        System.out.println("🎯 Welcome to the Enhanced Number Guessing Game!");

        while (playAgain) {
            System.out.println("\nChoose Difficulty Level:");
            System.out.println("1. Easy (1–50)");
            System.out.println("2. Medium (1–100)");
            System.out.println("3. Hard (1–200)");
            System.out.print("Enter your choice (1/2/3): ");

            int maxNumber = 100;
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    maxNumber = 50;
                    break;
                case 2:
                    maxNumber = 100;
                    break;
                case 3:
                    maxNumber = 200;
                    break;
                default:
                    System.out.println("⚠️ Invalid choice. Defaulting to Medium.");
            }

            int numberToGuess = random.nextInt(maxNumber) + 1;
            int attempts = 0;
            boolean guessedCorrectly = false;

            long startTime = System.currentTimeMillis();

            System.out.println("\nI am thinking of a number between 1 and " + maxNumber + "...");

            while (!guessedCorrectly) {
                System.out.print("Enter your guess: ");
                if (!scanner.hasNextInt()) {
                    System.out.println("❌ Invalid input! Please enter a number.");
                    scanner.next(); // clear invalid input
                    continue;
                }

                int userGuess = scanner.nextInt();
                attempts++;

                if (userGuess < 1 || userGuess > maxNumber) {
                    System.out.println("⚠️ Guess must be between 1 and " + maxNumber);
                    continue;
                }

                if (userGuess == numberToGuess) {
                    long timeTaken = (System.currentTimeMillis() - startTime) / 1000;
                    System.out.println("✅ Correct! You guessed it in " + attempts + " attempts and " + timeTaken + " seconds.");
                    guessedCorrectly = true;
                } else if (userGuess < numberToGuess) {
                    System.out.println("📉 Too low!");
                } else {
                    System.out.println("📈 Too high!");
                }

                // Hint after every 3 incorrect attempts
                if (!guessedCorrectly && attempts % 3 == 0) {
                    if (numberToGuess % 2 == 0) {
                        System.out.println("💡 Hint: The number is EVEN.");
                    } else {
                        System.out.println("💡 Hint: The number is ODD.");
                    }
                }
            }

            System.out.print("\n🔁 Do you want to play again? (yes/no): ");
            String response = scanner.next().trim().toLowerCase();
            playAgain = response.equals("yes") || response.equals("y");
        }

        System.out.println("🎮 Thanks for playing! Goodbye.");
        scanner.close();
    }
}
