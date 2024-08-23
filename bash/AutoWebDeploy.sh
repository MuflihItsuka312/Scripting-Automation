#!/bin/bash

PACKAGE="wget unzip httpd"
SERVER="httpd"
TMP="/tmp/webfiles"
unzipped_dir=$(ls -d */ | head -n 1)
#############################
# Install necessary packages#
#############################
sudo yum install -y
######################################
# Start and enable Apache HTTP server#
######################################
sudo systemctl start $SERVER
sudo systemctl enable $SERVER
#######################################
# Create a directory for the web files#
#######################################
mkdir -p $TMP cd $TMP
##############################
#remove html content/refresh##
##############################
sudo rm -rf /var/www/html/*
###############################
# Prompt the user for the link#
###############################
read -p "Please enter the link to the zip file: " zip_link
#####################################################
# Download and unzip the file from the provided link#
######################################################
wget "$zip_link"
unzip *.zip
#######################################################
# Visit the directory where the files were unzipped3###
# Assuming the zip extracts into a directory        ###
#######################################################
cd "$unzipped_dir"
#####################################################
# Copy the contents to the Apache web root directory#
#####################################################
sudo cp -r * /var/www/html
##########
#clean up#
##########
cd ..
sudo rm -f *.zip
rm -rf "$unzipped_dir"
############################################
# Restart the HTTP server to apply changes#
###########################################
sudo systemctl restart $SERVER
###########################################
# Clean up by removing the temporary files#
############################################
rm -rf $TMP
sudo systemctl status $SERVER
ls /var/www/html