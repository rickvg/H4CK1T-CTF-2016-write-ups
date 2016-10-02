#Write-up F1r3d&H4ck3d (Egypt) - H4CKIT CTF 2016

Challenge text:
One fine day the war began and all the businesses in the country were stopped. Many companies have laid off their employees and dissolved entire departments. But $

In this challenge, you receive a ZIP-file named: "FiredAndHackedNew.zip". As the file is too big, I can not add the complete file to this repository. This file contains multiple files and folders, like DOC-files, RTF-files, JPG-files, PCAP-files and binaries.

In this challenge there are three types of files, which are interesting: The RTF-file (images.rtf), PNG-file (work.png) and the PCAP-files in folder "1".
The RTF-file contains a URL to a TXT-file on the internet, which appears to look like a dictionary. I have attached this file to the repository as "dict.txt".

The PNG-file shows an image of three networks, where two networks have special SSIDs: FLAGPART1 & FLAGPART2.
FLAGPART1 has MAC-address 5C:4C:A9:AE:2D:A1 and FLAGPART2 has MAC-address 20:7C:8F:9A:1E:A3.
<img src="https://github.com/rickvg/H4CK1T-CTF-2016-write-ups/blob/master/Write-up-F1r3d-H4ck3d/work.png?raw=true"</img>

The image hints towards the available PCAP-files. The PCAP-files contain 802.11 packets, where the data is (unless I have the key/password) encrypted using WPA an$
I downloaded and installed Aircrack-ng and moved all PCAP-files to one folder and renamed the files to out[number].pcap. After extracting the aircrack-ng file, a $
It looks like the employee has also used Aircrack-ng to crack the keys. Note: He collected multiple PCAP-files (needed for IV-based cracking on WEP), he used a di$

Cracking the WEP-key using the IV-attack does not work for those PCAPs. However, I found, using the dictionary with a little brute forcing (guessing) results in t$
I ran the following command:

>aircrack-ng -w h:dict.txt -f 10000 -a 1 -b 5C:4C:A9:AE:2D:A1 out*.pcap

Results:

>                                                   Aircrack-ng 1.2 rc3<br/>
><br/>
><br/>
>                                      [00:00:47] Tested 80208652 keys (got 14405 IVs)<br/>
><br/>
>   KB    depth   byte(vote)<br/>
>    0   73/ 81   18(15360) 5F(15360) 99(15360) AE(15360) BC(15360) DB(15360) E3(15360) EA(15360) 0E(15104) <br/>
>    1   29/ 33   58(16896) 2F(16640) 37(16640) 3D(16640) 52(16640) 82(16640) A6(16640) C2(16640) D2(16640) <br/>
>    2    3/ 33   39(20224) 87(19968) 57(19712) 94(19712) B1(19712) 81(19200) ED(18944) 1F(18688) 41(18688) <br/>
>    3    3/ 38   67(18688) F6(18432) 35(18432) F1(17920) F4(17920) 8C(17920) 13(17664) 3D(17408) 60(17408) <br/>
>    4    2/ 24   40(19200) 8C(18944) B5(18944) E3(18944) AE(18688) 51(18432) 70(18432) B6(18176) 05(18176) <br/>
><br/>
>                     KEY FOUND! [ 18:25:39:67:40 ]<br/>
>       Decrypted correctly: 100%<br/>

After finding the key, I decrypted the WEP packets.

Decrypt WEP-pcap:
airdecap-ng -b 5C:4C:A9:AE:2D:A1 -w 1825396740 out10.pcap

To find the WPA-key, I ran the following command:

>aircrack-ng -w h:dict.txt -f 10000 -a 1 -b 20:7C:8F:9A:1E:A3 out*.pcap

Results:
>                      KEY FOUND! [ 4kymmenkertaistuvan ] <br/>
><br/>
><br/>
>      Master Key     : 93 71 FD 7E 75 06 3A 31 DD B7 8E 5E C6 8F 81 B1 <br/>
>                       0C 5C 89 A1 9D 84 DB B0 EF 82 D6 F1 7F 65 60 2A <br/>
><br/>
>      Transient Key  : BE 62 EE B6 3E 3A BB 1C DF CE 0A C0 CE BC 14 0A <br/>
>                       A1 97 36 C2 EF 31 F8 87 94 DA 8D 00 9D FB 3B 1B <br/>
>                       A8 33 86 F4 7A C1 7E E9 D8 4D 41 3F 1A 4E A7 8E <br/>
>                       3E 96 87 4B 1D EF 05 6C B8 73 7A 21 6B B1 E4 3B <br/>
><br/>
>      EAPOL HMAC     : B7 C8 3F AD 4B 64 93 C2 25 19 60 19 3A 5C FB 45 <br/>


Decrypt WPA:
>airdecap-ng -b 20:7C:8F:9A:1E:A3 -e FLAGPART2 -p 4kymmenkertaistuvan out1.pcap

None of the decrypted PCAP-files contained interesting information, so I figured the flag is part1 key + part2 key.
> h4ck1t{18253967404kymmenkertaistuvan}
