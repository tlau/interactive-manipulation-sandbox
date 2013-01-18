#!/bin/bash

ansible-playbook -k -K -i deploy.hosts deploy.yml
