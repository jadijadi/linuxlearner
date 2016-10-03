Title: 107.2 Automate system administration tasks by scheduling jobs
Date: 2015-12-25 12:20
Category: lpic102
Tags: test

# 107.2 Automate system administration tasks by scheduling jobs
*Weight: 4*

Candidates should be able to use cron or anacron to run jobs at regular intervals and to use at to run jobs at a specific time.

## Key Knowledge Areas
- Manage cron and at jobs.
- Configure user access to cron and at services.
- Configure anacron.

## Terms and Utilities
- /etc/cron.{d,daily,hourly,monthly,weekly}/
- /etc/at.deny
- /etc/at.allow
- /etc/crontab
- /etc/cron.allow
- /etc/cron.deny
- /var/spool/cron/
- crontab
- at
- atq
- atrm
- anacron
- /etc/anacrontab

## Crontab format
Crontab files are responsible to run some commands on specific intervals. Each line has 5 fileds to specify the run time and whatever after it is considered the command to be run.

````
A	B	C	D	E	command and arguments
````
|filed|Meaning|values|
|-|-|-|
|A|minute|0-59|
|B|hour|0-23|
|C|day of month|1-31|
|D|month|1-12 (or names, see below)|
|E|day of week|0-7 (0 or 7 is Sunday, or use names)|

Each time field can be a `*` to indicate *ANY*. Also if you have `@reboot` or `@daily` instead of time fields, the command will be run once after the reboot or daily. Lets see some examples:

````
5 0 * * *       $HOME/bin/daily.job >> $HOME/tmp/out 2>&1
# run at 2:15pm on the first of every month -- output mailed to paul
15 14 1 * *     $HOME/bin/monthly
# run at 10 pm on weekdays, annoy Joe
0 22 * * 1-5    mail -s "It's 10pm" joe%Joe,%%Where are your kids?%
23 0-23/2 * * * echo "run 23 minutes after midn, 2am, 4am ..., everyday"
5 4 * * sun     echo "run at 5 after 4 every sunday"
*/5 * * * *	echo "each 5 mintues"
42 8,18 * * 1-5	echo "8:42 and 18:42 and only on weekdays (monday till friday)"
@reboot		echo "runs after the reboot"
````

> Note: be careful about using a * on the first filed. That will run your cron on every minute!

> Note: Use with care. Something like `42 8 1 1 0` runs ONLY IF 1st Of Jan is a Monday!

When a cron runs, the output will be emailed to the owner of the cron.

## user specific crons
Cron is a linux service. To see your crons you can use `crontab -l` (list) and for editing it you can use `crontab -e` (edit) which will open the cron files with a special editor and will load your inserted crons (if they are correct) after wards.

