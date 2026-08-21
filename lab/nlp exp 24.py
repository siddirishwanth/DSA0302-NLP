def dialog_act(sentence):
    s = sentence.lower().strip()

    if any(word in s for word in ["hello", "hi", "hey"]):
        return "Greeting"

    elif any(word in s for word in ["bye", "goodbye"]):
        return "Goodbye"

    elif "thank" in s:
        return "Thanking"

    elif s.endswith("?"):
        return "Question"

    elif any(word in s for word in ["please", "can you", "could you"]):
        return "Request"

    elif any(word in s for word in ["yes", "no", "okay", "sure"]):
        return "Confirmation"

    else:
        return "Statement"

print("Enter dialog lines.")
print("Type 'stop' to finish.\n")

while True:
    sentence = input("User: ")

    if sentence.lower() == "stop":
        break

    print("Dialog Act:", dialog_act(sentence))
