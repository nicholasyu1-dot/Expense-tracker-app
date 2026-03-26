# Expense-tracker-app

# OVERVIEW

This is an app that is made for a personal expense tracker.
It has features including:

	 	-add expenses
	 	-remove expenses
	 	-interactable calendar
	 	-will save previous works done in the app




# RELEASE NOTES

Version 1.0.0
	The Expense tracker no has a feature of adding expenses and viewing it. The user can view past
	expenses because a database is implemented to save the user input.




# CONTAINER USAGE

	- Go to Windows cmd/powershell 
	- input:
		cd "(folder path paste here)"
		docker build -t expense-tracker-app .
		docker run --rm -it expense-tracker-app
		



# SETTING UP THE APP

Required to use the app:

		-install python package
		-TKinter (included in the python package)
		-install SQLite

Download the python from this link:

	https://www.python.org/downloads/

To install SQLite type this in your terminal:
	winget install SQLite.SQLite

To run the app

Go to this link and download the zip file.

	https://github.com/user-attachments/files/25946998/Expense-tracker-app-1.0.0.zip

After extracting the zip file into a folder. 

	- Open VsCode 
	- Open the folder where you extracted the zip file
	- run this link in the terminal:
		python Code\Expense-tracker-app.py





# PYTEST

	To run the pytest just copy paste this in the terminal:
			python -m pytest






# BENCHMARKING AND PROFILING
	
	The tool used in the benchamrking and profiling is CProfile
	The metric is in seconds
	
	The numbers during the profiling means
		 necalls - is how many times a function was called
		 tottime - time spent in the function alone
		 cumtime - total time including everythind it called inside it
			
	Total time per functions
		show_add_expense_window - 0.000s
		load_expenses           - 0.001s
		create_add_expenses_window - 0.015s
		show_view_expenses_window - 0.006s
		save_expense               - 1.463s

	Explanation for the highest
		the save expense is not slow on the saving part but because of the "showinfo" which is the popup 
		that ate 1.426s out of the 1.463s which basically means that it is the wait time for the user to click ok.




	
# Architecture Summary 

	- Class-based design which is clean and organized
	
	├── README.md
	├── Code/
	│   ├── Expense-tracker-app.py
	│   ├── expense_logic.py
	│   ├── test_expense_logic.py
	│   └── __pycache__/
	├── Database/
	│   └── database.py
	└── .github/
	    └── workflows/
	        └── github-actions.yml
	functions:
	
	- __init__ → startup
	- setup_styles → appearance
	- create_layout → structure
	- toggle_fullscreen → behavior


# LIMITATIONS

	- The app doesn't have a calendar YET
