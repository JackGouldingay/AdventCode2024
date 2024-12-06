def load_data(file):
    contents = open(file).read().split("\n")
    output = []
    for i in contents:
        output.append(i.split(" "))

    return output