from chatbot import chat
from summariser import summarise_notes
from quiz_generator import generate_quiz

print("=== SmartStudy Bot ===")

while True:

    print("\n1. Chat with StudyBot")
    print("2. Generate Quiz")
    print("3. Summarise Notes")
    print("0. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        chat()

    elif choice == "2":
        topic = input("Enter topic: ")
        n = input("Number of questions (default 5): ")
        n = int(n) if n.isdigit() else 5

        print("\nGenerating Quiz...\n")
        print(generate_quiz(topic, n))

    elif choice == "3":
        summarise_notes()

    elif choice == "0":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Try again.")