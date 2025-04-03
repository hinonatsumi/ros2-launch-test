FROM osrf/ros:foxy-desktop
COPY ./ros2_ws /ros2_ws
RUN apt update && apt install -y emacs