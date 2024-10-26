import threading

WORDS = ['science', 'computer', 'student', 'newhacks', 'mac', 'apple',
         'tree', 'basketball', 'football', 'soccer', 'hacker', 'hat',
         'headphones', 'camera', 'word', 'easy', 'difficult', 'funny',
         'water', 'orange']

def game():
    print("Agent X! You need to pass Ginky Co's standardized typing tests to follow through with your mission."
          "\nType each word which appears on "
          "your device before you run out of time. Type 'ready' to begin...")
    if input("").strip().lower() == 'ready':
        words()
    else:
        exit()

def words():
    for word in WORDS:
        answer = timer(word, 3)
        if answer.strip().lower() != word:
            print("WRONG")
            exit()


def timer(wordie, time):
    print(f"Word: {wordie}")
    user_input = [None]

    def get_input():
        user_input[0] = input()

    input_thread = threading.Thread(target=get_input)
    input_thread.start()

    input_thread.join(time)

    if input_thread.is_alive():
        print("\nYOU RAN OUT OF TIME!!")
        return ""
    else:
        return user_input[0]

game()
