import base64

def encode_to_base64(text):
    encoded = base64.b64encode(text.encode('utf-8'))
    return encoded.decode('utf-8')

def decode_from_base64(b64_text):
    try:
        decoded = base64.b64decode(b64_text).decode('utf-8')
        return decoded
    except Exception as e:
        return f"Error: {e}"

while True:
    choice = input("\nChoose an option:\n1. Encode to Base64\n2. Decode from Base64\n3. Exit\n> ")

    if choice == '1':
        text = input("Enter the sentence to encode: ")
        print("Base64 Encoded:", encode_to_base64(text))

    elif choice == '2':
        b64_text = input("Enter the Base64 string to decode: ")
        print("Decoded Text:", decode_from_base64(b64_text))

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