The files will be saved at `/var/spool/cron/tabs/` or `/var/spool/crontabs':

````
# cat /var/spool/cron/tabs/jadi
# DO NOT EDIT THIS FILE - edit the master and reinstall.
# (/tmp/crontab.khObLu installed on Thu Oct 29 22:04:43 2015)
# (Cronie version 4.2)
* * * * * date >> /tmp/date.cron.txt
````

You should never edit these files directly; Use `crontab -e` instead.

## at
We say that crontab runs commands on specific intervals but what will happen if you needed to run a command only once? Here `at` is your friend.

````
$ at now + 1 min
warning: commands will be executed using /bin/sh
at> touch /tmp/at
at> <EOT>
job 3 at Thu Oct 29 22:12:00 2015
````

> Note: As always, at the end of input we press Ctrl+D

If you want to check what is in the queue you can use `atq` and then try `atrm 4` to delete job number 4;

````

$ at teatime
warning: commands will be executed using /bin/sh
at> echo "tea time is 4pm"
at> <EOT>
job 4 at Fri Oct 30 16:00:00 2015
jadi@funlife:~$ at tomorrow
warning: commands will be executed using /bin/sh
at> echo "tomorrow this time"
at> <EOT>
job 5 at Fri Oct 30 22:15:00 2015
jadi@funlife:~$ at 17:30
warning: commands will be executed using /bin/sh
at> echo "this is the first 17:30"
at> <EOT>
job 6 at Fri Oct 30 17:30:00 2015
jadi@funlife:~$ atq
5	Fri Oct 30 22:15:00 2015 a jadi
4	Fri Oct 30 16:00:00 2015 a jadi
6	Fri Oct 30 17:30:00 2015 a jadi
jadi@funlife:~$ atrm 4
jadi@funlife:~$ atq
5	Fri Oct 30 22:15:00 2015 a jadi
6	Fri Oct 30 17:30:00 2015 a jadi
````

## system wide cron
There is file called `/etc/crontab`. This looks like a normal user file opened with `crontab -e` but has one extra filed:

`````
A	B	C	D	E	USER	command and arguments
`````

This file should be edited with an editor directly and we can mention which user runs this commands.

````
# cat /etc/crontab
SHELL=/bin/sh
PATH=/usr/bin:/usr/sbin:/sbin:/bin:/usr/lib/news/bin
MAILTO=root
#
# check scripts in cron.hourly, cron.daily, cron.weekly, and cron.monthly
#
-*/15 * * * *   root  test -x /usr/lib/cron/run-crons && /usr/lib/cron/run-crons >/dev/null 2>&1
````

> Note: Have a look at first two line. It configures the shell which will run the commands and the PATH variable plus who will get the output emails.

As you can see this default crontab runs other crons! They are hourly, daily, weekly and monthly crons.

## System hourly, daliy, weekly, monthly, .. crons

We have some system level crontab files in `/etc/cron.d/` too. In other words, whatever file which is copied there, will be treated just like `/etc/crontab` file (a system wide cron file). This make systems much cleaner and lets programs to copy one file there instead of editing the /etc/crontab.

````
$ sudo tree /etc/cron*
root's password:
/etc/cron.d
└── mdadm
/etc/cron.daily
├── google-chrome
├── mdadm
├── mlocate.cron
├── packagekit-background.cron
├── suse-clean_catman
├── suse.de-backup-rc.config
├── suse.de-backup-rpmdb
├── suse.de-check-battery
├── suse.de-cron-local
├── suse.de-snapper
└── suse-do_mandb
/etc/cron.deny [error opening dir]
/etc/cron.hourly
└── suse.de-snapper
/etc/cron.monthly
/etc/crontab [error opening dir]
/etc/cron.weekly
````

Lets have a look at one of the cron.d files:

````
$ cat /etc/cron.d/mdadm
#
# cron.d/mdadm - regular redundancy checks
#

# Start checking each month early in the morning.
# Continue each day until all done

PATH=/sbin:/usr/sbin:/bin:/usr/bin
0 1 * * 0 root source /etc/sysconfig/mdadm; [ -n "$MDADM_CHECK_DURATION" -a -x /usr/share/mdadm/mdcheck -a $(date +\%d) -le 7 ] && /usr/share/mdadm/mdcheck --duration "$MDADM_CHECK_DURATION"
0 1 * * 1-6 root source /etc/sysconfig/mdadm; [ -n "$MDADM_CHECK_DURATION" -a -x /usr/share/mdadm/mdcheck ] && /usr/share/mdadm/mdcheck --continue --duration "$MDADM_CHECK_DURATION"
````

But /etc/cron.hourly, /etc/cron.daily, /etc/cron.weekly, /etc/cron.monthly is **TOTALLY DIFFERENT**. In these directories are actual executable scripts and files. The cron will run these files one a hour, one a day, once a week or once a month based on their directory names.


## anacron
The difference between cron and anacron, is this:

> If the system is down when the cron should run a task, that cron job wont run till the next occurrence! But anacron creates the timestamp each time a **daily**, **weekly** or **monthly** job runs. If the system **boots up** and find outs that one of the anacron jobs are missed, it will run it during the boot!

As you can see anacron is useful for important tasks. If you need to take a backup once a week it is better to use anacron instead of cron; or feeding your dog once a day using cron may lead to it staying hungry for a day if the system is down when he should be fed.

> Note: anacron checks the timestamps at BOOT TIME and do not handle hourly crons.

## controlling access using files
You have already seen files at /var/spool/cron/tabs/USERNAME. There are also 4 more files to control who can and can not use cron and at. The files are:

````
/etc/cron.allow
/etc/cron.deny

/etc/at.allow
/etc/at.deny
````

In most systems none of these files exist but if you create them, they will become active as follow:

|file extension|functionality|
|-|-|
|.allow|ONLY users mentioned in this file are allowed to run this service. All other users will be denied|
|.deny|Everybody can use the service except the users mentioned in this file|

.

.

.

.

.

.

.

.

.

.