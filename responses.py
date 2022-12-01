import random

eating = "I don't like eating anything because I'm a bot"
advice = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Okay.",
                "Sorry I didn't got that?",
                "AI will take over the world"][
        random.randrange(5)]
    return response