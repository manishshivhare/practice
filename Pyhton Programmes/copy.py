import pyperclip
import socket


def get_ip_address():
    # Retrieve the IP address of the PC
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


def send_to_smartphone(text):
    ip_address = get_ip_address()
    # Replace <YOUR_SMARTPHONE_IP> with the IP address of your smartphone
    smartphone_ip = "2405:201:602c:4036:89d8:d563:f6fa:ce2e"
    port = 12345  # Choose any available port number

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((smartphone_ip, port))
        s.sendall(text.encode())

    print(f"Text sent to smartphone at IP address: {smartphone_ip}")


def main():
    text = pyperclip.paste()
    send_to_smartphone(text)


if __name__ == "__main__":
    main()
