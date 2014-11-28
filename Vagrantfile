# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version.
# Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common
  # configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "thoughtbot/ubuntu-14-04-server-with-laptop"

  # Create a forwarded port mapping which allows access to a specific
  # port within the machine from a port on the host machine.
  # Flask & BrowserSync
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.network "forwarded_port", guest: 3000, host: 3000
end
