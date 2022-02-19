import os

class CompareFiles:

    def script_info(self) -> None:
        print("-------------------------------------------------------------")
        print("This script will compare the files in two different folders.")
        print("It will show what files are missing on each path given.")
        print("-------------------------------------------------------------")

    def get_list_from_folder(self, folder_path):
        dir_file_list = os.listdir(folder_path.replace("\"", ""))
        '''
        command = rf"dir /b /a-d {folder_path}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        
        byte_folder_list = process.stdout.readlines()
        '''
        return dir_file_list

    def format_byte_to_str_list(self, byte_list) -> list:

        str_list = []

        for line in byte_list:
            word = line.decode("utf-8").strip()
            str_list.append(word)

        return str_list

    def get_folder_path_from_user(self) -> str:
        folder_path = input("Please enter a folder path: \n"
                            r"Example: \"C:\Users\USER\Desktop\" "
                            "\nPath:")

        return folder_path

    def compare_two_lists_and_print_results(self, list_one, list_two, path_one, path_two) -> None:
        counter_one = 0
        counter_two = 0
        print("-------------------------------------------------------------")
        print("Missing in: " + path_one)
        print("-------------------------------------------------------------")
        for missing_file in list(set(list_two) - set(list_one)):
            counter_one += 1
            print(f"{counter_one}. " + missing_file)

        if len(list(set(list_two) - set(list_one))) == 0:
            print("Nothing is missing!")
        else:
            print(f"Total: {counter_one} files are missing.")

        print("-------------------------------------------------------------")
        print("Missing in: " + path_two)
        print("-------------------------------------------------------------")
        for missing_file in list(set(list_one) - set(list_two)):
            counter_two += 1
            print(f"{counter_two}. " + missing_file)

        if len(list(set(list_one) - set(list_two))) == 0:
            print("Nothing is missing!")
        else:
            print(f"Total: {counter_two} files are missing.")


if __name__ == "__main__":
    cf = CompareFiles()

    cf.script_info()
    path_one = cf.get_folder_path_from_user()
    list_one = cf.get_list_from_folder(path_one)
    path_two = cf.get_folder_path_from_user()
    list_two = cf.get_list_from_folder(path_two)

    cf.compare_two_lists_and_print_results(list_one, list_two, path_one, path_two)
