# Write-up 1mageP1son (Mozambique) - H4CKIT CTF 2016

Challenge text: <br/>
Implementing of the latest encryption system as always brought a set of problems for one of the known FSI services: they have lost the module which is responsible for deconding information.
And some information has already been ciphered! Your task for today: to define a cryptoalgorithm and decode the message.

In this challenge you receive a PNG-file called space.png. The image is shown below:
*IMAGE*

When examining the file, you can see pixels in the left side of the image which are coloured differently than the rest of the image.
There seems to be a pattern in it as the distance between those pixel is the same. This could possibly be our Stego message!

As we are measuring the distances in GIMP we can conclude:
* Block size = 24x24 pixels
* Size of blocks with blocks = 1512x1512 pixels

This means, we can start collecting the pixel data and hope we will retrieve a message out of it. In order to do this, I wrote a script to write the pixels to a new image file.
This script can be found in this repository.

Note: The new image has a size of 64x64 pixels as 1512 / 24 + 1 (including last one) = 64. We have collected 64 pixels, so the resulting image will have this size.

Result image:
*IMAGE*

The resulting image contains the visual flag:
> `h4ck1t{SPACE_IS_THE_KEY}`

