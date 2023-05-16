from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint


def pdf_to_mp3(file_path, language):
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        print("[+] Начинаю работать с файлом", Path(file_path).name, "..")
        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
            pages = [page.extract_text() for page in pdf.pages]  # считываем все страницы из файла
            text = "".join(pages)
            # сохраняем файл до замены символов
            with open("temp1.txt", "w") as file:
                file.write(text)
            # сохраняем файл после замены символов
            text = text.replace("\n", "")  # удаляем из текста перенос строки
            with open("temp2.txt", "w") as file:
                file.write(text)

            # сохраняем текст в mp3
            x_audiofile = gTTS(text=text, lang=language, slow=False)
            x_filename = Path(file_path).stem
            x_audiofile.save(x_filename + ".mp3")
            return "[+] Файл сохранен" + x_filename + ".mp3"
    else:
        return "[-] Файл не существует! Проверьте путь.."


def main():
    tprint("PDF >> MP3")
    x_filepath = input("Введите путь к PDF файлу: ")
    x_filelang = input("Введите язык файла (en или ru): ")
    print(pdf_to_mp3(file_path=x_filepath, language=x_filelang))


if __name__ == "__main__":
    main()
