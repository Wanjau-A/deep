#  Implement a program that:
# Prompts the user to answer the great question of life,the universe, and everything
def main():
    answer = input("What is the answer to the great question of life,the universe, and everything? ")
# Outputs yes if user inputs 42 or case insensitive inputs forty-two,forty two
    result = mark(answer)
    print(result)


def mark(answer):
    answer_lower = answer.strip().lower()
    if answer_lower == "42" or answer_lower == "forty-two" or answer_lower == "forty two":
        return "Yes.Kudos!"
    else:
        return "Opss!No.Please try again."
    
if __name__ == "__main__":
    main()