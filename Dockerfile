ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}

ARG WORKSPACE=ros2_dev_ws
WORKDIR /root/${WORKSPACE}

EXPOSE 8765