#!/bin/bash
. user.properties

echo $user_name
echo $password
echo $hostport

apt-get -y update
apt-get install -y apache2
