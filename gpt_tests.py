'''Testing Code from ChatGPT'''

def main_loop():
    while True:
        # Your while loop logic
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            print("You chose option 1.")
            # Set the boolean condition to False to exit the loop
            break
        elif choice == "2":
            print("You chose option 2.")
            # Call another function here
            another_function()
        else:
            print("Invalid choice. Please try again.")

def another_function():
    print("Inside another function.")
    main_loop()
    # Perform some other tasks

# Call the main loop function to start the program
main_loop()

# After the main loop ends, you can continue with other code here
print("Program continued after the main loop.")
