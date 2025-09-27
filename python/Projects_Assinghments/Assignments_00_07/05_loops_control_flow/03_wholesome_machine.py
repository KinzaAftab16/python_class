AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("🌟 Let's practice a positive affirmation!")
    print(f"Please type the following affirmation exactly as shown:\n\n\"{AFFIRMATION}\"\n")

    user_feedback = input("Your input: ")

    while user_feedback != AFFIRMATION:
        print("\n❌ That wasn't quite right. Let's try again!")
        print(f"\nPlease type the affirmation:\n\"{AFFIRMATION}\"\n")
        user_feedback = input("Your input: ")

    print("\n✅ That's right! You nailed it! Keep believing in yourself. 💪")

if __name__ == '__main__':
    main()
