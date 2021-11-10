# tougauth

A simple Django app for following Django's recommendation to create a custom user model even if no changes from the provided user model are currently needed.  But I did add a couple of things

This may cause errors if added to a project which is not new.  Read Django's documentation for adding custom user models.

I added one field, display\_name, which can be left blank.  I added a property, name, which tries the following fields and returns the field if succesful in the following order: display\_name, first\_name and last\_name, username.  By default, \_\_str\_\_ returns name, but can be altered by setting settings.AUTH\_USER\_DISPLAY to a field or property

This app also creates a custom group which shows up in the same admin heading as the custom user

My intent is that this not be used as-is.  My intent is for you to rename this to your project name, followed by '\_auth', then change all occurances of 'T.ougshire' and 't.ougshire' (without the periods which I put in to prevent replacement in this readme) with your project name, capitalized appropriately.  Then hack it to suit your purposes.  But that's your choice.

Make sure you add this app to settings.INSTALLED_APPS and the user model as settings.AUTH_USER_MODEL
INSTALLED_APPS = \[
  ...
  'tougshire_auth.apps.TougshireAuthConfig',
  ...
 \]
 ...
 AUTH_USER_MODEL = 'tougshire_auth.TougshireAuthUser'
