# SSIS_Project8

The solution is used to generate data using a python script and then load it into the AdventureWorksLT2019 database.

Using the "input_file_2.py" script, data is generated - in this case, the name and surname. The data is saved to a text file. Then, using the "copy_file_rename.py" script, the file is duplicated, the date and time of the created duplicate are added to the name of the new file.

The next step of the solution is to load the generated data into the "Employees" table (the AdventureWorksLT2019_3.bak database backup contains the Employees table and the Contact table used in the next step). In addition to the data contained in the file, the date of adding the record to the table is also added to the table.

The last step is to add data to the Contact table. In addition to the data generated by the script, the contact table is also added to the e-mail address of the person, created by concatenating the person's name and surname.
