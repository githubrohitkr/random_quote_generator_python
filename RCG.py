import random

def get_user_name():
    name = input("Enter your name: ")
    return name

def get_quote_category():
    categories = ["motivation", "success", "life", "love"]
    print("Select a category for the quote:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category.capitalize()}")
    
    while True:
        choice = input("Enter the number of the category: ")
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a valid number.")

def get_random_quote(category):
    quotes = {
        "motivation": [
            "The future belongs to those who believe in the beauty of their dreams. - {name}",
            "You are never too old to set another goal or to dream a new dream. - {name}",
            "Believe you can and you're halfway there. - {name}"
        ],
        "success": [
            "Success is not final, failure is not fatal: It is the courage to continue that counts. - {name}",
            "Success is not the key to happiness. Happiness is the key to success. - {name}",
            "The only place where success comes before work is in the dictionary. - {name}"
        ],
        "life": [
            "In the end, it's not the years in your life that count. It's the life in your years. - {name}",
            "Life is really simple, but we insist on making it complicated. - {name}",
            "Life is 10% what happens to us and 90% how we react to it. - {name}"
        ],
        "love": [
            "The best thing to hold onto in life is each other. - {name}",
            "Love is composed of a single soul inhabiting two bodies. - {name}",
            "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves. - {name}"
        ]
    }
    
    return random.choice(quotes[category])

def add_user_quote(category):
    quote = input(f"Enter your quote for the '{category}' category: ")
    if category not in user_quotes:
        user_quotes[category] = []
    user_quotes[category].append(quote)

def main():
    print("Welcome to the Inspirational Quote Generator!")
    name = get_user_name()
    category = get_quote_category()

    quote = get_random_quote(category)
    if category in user_quotes:
        quote = random.choice(user_quotes[category])
    else:
        quote = get_random_quote(category)
        
    personalized_quote = quote.format(name=name)
    
    print("\nHere's your personalized quote:")
    print(personalized_quote)

    contribute = input("Would you like to contribute your own quote? (yes/no): ").lower()
    if contribute == "yes":
        add_user_quote(category)
        print("Thank you for contributing your quote!")

if __name__ == "__main__":
    user_quotes = {}  # To store user-contributed quotes
    main()
