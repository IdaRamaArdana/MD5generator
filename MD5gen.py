import hashlib

def generate_md5(text):
    """
    Generates the MD5 hash of the given text.

    :param text: The input text to hash.
    :return: The MD5 hash of the input text as a hexadecimal string.
    """
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the input text
    md5_hash.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    return md5_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    input_text = input("Enter the text to generate MD5 hash: ")
    md5_hash = generate_md5(input_text)
    print(f"MD5 hash: {md5_hash}")
