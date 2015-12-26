Title: How to restart KDE window manager on the fly
Date: 2015-12-18 15:47
Category: linux
Tags: command line, trick, kde, desktop, ubuntu

So you are inside your Kubuntu with a lot of windows open and you have changed some configurations and KDE needs to be restarted? Or you have done something and KDE is malfunctioning and you need to restart it? No need to exit your desktop and loose your windows. Just open an terminal (Alt-F2 -> Konsole) and run this:

````
nohup kwin-x11 --replace &
````

- **nohup** tells the new window manager to continue running even if you close the konsole
- **kwin-x11** is the name of kde winodw manager in newer Ubuntu machines
- as you can guess **--replace** replaces the current running window manager with the new one
-- The **&** at the end, will give you back the command line while running this command
