#!/usr/bin/python3
import subprocess
import sys
import os
import shutil

def execute(cmd):
	p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)

	while True:
		out = p.stderr.read(1)
		if out == b'' and p.poll() != None:
			break
		if out != '':
			sys.stdout.write(out.decode('utf-8'))
			sys.stdout.flush()

#getting google chrome keys
execute("sudo wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub > google.key")
execute("sudo apt-key add google.key")
os.remove("google.key")
#adding google chrome ppa
if os.path.exists("/etc/apt/sources.list.d/google-chrome.list"):
	execute("sudo rm /etc/apt/sources.list.d/google-chrome.list*")
execute("sudo sh -c 'echo \"deb http://dl.google.com/linux/chrome/deb/ stable main\" >> /etc/apt/sources.list.d/google-chrome.list'")
#updating and installation
execute("sudo apt-get update")
execute("sudo apt-get -y upgrade")
execute("sudo apt-get -y install apache2 mysql-server mysql-workbench postgresql ubuntu-restricted-extras vim git git-core ssh gimp dia inkscape skype audacity shutter axel deluge vlc filezilla p7zip p7zip-full p7zip-rar audacious meld google-chrome-stable curl exuberant-ctags build-essential libssl-dev vim tmux zsh python3-pip")
execute("gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3")
execute("\curl -sSL https://get.rvm.io | bash -s stable --rails")
