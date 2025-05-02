For this project, I made 3 classes, Bistro_system, custom_order, and drink. Drink just stores the basic attributes of a drink, and does not use other data types. In custom_order, I store all of the details of each order. In bistro_system, I have the logic of the actual program. It uses a hashmap to store the menu, since I wanted to be able to use the name of the drink as the index, and have the items be drinks. I use a linked list to store the list of pending orders, and the list of completed orders, since I wanted a data structure where it was efficient to pop the first item, and where I could also iterate through it when necessary. the comlexity of looping through the list is linear, and the complexity of popping the first element should be constant. The instructions to run the program are to run the program.py file, and follow the instructions that it tells you to do. I made it so that rather then entering the number of the drink, you enter the name of the drink itself while ordering. If I had more time, I would have implemented different prices for the different sizes of the drinks, and better customizations. Additionally, some of the printing of information is a little clunky. Another limitation is that I didn't complete code for if the user enters the wrong name, or a chracter that is not included.

Example:
ordering a drink:
Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as complete
5. View end of day report
6. Exit
2
Enter what you want:
Drip Coffee
What size do you want it?
large
Any custom instructions?
No cream
what is your name?
Noah


displaying orders:
Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as complete
5. View end of day report
6. Exit
3
item: Drip Coffee
cost: $2.5
size: large
customization: No cream
name: Noah

Marking as complete, and end of day report:
Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as complete
5. View end of day report
6. Exit
4


Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as complete
5. View end of day report
6. Exit
5
Bannana Milk    Quanitity sold: 0       Total Sales: $0
Calpico Lemonade        Quanitity sold: 0       Total Sales: $0
Coconut Milk Tea Latte  Quanitity sold: 0       Total Sales: $0
Drip Coffee     Quanitity sold: 1       Total Sales: $2.5
Golden Milk Latte       Quanitity sold: 0       Total Sales: $0
Total Revenue: $2.5


Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as complete
5. View end of day report
6. Exit
