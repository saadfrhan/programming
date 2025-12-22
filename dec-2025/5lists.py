languages = ["javascript", "c", "python", "rust", "go"]

print([language for language in languages])
print(languages[0])
print(languages[-1])
print(languages[0:3])
languages.append("c")
languages.append("php")
print([language for language in languages])
languages.remove("c")
print([language for language in languages])
