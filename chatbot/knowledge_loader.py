import os

def load_company_knowledge():

    current_dir = os.path.dirname(__file__)

    folder = os.path.join(current_dir, "company_knowledge")

    knowledge = ""

    if not os.path.exists(folder):
        return "No company knowledge available."

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        with open(path, "r", encoding="utf-8") as f:
            knowledge += f.read() + "\n"

    return knowledge    