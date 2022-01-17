# tougshire_auth

A custom user model, group, and admin

This may cause errors if added to a project which is not new.  Read Django's documentation for adding custom user models.

I added the field display\_name, to the subclassed User model, which can be left blank.  I added a property, name, which tries the following fields and returns the field if succesful in the following order: display\_name, first\_name and last\_name, username.  By default, \_\_str\_\_ returns the name property, but can be altered by setting settings.AUTH\_USER\_DISPLAY to a field or property

I added a field, short_name, to the the sub-classed group model. In the help, I suggest this name be one character, so a group called "Technicians" might have a short_name "T".  I added a list column which displays the shortnames of the groups to which the user is a member.  So if "Ben" is a member of "Technicians (T)", "Administrators (A)", and "Salespeople (S)", then Ben's Groups column will display "AST".  This could be a problem if there are many groups but I don't think that is common

I also added a column which displays is_active, is_staff, and is_superuser.  It looks like "Yes / Yes / No", for someone is active, staff, and not superuser

Make sure you add this app to settings.INSTALLED\_APPS and the user model as settings.AUTH\_USER\_MODEL

INSTALLED\_APPS = \[\
... \
'tougshire\_auth.apps.TougshireAuthConfig',\
... \
\]

AUTH\_USER\_MODEL = 'tougshire\_auth.TougshireAuthUser'
