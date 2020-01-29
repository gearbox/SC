Right after running 'python manage.py migrate', run the following commands in order to populate Languages and Countries
 models with real data for Languages:
 
`python manage.py loaddata languages_data.json.gz`
  
And then for Countries:

`python manage.py update_countries_plus`
  
(alternative) Load the provided fixture from the fixtures directory:

`python manage.py loaddata PATH_TO_COUNTRIES_PLUS/countries_plus/countries_data.json.gz`

It may look like this:

`python manage.py loaddata countries_data.json.gz` 

Generating Culture Codes (ex: pt_BR).
You can run the below command in fjango shell:

`from languages_plus.utils import associate_countries_and_languages`
`associate_countries_and_languages()`

