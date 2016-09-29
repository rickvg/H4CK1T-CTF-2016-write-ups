#Write-up p13c3 0f c4k3 (Brazil) - H4CK1T CTF 2016

Challenge text:<br/>
There is a suspicion that one of the data center agents concealing part of the information. Find out what kind of data Agent is hiding.

Challenge file:<br/>
Docs_9edf906b0a90f66016f45473411a76f8.zip

Category: Forensics

The challenge file contains a folder, called "Docs". If you open this folder, you see a set of files.
I need to find a data about files or files that have been in this folder. The only known file to get this information is "Thumbs.db".
Thumbs.db is known for containing metadata or thumbnails of image files, even when the actual image files have been deleted.

To view Thumbs.db properly, I used a tool called "Vinetto". It is specifically designed to examine Thumbs.db files.
I ran the following command to execute Vinetto:

> vinetto Thumbs.db

This resulted in the following output:

>` Root Entry modify timestamp : Tue Sep 20 20:15:34 2016 <br/>
>
> ------------------------------------------------------
>
> 0001   Tue Sep 20 13:49:44 2016   1342116275_006.jpg
> 0002   Tue Sep 20 13:49:56 2016   1361191423_97e1040f8c75.jpg
> 0003   Tue Sep 20 13:51:16 2016   1409560635-3a78363c4eb9dc3a7719e6c075b46607.png
> 0004   Tue Sep 20 13:49:34 2016   625.jpg
> 0005   Tue Sep 20 13:50:58 2016   193765_original.jpg
> 0006   Tue Sep 20 13:58:50 2016   h4ck1t{75943a3ca2223076e997fe30e17597d4}.jpg `

The name of the last file is the flag:
> `h4ck1t{75943a3ca2223076e997fe30e17597d4}`
