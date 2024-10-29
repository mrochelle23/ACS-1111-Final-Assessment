# Coffee Ordering System

A simple coffee ordering system implemented in Python that allows customers to place drink orders through a barista. This program demonstrates the use of object-oriented programming (OOP) principles, including classes, inheritance, and method definitions.

## Features

- Create `Person` instances representing customers.
- Each `Person` can create an order for their favorite drink.
- The `CoffeeBar` class manages a list of orders.
- A `Barista` class that inherits from `Person` and can process orders.

## Classes

1. **Person**: Represents a customer with a name and favorite drink.
   - Method: `my_order()` to create an order.

2. **Order**: Represents an order placed by a person.
   - Method: `to_string()` to return a formatted string of the order.

3. **CoffeeBar**: Represents a coffee shop that processes orders.
   - Method: `place_order(order)` to add an order to the list.
   - Method: `process_orders()` to print all orders processed by the barista.

4. **Barista**: Inherits from `Person` and represents a barista with a greeting message.

## Installation

To run this project, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/mrochelle23/ACS-1111-Final-Assessment.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CoffeeOrderingSystem
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## Usage

Once you run the program, it will create instances of customers (Amy, Bob, and Cat) and a barista (Kevin). The customers will place their drink orders, and the barista will process and print out the orders in the console.

Example output:

```
Kevin Amy orders: Coffee
Kevin Bob orders: Tea
Kevin Cat orders: Milk
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your changes.

## Acknowledgments

- Inspired by object-oriented programming concepts.
- Thanks to all open-source contributors for their valuable resources.
