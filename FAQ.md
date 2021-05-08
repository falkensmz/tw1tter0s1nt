F.A.Q - Frequently Asked Questions


 - Does the tool is ready 'out-of-the-box'?

No, tw1tter0s1nt is not functionable out-of-the-box UNLESS, you have the twint Python library installed on your machine. All you need is https://github.com/twintproject/twint and
a Linux distro. I recommend the tested ones which are mentioned in the Readme file.

 - Is it ilegal to use tw1tter0s1nt?

Short answer : No, long answer : it depends. OSiNT in general, is not ilegal. This tool does not use any kind of exploitation module to scrape Twitter. It uses legal methods to do
so (more on https://github.com/twintproject/twint). So, no, it is not ilegal to use this tool.

 - Does it work on Kali Linux?

As I have mentioned in the Readme file, Kali Linux is the OS tw1tter0s1nt was coded in. It is also the distro that I perform the first test on. ParrotSec & Linux Mint are both 
fully supported as I perform test on all of these three. It should work on any Linux distro as long as you have twint (https://github.com/twintproject/twint) installed. However,
Kali, Parrot & Mint are fully supported.

 - What is the tool coded in?

tw1tter0s1nt is coded/programmed/written in Python3.

 - Who is this tool for?

Well, for anyone. Anynone who is looking to find more in-depth information on a person/target (in case of a penetration test/hack). So if you are a Pentester/Hacker, IT student,
journalist or a person, this tool will make your life much easier.

 - Is the project still supported?

Yes, I check and test this tool everyday and come up with new ideas for it. The 2.0.0 update will make it much more interesting to use as it WILL have a command-line interface. (Just
gave a spoiler right there :) )

 - Do I need hacking experience to use this?

No. I made this program just to make your life easier. Weather you are a script kiddie or a professional hacker/pentester, this can and will make your life easier.

 - What about anonimity? Am I hidden when I use this tool?

This is a very important part in my opinion. While you don't need a Twitter account to use this, your IP and DNS can and DO get logged in the Twitter's servers. It shouldn't be
a big problem since you are not doing anything illegal, it's just open source intelligence (OSiNT). But if you do want to be anonymous, I recommend using something like 
anonsurf/proxychains. Anonsurf/kali-anonsurf should work since they use Tor proxies, but if you don't trust Tor (you are not alone), you can use something like proxychains and
plug in your own proxies there. proxychains is not fully supported BUT it should work. Hopefully, I am working on a module in tw1tter0s1nt which will allow you to anonymously
scrape Twitter, so, you will not need to use anonsurf or proxychains.
