import SimpleCV as scv
import sys

a = scv.Image("output1.tif")
b = scv.Image("output2.tif")

hue_a = a.hueDistance(132)
hue_b = b.hueDistance(132)
innerA.scale(0.4).rotateLeft().save("hue_a.png")
innerB.scale(0.4).rotateLeft().save("hue_b.png")


#threshold hue transform
threshold_a = hue_a.threshold(200)
threshold_b = hue_b.threshold(200)
threshold_a.rotateLeft().save("hue_a_threshold.png")
threshold_b.rotateLeft().save("hue_b_threshold.png")

sys.exit()

#Morphological operations/denoising
morph_a = hue_a.threshold(200).erode(2).dilate(3).erode(2)
morph_b = hue_b.threshold(200).erode(2).dilate(3).erode(2)
morph_a.scale(0.4).rotateLeft().save("hue_a_morph.png")
morpha_b.scale(0.4).rotateLeft().save("hue_b_morph.png")

#regions we are unsure and label as gray
middleA = hue_a.threshold(200).erode(1).dilate(2).invert()/2
middleB = hue_b.threshold(200).erode(1).dilate(2).invert()/2
middleA.scale(0.4).rotateLeft().save("middle_a.png")
middleB.scale(0.4).rotateLeft().save("middle_b.png")

#watershed mask
innerA = morph_a.threshold(190).erode(1).dilate(1).erode(1)
innerB = morpha_b.threshold(200).erode(1).dilate(1).erode(1)
middleA = morph_a.threshold(190).erode(1).dilate(3).invert()/2
middleB = morph_b.threshold(200).erode(1).dilate(3).invert()/2
a_mask = innerA+middleA
b_mask = innerB+middleB
a_mask.scale(0.4).rotateLeft().save("mask_a.png")
b_mask.scale(0.4).rotateLeft().save("mask_b.png")

#watershed algorithm



