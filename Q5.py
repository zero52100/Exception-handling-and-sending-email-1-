try:
    source_file = input("Enter  source file name: ")
    with open(source_file, 'r') as sf:
        data = sf.read()

    destination_file = input("Enter destination file name: ")
    with open(destination_file, 'w') as df:
        df.write(data)

    print("File contents successfully copied.")

except FileNotFoundError:
    print("Source file not found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'source_file' in locals() and not source_file.closed:
        source_file.close()

    if 'destination_file' in locals() and not destination_file.closed:
        destination_file.close()
