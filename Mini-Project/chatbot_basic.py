from datetime import datetime

def chatbot():
    print("Halo! Saya adalah Chatbot sederhana. Apa yang ingin Anda tanyakan?")
    print("Ketik 'keluar' untuk mengakhiri percakapan.\n")

    while True:
        user_input = input("Anda: ").lower()

        if user_input == "keluar":
            print("Chatbot: Terima kasih telah berbicara dengan saya. Sampai jumpa!")
            break
        elif "nama kamu" in user_input:
            print("Chatbot: Nama saya adalah Chatbot Sederhana.")
        elif "apa kabar" in user_input:
            print("Chatbot: Saya hanya sebuah program, tapi saya baik-baik saja. Bagaimana dengan Anda?")
        elif "siapa presiden indonesia" in user_input:
            print("Chatbot: Presiden Indonesia saat ini adalah Joko Widodo.")
        elif "berapa 2 tambah 2" in user_input:
            print("Chatbot: 2 tambah 2 adalah 4.")
        elif "apa itu python" in user_input:
            print("Chatbot: Python adalah bahasa pemrograman yang populer dan mudah dipelajari.")
        elif "hari ini hari apa" in user_input:
            hari_ini = datetime.now().strftime("%A")
            print(f"Chatbot: Hari ini adalah hari {hari_ini}.")
        else:
            print("Chatbot: Maaf, saya tidak mengerti pertanyaan Anda.")

if __name__ == "__main__":
    chatbot()