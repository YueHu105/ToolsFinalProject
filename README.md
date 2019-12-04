Tracker
=
What it Tracker?
-
Tracker is a Web-based application to keep track of all the known squirrels in Central Park. It includes a map visualization, choices for adding, updating, deleting sighting records and a general stats about the sightings.

The dataset and sources
-
The data is from 2018 Central Park Squirrel Census. It contains 3,023 sighting records.

How to use Tracker?
-
There are six views in the application. 
### View of a map which displays the location of the squirrel sightings<br>  
Located at: /map<br>  
Method: GET

### View of a list of all squirrel sightings<br>  
Located at: /sightings<br>  
Method: GET

### View to update a particular sighting<br>  
Located at: /sightings/<unique-squirrel-id><br>  
Method: POST
	
### View to create a new sighting<br>  
Located at: /sightings/add<br>  
Method: POST

### View to delete a sighting<br>  
Located at: /sightings/<unique-squirrel-id><br>  
Method: DELETE

### View of general stats about the sightings<br>  
Located at: /sightings/stats<br>  
Method: GET

Group name and section
-
Project Group 12, Section 2<br>  
UNIs: [ps3120, yh3218] <br>  
Name: Pei Yin Jodie Shue, Yue Hu

