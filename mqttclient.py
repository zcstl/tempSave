#!/usr/bin/python
 
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import ssl
 
auth = {
  'username':"1189ce138c4641f6ae2da07e95c13f53",
  'password':"494677b84e9b67a8316a29d40ffb8fe32e3805a193ee9820c4c30a2509407cf6"
}
 

publish.single("LyIMMMGo2830/out/zcstest",
  payload='{"cmd":"turn off"}',
  hostname="139.159.207.70",
  client_id="D2830186390z6cUu",
  auth=auth,
  port=1883,
  protocol=mqtt.MQTTv311)
