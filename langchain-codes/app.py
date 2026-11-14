from chains.coding_chain import coding_chain


def show_menu():
    print("Choose an option")
    print("""
    1. Ask coding question
    2. Generate code
    3. Explain code
    """)

def get_user_choice(choice):
    if choice == "1":
        return input("Enter your coding question: ")

    elif choice == "2":
        return input("Describe the code you want me to generate")

    elif choice == "3":
        return input("Enter the code you want me to explain")

    return None

def main():
    print("=" * 70)
    print("AI Coding Assistant")
    print("Type 'exit' to quit")
    print("=" * 70)
    
    while True:
        show_menu()
        choice = input("Enter your choice : ")
        question = get_user_choice(choice)
        if question.lower() == 'exit' or question.lower() == 'quit':
            print("Thank you for using AI Coding Assistant")
            break

        print("Generating Response")
        print("=" * 70)
        
        task_map = {
            "1": "Answer programming question",
            "2": "Generate production ready source code",
            "3": "Explain the given source code in detail"
        }
        
        response = coding_chain.invoke(
            {
                "task": task_map[choice],
                "question": question
            }
        )
        print(response)

if __name__ == "__main__":
    main()