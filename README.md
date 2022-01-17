# tougshire_auth

A simple Django app for following Django's recommendation to create a custom user model even if no changes from the provided user model are currently needed.  But I did add a couple of things

This may cause errors if added to a project which is not new.  Read Django's documentation for adding custom user models.

I added one field, display\_name, which can be left blank.  I added a property, name, which tries the following fields and returns the field if succesful in the following order: display\_name, first\_name and last\_name, username.  By default, \_\_str\_\_ returns name, but can be altered by setting settings.AUTH\_USER\_DISPLAY to a field or property

This app also creates a custom group which shows up in the same admin heading as the custom user

You might want to copy or fork this code then modify it to create your own custom user model app.  Here's what I do:

* rename this to the project name, followed by '\_auth' - so if my project is named "example" then instead of tougs<wbr>hire_auth it will be example_auth
* rename templates/toug<wbr>shire\_auth/ the same way
* change all occurances of 'Toug<wbr>shire' and 'toug<wbr>shire' with the project name, capitalized appropriately.


Make sure you add this app to settings.INSTALLED\_APPS and the user model as settings.AUTH\_USER\_MODEL

INSTALLED\_APPS = \[\
... \
'tougshire\_auth.apps.TougshireAuthConfig',\
... \
\]

AUTH\_USER\_MODEL = 'tougshire\_auth.TougshireAuthUser'
