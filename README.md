# L-Line
## IVR phone system created through the Pystrix agi 

*Started research:* 3/17/19 

*Started coding:* 3/30/19 

## Description:

Ivr phone system using the the pystrix library to access the Asterisks agi. Created in Python 3.7 this is a rough draft of the final 
product.I made this so that I could automate a phone system that was being used on floor for easier handling. There is more work to be completed as well as needs to recreate the Freepbx server that the whole system runs off of. I learned how the Pystrix library worked as well as multiple new commands I can use for future projects to better the current phone system. This is mostly made with If elif statements and randomizers planning to upgrade everything to be understood in a Decision tree under the recommendation of a friend. I also plan to try to create functionality to have it modular to make it easy to be used in multiple situations. The hardest part of this project was finding a current up to date library with all the commands I needed available to be used. You will need a working voip phone system running asterisks on a freepbx server. From there you take the main file **L-Line-IVR** and upload it into your server. You will also need to download or create audio files to add in as well to create the audio portion for this to work.


## Needs:

 - [x] to have IVR functional 
 - [x] to be mostly based out of python 
 - [ ] to be customizable for the future
 - [ ] to be able to be accessed easily
 - [ ] to be able to add new audio files on the go 
 - [ ] To create an easily expandable IVR that has general capabilities
 
## Next Steps:

1. Make alternative in Decisions trees
2. Have audio files accessed by classes
3. Remake phone system.

## Sources:

[Asterisk AGI](https://www.voip-info.org/asterisk-agi)

[Asterisk Docs](http://www.asteriskdocs.org/en/3rd_Edition/asterisk-book-html-chunk/AGI-communication.html)

[Google link for IVR](https://www.google.com/search?rlz=1C1CHBF_enUS774US774&ei=wwahXI_wM62Rggep0LOIAg&q=writing+IVR+pyst+in+python&oq=writing+IVR+pyst+in+python&gs_l=psy-ab.3...39946.42816..43743...0.0..0.100.948.10j1......0....1..gws-wiz.......33i10.MT04jQDu7Vg)

[Pystrix documentaion](https://buildmedia.readthedocs.org/media/pdf/pystrix/latest/pystrix.pdf)

[Github for Pystrix](https://github.com/IVRTech/pystrix/blob/master/doc/agi/index.rst)
