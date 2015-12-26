Title: Fix the Drupal pagination problem with nginx
Date: 2015-12-25 12:20
Category: linux
Tags: nginx, tip

### Problem
You have configured your drupal site and everything works fine except the pagination. Many other pages can misfunction too, technically the ones that pass a parametere to your page via GET like variables.

### Reason
The problem comes from the `try_files` config suggested in many websites as:

````
try_files $uri $uri/ /index.php;
````

This line does not pass the quesry_string variable to drupal so drupal can not see that the users is clicking to go to the 2nd page.

### Solution
What you need is passing the `query_string` to the index.php in Druapl. It is enough to chagne this line in your configurations (at `/etc/nginx/`) from

````
try_files $uri $uri/ /index.php;
````

to

````
try_files $uri $uri/ /index.php?q=$uri&$query_string;
````



