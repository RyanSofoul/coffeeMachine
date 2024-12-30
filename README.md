# Coffee Machine Project
This Python-based coffee machine simulates a real-world coffee maker, allowing users to choose from a variety of drinks, check available resources, process payments, and serve the drink while tracking profit and ingredients. It's a simple and interactive way to understand basic operations like resource management and transaction processing.

# Features
Menu: Choose between espresso, latte, and cappuccino.
Resource Management: Tracks water, milk, and coffee resources. Alerts the user if ingredients run low.
Payment System: Users can input coins (quarters, dimes, nickels, and pennies) to make a purchase.
Profit Tracking: Keeps track of the money earned by the coffee machine.
Report Function: View the current status of resources and profit.
Interactive: Command-line interface where users can interact with the coffee machine.

# Installation
1. Clone this repository to your local machine:
```
git clone https://github.com/RyanSofoul/coffeeMachine.git
```
2. Ensure Python 3 is installed on your system.

3. Run the project:
```
python main.py
```
# Usage
Upon running the program, you'll be prompted to choose a drink.
The machine will check if there are enough resources to make the drink.
You’ll be asked to input coins to pay for the drink.
If payment is sufficient, the machine will prepare the drink and provide change if needed.
You can type report at any time to view the current resources and profit.
To turn off the machine, type off.

# Example
```
What would you like?: (espresso/latte/cappuccino): latte
Please input coins.
How many quarters?: 2
How many dimes?: 1
How many nickels?: 1
How many pennies?: 3
Here is $0.1 dollars in change.
Here is your latte. Enjoy!
```
# Functions
resource_check(ingredients): Checks if there are enough resources to prepare the selected drink.
process_coins(): Prompts the user to input coins and calculates the total amount.
transaction_success(money_entered, cost): Verifies if the entered money is enough for the selected drink.
make_coffee(drink, ingredients): Deducts the ingredients from the machine's resources and serves the drink.

# Contributing
Feel free to fork this project, make changes, and create a pull request. Contributions are welcome!

# License
This project is open-source and available under the MIT License.
