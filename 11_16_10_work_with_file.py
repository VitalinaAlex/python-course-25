"""Task 1
Files
Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it. 
Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system command line. 
Does the new file show up in the directory where you ran your scripts? 
What if you add a different directory path to the filename passed to open?
Note: file write methods do not add newline characters to your strings; add an explicit "\n" at the end of the string if you want to fully terminate the line in the file."""

# новий файл або перезапис ('w')
with open("myfile.txt", "w") as file:
    file.write("This is the first line: Hello file world!\n")
    
# новий файл або новий рядок ('w')
with open("myfile.txt", "a") as file:
    file.write("This is the second line: Hello file world!")

print("File 'myfile.txt' created and written to.")
# читати вміст та вивести
with open("myfile.txt", "r") as file:
    # Виводимо вміст на екран
    print(file.read())

"""Task 2
Extend Phonebook application
Functionality of Phonebook application:
Add new entries 
Search by first name 
Search by last name 
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is present in the folder with application, else raise an error. 
After the user exits, all data should be saved to loaded JSON."""
