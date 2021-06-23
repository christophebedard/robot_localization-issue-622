# robot_localization-issue-622

Minimal working example to reproduce:

* https://github.com/cra-ros-pkg/robot_localization/issues/622
* https://answers.ros.org/question/380328/robot_localization-cant-subtract-times-with-different-time-sources/

## Steps

1. Clone `robot_localization` and this repo
    ```sh
    $ mkdir -p ~/ros2_ws/src
    $ cd ~/ros2_ws/src
    $ git clone https://github.com/cra-ros-pkg/robot_localization.git -b ros2
    $ git clone https://github.com/christophebedard/robot_localization-issue-622.git
    ```
1. Install dependencies
    ```sh
    $ rosdep install -y --rosdistro rolling --from-paths src/ -i src/ --skip-keys="rti-connext-dds-5.3.1"
    ```
1. Build
    ```sh
    $ source /opt/ros/rolling/setup.bash
    $ colcon build --packages-up-to test_pkg --mixin debug
    ```
1. In another terminal, run the `minimal_publisher` node
    ```sh
    $ cd ~/ros2_ws
    $ source install/setup.bash
    $ ros2 run test_pkg minimal_publisher
    ```
1. In another terminal, launch `ekf.launch.py`
    ```sh
    $ cd ~/ros2_ws
    $ source install/setup.bash
    $ ros2 launch robot_localization ekf.launch.py
    ```
1. The `ekf_node` should crash with this error
    ```
    [ekf_node-1] terminate called after throwing an instance of 'std::runtime_error'
    [ekf_node-1]   what():  can't subtract times with different time sources [1 != 2]
    ```
