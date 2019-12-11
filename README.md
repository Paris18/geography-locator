# geography-locator
This project will receive the file with address and computes the logitude and latitude of that address and you can download the response in csv file

### Basic Requirements

	Python3
	virtualenv

### Step 1: create virtualenv and Install the requirements with requirement.txt file 

	virtualenv env_name
	pip install -r requirements.txt

### Step 2: Create Migration file
	
	python manage.py makemigrations

### Step 3: Execute the migrations

	python manage.py migrate

### Step 4: Run the Application

	python manage.py runserver

## Api request and response

### Download test file (example file)

	curl -X GET \
	http://127.0.0.1:8000/api/v1/ltude/get_template_file/ \
    -H 'Content-Type: application/json'

