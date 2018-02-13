from clearcontrol.devices.lasers import LaserDeviceInterface;
from clearcontrol.microscope.lightsheet.imaging import DirectImage;
from clearcontrol.microscope.lightsheet.imaging import DirectImageStack;
from net.clearcontrol.lightsheet.easyscopy import EasyScopyUtilities;
from net.clearcontrol.easyscopy.lightsheet.implementations.xwing import SimulatedXWingScope;
from net.imglib2 import RandomAccessibleInterval;
from net.imglib2.img.display.imagej import ImageJFunctions;
from net.imglib2.type.numeric.integer import UnsignedShortType;


# The XWingScope is an instance of EasyLightSheetMicroscope
lScope = SimulatedXWingScope.getInstance();

# Turn on a laser
lLaser = lScope.getDevice("Laser", "488");
lLaser.setTargetPowerInPercent(20);
lLaser.setLaserOn(True);
lLaser.setLaserPowerOn(True);
lLaser.setLaserOn(True);
lLaser.setLaserPowerOn(True);

lScope.getLightSheetMicroscope().getLightSheet(0).getHeightVariable().set(0);

# Take an image
lImage = lScope.getDirectImage();
#lImage.setLightSheetIndex(3);
lImage.setImageWidth(2048);
lImage.setImageHeight(512);
lImage.setIlluminationZ(25);
lImage.setDetectionZ(25);
lImage.setExposureTimeInSeconds(1.0);

# start acquisition
img = EasyScopyUtilities.stackToImg(lImage.acquire());

# show the images
ImageJFunctions.show(img);



# take an imagestack
lImageStack = lScope.getDirectImageStack();
lImageStack.setImageWidth(2048);
lImageStack.setImageHeight(512);
lImageStack.setIlluminationZ(25);
lImageStack.setDetectionZ(25);
lImageStack.setNumberOfRequestedImages(10);
lImageStack.setDetectionZStepDistance(0);
lImageStack.setIlluminationZStepDistance(1);
lImageStack.setExposureTimeInSeconds(1.0);

# start acquisition
imgStack = EasyScopyUtilities.stackToImg(lImageStack.acquire());

# show the images
ImageJFunctions.show(imgStack);


# That's always a godd idea by the end!
lScope.shutDownAllLasers();

# bye bye
# XWingScope.cleanup();



