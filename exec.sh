#!/bin/bash

# run this for executing AND setting env variables!


name='ros2-humble'

active_containers=$(docker ps --format '{{.Names}}')


if [[ $active_containers == *$name* ]]; then
    echo "Container $name is running. Starting docker exec cmd."
    ip=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | cut -d\  -f2):0
    docker exec -it --privileged -e DISPLAY=$ip $name bash
  else
  echo "Container $name isn't running."
fi