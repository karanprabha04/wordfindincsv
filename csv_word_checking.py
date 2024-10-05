# Call the function to delete old tracecli folders in the specified directory
def delete_old_tracecli_folders(directory):
    # Get list of all directories in the specified path
    folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    tracecli_folders = [name for name in folders if name.startswith("tracecli")]

    if not tracecli_folders:
        print("No tracecli folders found in the specified directory.")
        return None

    tracecli_folders.sort()  # Sort folders alphabetically
    latest_folder = os.path.join(directory, tracecli_folders[-1])  # Get the latest folder

    # Delete all tracecli folders except the latest one
    for folder in tracecli_folders[:-1]:
        folder_path = os.path.join(directory, folder)
        try:
            shutil.rmtree(folder_path)
            print(f"Deleted folder: {folder_path}")
        except Exception as e:
            print(f"Error deleting folder {folder_path}: {str(e)}")

    return latest_folder

# Call the function to tracecli folder in the specified directory
def get_tracecli_folder():
    folder_name = input("Enter the name of the folder: ")
    current_directory = os.getcwd()
    tracecli_folder_path = os.path.join(current_directory, folder_name)
    return tracecli_folder_path

# Call the function to get csv file in the specified directory
def latest_csv_file(folder):
    csv_files = glob.glob(os.path.join(folder, '*.csv'))

    if not csv_files:
        print("No CSV file found in the specified folder.")
        return None

    # Get the latest CSV file based on modification time
    latest_file = max(csv_files, key=os.path.getmtime)
    print("Latest CSV file:", latest_file)
    return latest_file

# Call the function to find specific search word in the CSV File
def check_text_in_column(latest_file, column_index, text_to_check):
    with open(latest_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > column_index and row[column_index] == text_to_check:
                return True
    return False

# Main program
directory_path = r"C:\Users\sundar9x\AppData\Local\Temp\1"  # give the root directory
if True:
    latest_tracecli = delete_old_tracecli_folders(directory_path)
    if latest_tracecli:
        latest_file = latest_csv_file(latest_tracecli)
        if latest_file:
            column_index = 1  # Index of the column to check (0-based index)
            text_to_check = 'DRAM_Core0_Channel_0'
            if check_text_in_column(latest_file, column_index, text_to_check):
                print(f"The Source trace '{text_to_check}' exists")
            else:
                print(f"The Source trace '{text_to_check}' does not exist.")
else:
    tracecli_folder = get_tracecli_folder()
    latest_file = latest_csv_file(tracecli_folder)
    if latest_file:
        column_index = 1  # Index of the column to check (0-based index)
        text_to_check = 'DRAM_Core0_Channel_0'
        if check_text_in_column(latest_file, column_index, text_to_check):
            print(f"The Source trace '{text_to_check}' exists")
        else:
            print(f"The Source trace '{text_to_check}' does not exist.")