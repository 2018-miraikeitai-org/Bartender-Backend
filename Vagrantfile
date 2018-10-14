# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "minimal/xenial64"
  config.vm.box_check_update = false
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder ".", "/vagrant/docker"
  
  config.vm.provider "virtualbox" do |vb|
     vb.memory = "2048"
  end
  
  config.vm.provision :docker, run: "always"

  config.vm.provision :docker_compose,
    yml: "/vagrant/docker/docker-compose.yaml",
    compose_version: "1.22.0",
    run: "always"
end
