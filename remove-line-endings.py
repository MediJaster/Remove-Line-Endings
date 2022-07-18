def get_string(filename):
    file = open(filename, "rt")
    text = file.read()
    file.close()

    return text

def remove_endl(string):
    return string.replace("\n", "")

def write_compressed_string(string, filename):
    file = open(filename, "w")
    file.write(string)
    file.close()

write_compressed_string((remove_endl(get_string("string.txt"))), "string_compressed.txt")

