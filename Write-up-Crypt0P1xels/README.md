#Write-up Crypt0P1xels (Algeria) - H4CK1T CTF 2016

Challenge text:<br/>
We have received pictures from the enemy companion of the unknown before planet. And we haven't thought up anything better, than to construct DeathStarV3 (the general was a fan of "Star Wars") and to absorb energy of the whole planet! And again we are pursued by problems: that we don't know coordinate! Your task is to determine coordinates of this unique planet (which according to our spy are ciphered in the image). Also he could steal one of the scripts intended for embedding of coordinates. All hope only for you!

The following file is attached to this challenge:<br/>
*CryptoPixels_473e51e6e53cfc47b8f87b8a65a8d542.zip

This ZIP-file contains files: encrypted.png and SECRET_TOOL.py. The Python-script SECRET_TOOL.py is used to encrypt the stego-data into the PNG file.

The image:
<img src="https://github.com/rickvg/H4CK1T-CTF-2016-write-ups/blob/master/Write-up-Crypt0P1xels/encrypted.png"</img>

The functions of script "SECRET_TOOL.py":
* Opens an image: "original.png"  and converts it to RGB data;
* Calculates random integers x and y between 1 and 255;
* It changes pixels in the RGB-image, where the pixel on position x=0, y=0 contains the length of the flag, including the x- and y-value of the next pixel that contains encoding;
* It calculates the new position of x and y, indicating the position of the next pixel. This forms a chain that is recreatable;
* The data stored in the pixel is converted from ASCII to decimal, using ord().

In order to solve this challenge I have created a script, which is added to this respository.

The functions of the script are:
* Opening the image: "encrypted.png" and convert it to RGB data;
* Get the length of the flag from pixel on position x=0, y=0;
* Get x- and y-values of the position of the next pixel;
* Retrieve decimal value from next pixel, including the x- and y-values, and convert it to ASCII text using chr();
* Append all found characters to a string and eventually, after variable i reached the value of flaglength, print the actual string.

The string is:
> `1NF0RM$T10N_1$_N0T_$3CUR3_4NYM0R3`

The flag is:
> `h4ck1t{1NF0RM$T10N_1$_N0T_$3CUR3_4NYM0R3}`
