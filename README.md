# RONALD360

###### READMEv1.0


## [Overview](#Overview)

An open source, cheap, 4-mecanum-wheel robot capable of swiftly navigating very flat surfaces through teleoperation via a 360 camera.
It consists of a [M5 RoverC](https://shop.m5stack.com/collections/m5-hobby/products/roverc-prow-o-m5stickc), and a [Insta360 X3](https://www.insta360.com/product/insta360-x3) connected via a 3D Printed Carbon Fiber Reinforced Mount

* [Hardware](#Hardware)

No modifications are necessary to the Insta 360 in order to make it stream, you just need to make sure that you have the Insta360 Installed, Updated and paired with your camera. You are also able to use An Insta360 One X2 Instead of an X3 and everything should work just as well.

* ** *Limitations of the mechanum wheel system:* ** 

	- Due to the high-ratio gearbox needed to drive a mechanum wheel system with small motors the robot stop really quickly, and specially quickly when going sideways. This can result in the robot tipping over. Be carefull. 
	- Leaves, hair and other undesireables will make their way into the inside of your mechanum wheel of you drive over them, specialy if not going straight or backwards. Don't drive over things that can tangle the wheels.
	- You need a fair bit of torque to get moving, about 10% actuation to start moving, below that you just get coil whine
	- The gearbox is exposed and down low, if stuff gets inside of it you're F***.



* [Software](#Software)

* [Software Checkout and Setup With UIFlow](#Software-Checkout-and-Setup-UIFlow)
	
	- Go to [UIFlow](https://flow.m5stack.com), enter the API Key from your [M5 StickC+](https://shop.m5stack.com/collections/m5-controllers/products/m5stickc-plus-esp32-pico-mini-iot-development-kit) and upload the .m5f File. You may alternatively copy the code from the .py file into the python window.
	- Upload to your [M5 StickC+](https://shop.m5stack.com/collections/m5-controllers/products/m5stickc-plus-esp32-pico-mini-iot-development-kit)
	
* [Software Checkout and Setup With Micropython](#Software-Checkout-and-Setup-mPython)
	* 
	TODO
	

* [Additional Project Components & Tecniques](#additional-project-components-&-Tecniques)
    * [ESP-NOW](#ESP-NOW)

* [Future Work](#future-work)

- Figure out a way to record and live stream at the same time in 360.
- Integrate robot with a VR Headset app to control robot and view 360 feed like a videogame. 


* [Archive](#Archive)

![Env](Images/RONALD_MRK1.jpeg) 
This is the MRK1 Robot. It had a simple ESP32-Powered Webcam, the [M5 Unit Cam(MRK1)](https://shop.m5stack.com/collections/m5-cameras/products/unit-cam-wi-fi-camera-diy-kit-ov2640), and later a [M5 UnitV2(MRK2)](https://shop.m5stack.com/collections/m5-cameras/products/unitv2-ai-camera-gc2145) but both proved to be too laggy and useless. Unfortunately I did not take a picture of the Mrk 2 Robot before disassembling it because I built it at a really chaotic time in my life. 
