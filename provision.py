#!/usr/bin/env python
import os, sys

if os.getuid() == 0:
	#----- Write Alias -----#
	with open('/home/lazuardi/.bash_aliases', 'a') as alias:
	    alias.write("alias apt=\"sudo apt\"\n")
	    alias.write("alias pip=\"sudo pip\"\n")
	    alias.write("alias gdebi=\"sudo gdebi\"\n")
	    alias.write("alias wget=\"wget -c\"\n")
	    alias.write("alias arcturus=\"ssh root@10.10.10.4\"\n")
	    alias.write("alias sirius=\"ssh root@10.10.10.3\"\n")
	    alias.write("alias antares=\"ssh root@10.10.10.14\"\n")
	    alias.write("alias procyon=\"ssh root@10.10.4.20\"\n")

	#----- Write Bashrc Prompt -----#
	with open('/home/lazuardi/.bashrc','a') as bashrc:
		bashrc.write("export EDITOR=$(which vim)\n")
		bashrc.write("PS1=$\'\[\e[1m\](Nizu) \u2981 (\w) \u2981 (\D{%a,%e %b %y})\n\u2192\[\e[0m\] \'\n")

	#----- Write Vim Configuration File -----#
	with open('/home/lazuardi/.vimrc','a') as vimcfg:
		vimcfg.write("set number\n")
		vimcfg.write("set tabstop=4\n")

	#----- Write NTFS Partition -----#
	with open('/etc/fstab','a') as fstab:
		fstab.write("#DATA\nUUID=B410BD6410BD2E6C /data ntfs-3g defaults,rw,uid=1000,gid=1000 0 0")


	os.system('chown -Rf lazuardi.lazuardi /home/lazuardi/.bash_aliases')
	os.system('chown -Rf lazuardi.lazuardi /home/lazuardi/.bashrc')
	os.system('chown -Rf lazuardi.lazuardi /home/lazuardi/.vimrc')
	os.system('mkdir /data')
	os.system('ssh-keygen')

	#----- Add 3rd Party Repository -----#
	# os.system("add-apt-repository ppa:varlesh-l/papirus-pack")
	os.system("add-apt-repository ppa:docky-core/stable")
	os.system("add-apt-repository ppa:n-muench/burg")
	os.system("add-apt-repository ppa:noobslab/themes")
	os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
	os.system("echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
	os.system("apt update")

	#----- Install LAMP + MongoDB Package -----#
	os.system("apt install mongodb mysql-server mysql-client phpmyadmin apache2 libapache2-mod-wsgi -y")

	#----- Install Pentest Basic Package -----#
	os.system("apt install nmap sqlmap metasploit-framework dsniff driftnet aircrack-ng uniscan hamster-sidejack -y")

	#----- Install Development Package -----#
	os.system("apt install build-essential g++ gcc python-dev python-setuptools python-pip python-mysqldb filezilla git git-core vim autoconf automake libgtk-3-dev -y")
	os.system("pip install --upgrade pip")
	os.system("pip install fabric fabtools flask pycurl pymongo mongoengine tabulate flask-socketio")

	#----- Install Multimedia Package -----#
	os.system('apt install vlc audacious gimp arc-flatabulous-theme -y')
else:
	print "Cannot run as Mortal.."
