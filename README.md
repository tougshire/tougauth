# T<z></z>ougshire Auth

A simple Django app for following Django's recommendation to create a custom user model even if no changes from the provided user model are currently needed.  But I did add a couple of things

This may cause errors if added to a project which is not new.  Read Django's documentation for adding custom user models.

I added one field, display\_name, which can be left blank.  I added a property, name, which tries the following fields and returns the field if succesful in the following order: display\_name, first\_name and last\_name, username.  By default, \_\_str\_\_ returns name, but can be altered by setting settings.AUTH\_USER\_DISPLAY to a field or property

This app also creates a custom group which shows up in the same admin heading as the custom user

My intent is that this not be used as-is.  My intent is for you to do the following:
* rename this to your project name, followed by '\_auth',
* rename templates/t<z></z>ougshire\_auth/ the same way
* change all occurances of 'T<z></z>ougshire' and 't<z></z>ougshire' with your project name, capitalized appropriately.

Then hack it to suit your purposes.  But that's your choice.

If you want to use the login and account templates, add the paths to your projects's urls

    ...  
    path('accounts/', include('tougshire_auth.urls')),  
    ...  


Make sure you add this app to settings.INSTALLED\_APPS and the user model as settings.AUTH\_USER\_MODEL

    INSTALLED\_APPS = \[
    ...
    'tougshire\_auth.apps.TougshireAuthConfig',
    ...
    \]

    AUTH\_USER\_MODEL = 'tougshire\_auth.TougshireAuthUser'

Note: in the in this document, I used \<z\> and \<\/z\> tags within T<z></z>ougshire and t<z></z>ougshire to prevent accidental replacement
