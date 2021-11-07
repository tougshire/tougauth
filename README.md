# tougauth

A simple Django app for a custom user model that makes few changes from the provided user model.  It is meant to help follow Django's recommendation to create a custom user model even if no changes from the provided user model are currently needed

There is one added field, display name, which can be left blank

This app also creates a custom group which shows up in the same admin heading as the custom user

My intent is for this to be used as a starting template to be addded to a Django project then renamed and customized

I recommend renaming your copy from 'tougshire_auth' to your project's name followed by underscore and 'auth', and replacing all instances of 'tougshire' and 'Tougshire' with your project's name, capitalized appropriately, including in the migrations file

In your settings, set AUTH_USER_MODEL to your renamed 'tougshire_auth.TougshireAuthUser', and to add your renamed 'tougshire_auth.apps.TougshireAuthConfig' to INSTALLED_APPS in your settings

This should be used for new projects before any migrations are made that include or reference the user model












