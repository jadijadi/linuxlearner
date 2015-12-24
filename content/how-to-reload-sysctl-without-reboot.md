Title: Apply sysctl.conf without rebooting
Date: 2015-12-16 10:20
Category: tip
Tags: kernal, sysadmin, command line

There are a lot of important configs in `/etc/sysctl.conf`; say configs related to hardening. Most people reboot the system after they change these valued. But not you! It is enouth to use the `sysctl` command with the `-p` switch to aplly the changes you've just done as follow:

````
$ sudo sysctl -p /etc/sysctl.conf
````

As always it is good to have a look at the related part of the man page:

````
 -p[FILE], --load[=FILE]
     Load   in   sysctl   settings   from   the   file  specified  or
     /etc/sysctl.conf if none given.  Specifying - as filename  means
     reading  data  from standard input.  Using this option will mean
     arguments to sysctl are files, which are read in order they  are
     specified.   The  file  argument can may be specified as reqular
     expression.
````
