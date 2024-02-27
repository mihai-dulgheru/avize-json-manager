import pandas as pd

from file_handler import copy_files, process_json_files


def main():
    input_directory = "input"
    output_directory = "output"
    copy_files(input_directory, output_directory)
    print("Fișierele au fost copiate cu succes!")

    input_directory = "input/avize-by-act"
    data = process_json_files(input_directory)
    df = pd.DataFrame(data)
    output_excel_file = "output/avize_data.xlsx"
    df.to_excel(output_excel_file, index=False)
    print("Fișierul Excel a fost generat cu succes!")


if __name__ == '__main__':
    main()
