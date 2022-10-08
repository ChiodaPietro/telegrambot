from datetime import  datetime

def sample_responses(input_text):
    user_message= str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "hey how is it going?"

    if user_message in ("who are you", "who are you?"):
        return "i am your father"

    return "no man"