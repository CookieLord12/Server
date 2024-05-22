# Server-Manager
# Introduction
## What is my application?
My program was made for my specific purpose of making it easier to start and monitor my server, while I am away. The main function of this program is to send commands via ssh and run other server programs. It is also possible for other people to connect to the server and use this program with appropriate passwords.
## How to run the program?
To run the program, first the user must download OpenSSH Client and OpenSSH Server to the respective PCs and the libraries used by the python code (paramiko, psutil). The program is run by ‘Connect.py’ file. Also, the user is required to have hostname, username, password of the PC it is trying to connect to in a file named ‘pass.txt’ in such format, in a folder named ‘logs’ on desktop:

![paveikslas](https://github.com/CookieLord12/Server/assets/65421355/f738a9d7-7ea9-4bf2-a8d2-47b4a6fd14dc)


## How to use the program?
If the requirements are met the program will start and give you a choice between however many commands are prepared in the code (in this example there are 4) and you pick the command you want to run by typing in the appropriate number in the command prompt. Afterwards the actions and results are saved into the ‘logs’ folder on both computers.
# Body/Analysis
## Four Pillars of OOP
### Encapsulation:
1. Encapsulation is evident in the SSHCommandExecutor class, where the details of the SSH connection (hostname, username, password) are hidden within the class. Users interact with this class through the execute method without needing to understand the inner workings of the SSH connection.
1. Example:

![paveikslas](https://github.com/CookieLord12/Server/assets/65421355/ef982172-2038-4df4-b2a7-4df242df911b)

1. Here, hostname, username, and password are encapsulated within the SSHCommandExecutor class.
### Abstraction:
- The CommandExecutor class provides an abstraction for command execution. It defines a common interface (execute method) that all concrete command executors must implement.
- Example:
- 
![paveikslas](https://github.com/CookieLord12/Server/assets/65421355/6da29de3-ad56-4f7c-be07-164c7e48aff8)

- This abstract class ensures that any subclass will implement the execute method, providing a unified interface for executing commands.
### Inheritance:
- Inheritance is used where SSHCommandExecutor inherits from the CommandExecutor base class. This allows SSHCommandExecutor to inherit the interface contract defined by CommandExecutor.
- Example:

![paveikslas](https://github.com/CookieLord12/Server/assets/65421355/03d2708d-3c73-44e1-b339-e68bc163f443)

- SSHCommandExecutor inherits from CommandExecutor and implements the execute method.
### Polymorphism:
- Polymorphism is demonstrated through the use of the execute method. Regardless of the specific type of CommandExecutor (in this case, SSHCommandExecutor), the execute method can be called, and it will behave according to the implementation in the subclass.
- Example:

![paveikslas](https://github.com/CookieLord12/Server/assets/65421355/c078ed4b-b6dc-4719-b5c4-b17844095ae6)
![paveikslas](https://github.com/CookieLord12/Server/assets/65421355/3410a9d6-69c0-4211-a52e-6e38556379bc)

- The create\_executor method encapsulates the instantiation logic of SSHCommandExecutor.

## Design Patterns
### Factory Method:
1. The CommandExecutorFactory class uses the Factory Method pattern to create instances of CommandExecutor. This pattern is used to encapsulate the creation logic of SSHCommandExecutor, making the code more modular and easier to extend.
1. Example:

![paveikslas](https://github.com/CookieLord12/Server/assets/65421355/68be2daf-2004-4799-ad91-b1d32b1d949b)
![paveikslas](https://github.com/CookieLord12/Server/assets/65421355/35807fc8-3919-4ad8-859b-32c30eb58120)

1. The create\_executor method encapsulates the instantiation logic of SSHCommandExecutor.
### Strategy:
- The command execution logic can be seen as following the Strategy pattern, where different command strings are executed based on user input, allowing the strategy (command) to be selected at runtime.
- Example:

![paveikslas](https://github.com/CookieLord12/Server/assets/65421355/2485de1d-fc33-416e-958b-a1661355b7a0)

- Here, the specific command executed varies based on the user's choice, illustrating the Strategy pattern.
# Results
- The program performs its main purpose well when used correctly. It can send any command and new commands can be added easily.
- Many issues derived from configuration of firewall or admin privileges. They were not fixed entirely, but rather other ways were found to correct errors.
- The program can still be improved, and it has not yet been implemented in my personal server due to hardware issues. Because of this I could only make simple commands to demonstrate the use of this program.
# Conclusions
My code effectively uses the principles of Object-Oriented Programming and design patterns. Encapsulation is used to hide implementation details, abstraction defines common interfaces, inheritance allows code reuse, and polymorphism enables flexibility in using different command executors. The Factory Method pattern is used to create command executors, and the Strategy pattern is seen in the command selection logic. Currently I am working on fixing the hardware issues on my personal server so that the prototype could be properly tested. The end goal is to make it possible for the server to be easily controlled from any device with appropriate login information and for the program to be intuitive and easy to install. 
