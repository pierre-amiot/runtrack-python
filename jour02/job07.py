def dev_type(langage):
    if langage == "javascript":
        print("Tu es un développeur web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")
        dev_type("javascript")
dev_type("python")
dev_type("java")
dev_type("reactjs")
dev_type("ruby")