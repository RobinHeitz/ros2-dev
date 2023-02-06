#! /usr/bin/env python

import rospy
from visualization_msgs.msg import Marker

def main():


  rospy.init_node('mesh_marker')

  marker_pub = rospy.Publisher("/avocado", Marker, queue_size = 2)

  base_link = Marker()

  base_link.header.frame_id = "base_link"
  base_link.header.stamp = rospy.Time.now()
  base_link.ns = ""

  # Shape (mesh resource type - 10)
  base_link.type = 10
  base_link.id = 0
  base_link.action = 0

  # Note: Must set mesh_resource to a valid URL for a model to appear
  base_link.mesh_resource = "package://igus_rebel_description/meshes/robolink_rebel/Robolink_RebeL_000.dae"
  base_link.mesh_use_embedded_materials = true



  link_1 = Marker()
  link_1.header.frame_id = "link_1"
  link_1.header.stamp = rospy.Time.now()
  link_1.ns = ""

  # Shape (mesh resource type - 10)
  link_1.type = 10
  link_1.id = 0
  link_1.action = 0

  # Note: Must set mesh_resource to a valid URL for a model to appear
  link_1.mesh_resource = "package://igus_rebel_description/meshes/robolink_rebel/Robolink_RebeL_001.dae"
  link_1.mesh_use_embedded_materials = true




  # # Scale
  # marker.scale.x = 10.0
  # marker.scale.y = 10.0
  # marker.scale.z = 10.0

  # # Color
  # marker.color.r = 0.0
  # marker.color.g = 0.0
  # marker.color.b = 0.0
  # marker.color.a = 1.0

  # # Pose
  # marker.pose.position.x = 3
  # marker.pose.position.y = 0
  # marker.pose.position.z = 0
  # marker.pose.orientation.x = 0.0
  # marker.pose.orientation.y = 0.0
  # marker.pose.orientation.z = 0.0
  # marker.pose.orientation.w = 1.0

  while not rospy.is_shutdown():
    marker_pub.publish(marker)
    rospy.rostime.wallsleep(1.0)

if __name__=="__main__":
  main()