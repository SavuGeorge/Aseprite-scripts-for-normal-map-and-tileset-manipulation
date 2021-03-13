# Aseprite-scripts-for-normal-map-and-tileset-manipulation

Installation: 
Copy contents of 'Scripts' folder into the Aseprite scripts folder. ( Can be opened in Aseprite using File > Scripts > Open Scripts Folder )
Scripts can now be used from File > Scripts.




CreateNormalDonuts:

Uses layers labeled 'r' and 'g' with normal maps drawn for upper middle tile and/or upper right tile. Rotates and recalculates normal value per-pixel.

![Normal rotate](https://user-images.githubusercontent.com/36958266/111036898-54bb8380-842a-11eb-8d45-dcb563139275.png)


FinalNormal & SplitNormal:

FinalNormal combines layers labeled 'r', 'g', and 'b' to create a full normal map. Optionally uses a layer labeled 'a' to add an extra value in the alpha channel.
SplitNormal takes a normal map and splits it into 3 separate r g b images. Essentially the reverse of FinalNormal.

![Combine normal maps](https://user-images.githubusercontent.com/36958266/111037015-f04cf400-842a-11eb-9ee0-95b1fb0cea08.png)


TileDonut

Rotates and copies upper middle and upper right tiles of the currently selected layer to create a full donut.

![Aseprite Donut](https://user-images.githubusercontent.com/36958266/111037038-12df0d00-842b-11eb-9b0f-1d2daf8998f8.png)




Layers layout:

![Layers](https://user-images.githubusercontent.com/36958266/111037045-196d8480-842b-11eb-94e7-ed75ad72950c.PNG)




