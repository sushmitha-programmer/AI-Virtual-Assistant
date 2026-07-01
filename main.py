from assistant import speak, take_command

def main():
    speak("Hello Sushmitha. I am your AI Virtual Assistant.")

    while True:
        command = take_command()

        if command == "":
            continue

        if "hello" in command:
            speak("Hello! How are you?")

        elif "your name" in command:
            speak("My name is Jarvis.")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I don't understand that command yet.")

if __name__ == "__main__":
    main()