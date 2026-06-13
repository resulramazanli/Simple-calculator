# calculator.py

def safe_eval(expression):
    """Safely evaluate math expression."""
    try:
        # Only allow math operations
        allowed_chars = set('0123456789+-*/%().** ')
        if not all(c in allowed_chars for c in expression):
            return None
        
        result = eval(expression)
        return result
    except:
        return None

def main():
    history = []
    print("=== Simple Calculator ===")
    print("Commands: 'history', 'clear', 'quit'")
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            if user_input.lower() == 'history':
                if history:
                    print("\nCalculation History:")
                    for i, calc in enumerate(history, 1):
                        print(f"{i}. {calc}")
                else:
                    print("No history yet.")
                continue
            
            if user_input.lower() == 'clear':
                history = []
                print("History cleared.")
                continue
            
            result = safe_eval(user_input)
            if result is not None:
                print(f"= {result}")
                history.append(f"{user_input} = {result}")
            else:
                print("Invalid expression. Try: 5 + 3 * 2")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()