# tougauth

A simple Django app for following Django's recommendation to create a custom user model even if no changes from the provided user model are currently needed.  But I did add a couple of things

This may cause errors if added to a project which is not new.  Read Django's documentation for adding custom user models.

I added one field, display\_name, which can be left blank.  There is an added property, name, which tries the following fields and returns the field if succesful in the following order: display\_name, first\_name and last\_name, username.  By default, \_\_str\_\_ returns name, but can be altered by setting settings.AUTH\_USER\_DISPLAY to a field or property

This app also creates a custom group which shows up in the same admin heading as the custom user

My intent is that this not be used as-is.  My intent is for this to be renamed to your project name, followed by '\_auth', then change all occurances of 'Tougshire' and 'tougshire' with your project name, capitalized approprieately.  Then hack it to suit your purposes

