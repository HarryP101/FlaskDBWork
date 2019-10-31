# FlaskDBWork

I have included a setup file which includes all the python packages that are required for this application to run

In order to run it, simply navigate to the source directory where app.py is located and use 'flask run'

This will run the web application for the http api for getting historical data

Running FixerIngester.py will load the data and save it to the database url specified in the file. I ran out of time,
but one of the additional things I would have done would be to save the database url as an environment variable, then get
it using os.environ. This has the benefit of not showing up in source control and also making sure it points to the right location on different machines, if its been configured.

I could spend ages adding additional functionality to Database and FixerIngester, but ive included the main functions Id like to include at some point. Also, to keep things simple, i only saved one currency rate to the Database, but it would be simple to extend this further for the other currencies, perhaps using a 2nd relational table for the 5 rates to one base rate.

In order to monitor this application, traffic to the api could be monitored, as well as sql query statement traffic. For example, the number of 500 http errors could be monitored.
