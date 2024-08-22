# Banking System Simulation Application

## Overview

This is a **Banking System Simulation Application** designed to help **teenagers and young adults** understand the fundamental concepts of banking operations. The application allows users to simulate typical banking activities such as **depositing, withdrawing, and managing multiple types of bank accounts**. Additionally, the application includes a **special budget feature** that assists users in managing their finances more effectively by setting and tracking spending limits.

The entire project is implemented in **Python**, making it easily extendable and simple for beginners to understand and use.

## Features

### 1. **Account Types**
   - **Savings Account**: An account designed for long-term savings with an emphasis on maintaining a positive balance.
   - **Checking Account**: An account that can be used for everyday transactions with no withdrawal limits.
   - **Youth Account**: A specialized account for teenagers with limited features to promote responsible financial behavior.

### 2. **Basic Banking Operations**
   - **Deposit**: Users can deposit money into any account.
   - **Withdraw**: Users can withdraw money from any account, subject to account type rules.
   - **Account Balance Check**: Users can view the current balance of their accounts.

### 3. **Budget Feature**
   - **Set Budget**: Users can define a monthly budget for different spending categories (e.g., entertainment, food, etc.).
   - **Track Expenses**: The system will keep track of expenses and compare them to the set budget.
   - **Alerts**: Notifications when approaching or exceeding the budget for a specific category.

### 4. **Simulation of Real-World Banking Scenarios**
   - **Overdraft Protection**: For checking accounts, users can experience overdraft protection scenarios.
   - **Interest Calculation**: Savings accounts will have interest applied monthly based on the balance.
   - **Transaction History**: Users can view their past deposits, withdrawals, and other account activities.

## How to Use

1. **Install Python**: Ensure that Python is installed on your machine. This project requires Python 3.x.
2. **Clone the Repository**: Clone the project from the repository to your local machine.
    ```bash
    git clone <repository-url>
    ```
3. **Install Dependencies**: Install the required dependencies by running the following command:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Application**: Start the application by running the `main.py` file.
    ```bash
    python main.py
    ```

## Project Structure

- **main.py**: The entry point for the application.
- **banking.py**: Contains the logic for banking operations such as deposits, withdrawals, and account management.
- **budget.py**: Manages the budget-related features including setting budgets, tracking expenses, and providing alerts.
- **utils.py**: Utility functions for handling common tasks like formatting and data validation.
- **data/**: Folder containing user data and transaction history (if persistent data storage is implemented).
- **tests/**: Contains unit tests for various components of the application.

## Future Enhancements

- **User Authentication**: Implement user login and session management for multiple users.
- **Graphical User Interface (GUI)**: Develop a GUI using a library such as Tkinter or PyQt for a more user-friendly experience.
- **Investment Accounts**: Add simulation features for investment accounts such as stocks, bonds, and mutual funds.
- **Mobile Compatibility**: Expand the application to run as a mobile app using frameworks like Kivy.

## Contribution

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or feedback, feel free to reach out at:
- **Email**: support@bankingsimulation.com
- **GitHub Issues**: Open an issue on the repository page.

---

This project aims to foster financial literacy among young users by providing a practical and interactive way to learn about banking and budgeting in a safe and controlled environment.

---

