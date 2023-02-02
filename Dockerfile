ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}

ARG WORKSPACE=ros2_dev_ws
WORKDIR /root/${WORKSPACE}

EXPOSE 8765

# Copy ROS packages into workspace folder.
COPY ${WORKSPACE}/src /root/${WORKSPACE}/src

COPY /scripts /scripts


RUN apt-get -qq update && apt-get -qq upgrade -y && apt-get install -y \
    git \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    #ros-${ROS_DISTRO}-moveit \

    # ros-${ROS_DISTRO}-rviz2 \

    # ros-humble-turtle-tf2-py \
    ros-humble-tf2-tools \
    ros-humble-tf-transformations \

    #foxglove bridge:
    ros-humble-foxglove-bridge \


    ros-humble-rqt* \
    # ros-humble-turtlesim \
    #ros-${ROS_DISTRO}-ros2-control \
    nano &&\
    rm -rf /var/lib/apt/lists/*

# RUN chmod +x /scripts/sourcing.sh
# RUN bash scripts/sourcing.sh

COPY scripts/*.sh /scripts
# RUN find . -iname "*.sh" -exec bash -c 'chmod +x "$0"' {} \;
CMD find /scripts -iname "*.sh" -exec bash -c 'chmod +x "$0"' {} \;