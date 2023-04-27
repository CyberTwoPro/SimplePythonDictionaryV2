import tkinter as tk

def click():
    entered_text = entry.get().lower()  # collect text from text entry box and convert to lowercase
    output.delete(1.0, tk.END)  # clear text box
    try:
        definition = my_glossary[entered_text]
        word_count_label.config(text=f"Words: {len(definition.split())}")  # update word count label
    except KeyError:
        definition = "404. Error. There is no entry for this word."
        word_count_label.config(text="Words: 0")  # update word count label
    output.insert(tk.END, definition)

# Main Window
window = tk.Tk()
window.title("PixelApps | BETA | Dictionary Python V0.2")
window.geometry("600x580")
window.resizable(False, False)
window.configure(background="#292D36")
window.iconbitmap("img.ico")

# Create a Label
label = tk.Label(window, text="Enter the word you want defining:", font=("Helvetica", 16), fg="#FFFFFF", bg="#292D36")
label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

# Create a Text Entry Box
entry = tk.Entry(window, width=30, font=("Helvetica", 14), bg="#FFFFFF", fg="#292D36", bd=0)
entry.grid(row=1, column=0, padx=20, pady=10, sticky="w")

# Create a Label to show number of words in definition
word_count_label = tk.Label(window, text="Words: 0", font=("Helvetica", 14), fg="#FFFFFF", bg="#292D36")
word_count_label.grid(row=1, column=1, padx=20, pady=10, sticky="w")

# Add a Submit Button
submit_button = tk.Button(window, text="SUBMIT", width=10, font=("Helvetica", 14), bg="#007FFF", fg="#FFFFFF", bd=0, command=click)
submit_button.grid(row=2, column=0, padx=20, pady=20, sticky="w")

# Create another Label
definition_label = tk.Label(window, text="\nDefinition:", font=("Helvetica", 16), fg="#FFFFFF", bg="#292D36")
definition_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")

# Create a Text Box
output = tk.Text(window, width=40, height=10, font=("Helvetica", 14), bg="#FFFFFF", fg="#292D36", bd=0, wrap="word")
output.grid(row=4, column=0, padx=20, pady=10, sticky="w")

# The dictionary:
my_glossary = {
    "newai": "You found it! The BEST coding school ever! NewAI.com.au",
    "algorithm": "A set of instructions for solving a problem or accomplishing a task.",
    "bug": "An error in a program that prevents it from running as expected.",
    "cache": "A small amount of memory used by a computer to store frequently accessed data.",
    "database": "An organized collection of data that can be accessed and managed electronically.",
    "encryption": "The process of converting data into a secret code to prevent unauthorized access.",
    "firewall": "A security system that monitors and controls incoming and outgoing network traffic.",
    "HTML": "Hypertext Markup Language. A standard language used for creating web pages.",
    "JavaScript": "A programming language used for creating interactive web pages.",
    "kernel": "The central part of an operating system that manages system resources.",
    "Linux": "A popular open-source operating system used in servers, supercomputers, and other systems.",
    "malware": "Malicious software designed to harm a computer system.",
    "network": "A group of computers and devices connected together to share resources and information.",
    "operating system": "The software that controls a computer's hardware and manages its resources and operations.",
    "programming language": "A language used to create software and other computer programs.",
    "RAM": "Random Access Memory. A type of computer memory that can be accessed randomly.",
    "server": "A computer system that provides resources or services to other computers or devices on a network.",
    "TCP/IP": "Transmission Control Protocol/Internet Protocol. A set of protocols used for communication over the internet.",
    "USB": "Universal Serial Bus. A standard for connecting devices to a computer.",
    "virus": "A type of malware that spreads by infecting other programs or files.",
    "Wi-Fi": "Wireless Fidelity. A technology used for wireless networking.",
    "XML": "Extensible Markup Language. A language used for creating structured documents.",
    "ZIP file": "A compressed file format used for archiving and distributing files.",
    "API": "Application Programming Interface. A set of protocols, routines, and tools for building software applications.",
    "bandwidth": "The maximum amount of data that can be transmitted over a network or internet connection.",
    "cookie": "A small piece of data stored on a user's computer by a web browser.",
    "domain name": "A unique name that identifies a website on the internet.",
    "email": "Electronic mail. A system for sending and receiving messages over the internet.",
    "firewire": "A type of high-speed data transfer technology used for connecting devices to a computer.",
    "GUI": "Graphical User Interface. A type of interface that allows users to interact with a computer using graphical elements.",
    "HTTP": "Hypertext Transfer Protocol. A protocol used for communication between web browsers and servers.",
    "icon": "A small graphical representation of a program or file.",
    "JavaScript library": "A collection of pre-written JavaScript code that can be reused in web development.",
    "keyboard shortcut": "A combination of keys that perform a specific action in a software program.",
    "Linux distribution": "A version of the Linux operating system packaged with additional software and tools.",
    "metadata": "Data that describes other data, such as the author and date of creation of a file.",
    "NIC": "Network Interface Card. A hardware component used to connect a computer to a network.",
    "open source": "Software that is freely available and can be modified and distributed.",
    "interactive mode": "This is when we use IDLE to try out snippets of code without saving them.",
    "GUI": "Graphical User Interface. A window with buttons and text entry boxes is an example of a graphical user interface.",
    "tuple": "An ordered container data type whose values are indexed from 0. Its contents cannot be changed.",
    "widget": "An element of a GUI such as a button or text entry box.",
    "open source": "Software that is freely available and can be modified and distributed.",
    "algorithm": "A set of instructions designed to solve a specific problem or perform a specific task.",
    "cloud computing": "The delivery of computing services, including servers, storage, databases, networking, software, analytics, and intelligence, over the Internet.",
    "cybersecurity": "The practice of protecting computer systems and networks from digital attacks, theft, and damage.",
    "machine learning": "A subset of artificial intelligence that involves training machines to learn from data and improve over time.",
    "blockchain": "A decentralized digital ledger used to record transactions across many computers.",
    "big data": "Extremely large data sets that can be analyzed to reveal patterns, trends, and associations.",
    "augmented reality": "The overlaying of digital information onto the real world.",
    "virtual reality": "A simulated experience that can be similar to or completely different from the real world.",
    "Internet of Things (IoT)": "The interconnectivity of physical devices, vehicles, buildings, and other objects that are embedded with sensors, software, and network connectivity.",
    "artificial intelligence": "The simulation of human intelligence in machines that are programmed to think and act like humans.",
    "natural language processing": "The ability of computers to interpret and understand human language.",
    "user experience (UX)": "The overall experience a user has while interacting with a product or service, including ease of use, accessibility, and satisfaction.",
    "user interface (UI)": "The visual and interactive components of a product or service that a user interacts with, such as buttons and menus."
}

# Run Main Loop
window.mainloop()
