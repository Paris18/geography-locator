# geography-locator
This project will receive the file with address and computes the logitude and latitude of that address and you can download the response in csv file.

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

#### Download test file (example file)

	curl -X GET \
	http://127.0.0.1:8000/api/v1/ltude/get_template_file/ \
    	-H 'Content-Type: application/json'
	
	Note : As response template file will be downloaded.

#### Cleare Existing Data if you dont't want previous

	curl -X DELETE \
	  http://127.0.0.1:8000/api/v1/ltude/cleardata/ \
	  -H 'Content-Type: application/json'


	Response:
	 {
	    "status": "deleted all existed data"
	 }


#### Upload a input file

	curl -X POST \
	  http://127.0.0.1:8000/api/v1/ltude/getltudes/ \
	  -H 'Content-Type: application/x-www-form-urlencoded' \
	  -F key={location iq key} \
	  -F 'input_file=@/D:/Projects/diGeograph/address.csv'

	Response:
	 {
    	"Status": "Filed uploaded successfully and computed output"
	 }

#### Get list of address info in REST

	curl -X GET \
	  http://127.0.0.1:8000/api/v1/ltude/listltudes/ \
	  -H 'Content-Type: application/json'


	Response:
	 [
	    {
	        "id": "07698136-60a9-48bf-9664-87eac2b0bb3c",
	        "created_at": "2019-12-12T06:18:37.162568Z",
	        "updated_at": "2019-12-12T06:18:37.162568Z",
	        "address": "Halaga Belagavi",
	        "latitude": 15.8215819,
	        "longitude": 74.5618976
	    },
	    {
	        "id": "bec542ec-7db7-4612-9d5e-6bb867997f59",
	        "created_at": "2019-12-12T06:18:37.667597Z",
	        "updated_at": "2019-12-12T06:18:37.667597Z",
	        "address": "Bastawad Belagavi",
	        "latitude": 15.8097529,
	        "longitude": 74.5597333
	    }
	 ]


#### Download address file

	curl -X GET \
	  http://127.0.0.1:8000/api/v1/ltude/get_address/ \
	  -H 'Content-Type: application/json'

	  Note : As response output file will be downloaded.


#### Get or Create the individual address data

	curl -X POST \
	  'http://127.0.0.1:8000/api/v1/ltude/getltude/?address=Mudalagis%20Belagavi&key=984aabebe49559' \
	  -H 'Content-Type: application/json' \

	  -d '{
		"address":"mudalagi belagavi",
		"key":"xxxxxxxxxxxx"
		}'

	Response:
	 {
	    "id": "e4abbb17-5d7f-4efe-9ccb-928ecf791723",
	    "created_at": "2019-12-12T07:03:13.477644Z",
	    "updated_at": "2019-12-12T07:03:13.477644Z",
	    "address": "Mudalagis Belagavi",
	    "latitude": 15.849057,
	    "longitude": 74.508943
	 }
