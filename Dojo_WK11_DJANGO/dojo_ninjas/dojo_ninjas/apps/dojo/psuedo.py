'''
Task
Using Django Shell:

    Create 3 dojos
    Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())
    Create 3 additional dojos by using Dojo.objects.create
    Create 3 ninjas that belong to the first dojo you created.
    Create 3 more ninjas and have them belong to the second dojo you created.
    Create 3 more ninjas and have them belong to the third dojo you created.
    Be able to retrieve all ninjas that belong to the first Dojo
    Be able to retrieve all ninjas that belong to the last Dojo

Add a new field in the Dojo class (found in your models.py) called 'desc'. Allow 'desc' to hold long text (more than 255 characters). To forward engineer the change, run the appropriate migration commands. Successfully run the migration files and check the records to make sure the new field was added successfully.
'''
