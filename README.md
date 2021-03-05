# Test api for google spreedsheets
Small test api for google spreedsheets that gets data from public url and returns basic types of columns.

example of public url - https://docs.google.com/spreadsheets/d/1ww2UcaIz19H_1MRJLmCLp6UGQMvg1_xg65yrn0uZ0rQ/

# Install
Before running code you need to create a new Cloud Platform project and automatically enable the Google Sheets API and generate API key for this progect
(you can find all needed information [here](https://developers.google.com/sheets/api/guides/concepts)).
After that add this key to .env file

Make sure that you have [docker](https://www.docker.com/) installed. Open command line(terminal) and run(inside repo folder):

`docker-compose up`

or

`docker-compose up -d` - will run docker containers in the background


http://localhost:8000/ - base api endpoint

http://localhost:8000/docs - api documentation
