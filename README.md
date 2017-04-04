# insta-Unfollow-Users

[Edit: This script stopped working after Instagram changed its API behavior. I have a plan on updating the script whenever I get time. I'll probably have to use some workaround to accomplish this. Thank you for your patience!]


This is a script/bot to unfollow all instagram users that are not following back

There are people who follow you to make you follow back, and then unfollow you.
Also, many a time, you follow a person but they do not follow back.

Presenting Instagram User Unfollower! 
This is a bot/script to unfollow the users that are not following you back. Simple as that. No strings attached.

Instructions:-

First off, you need to login to instagram and head over to www.instagram.com/developer

1) Read simple instructions here -> http://www.slickremix.com/docs/how-to-create-instagram-access-token/ 

In addition to that, click on "Edit" after you've saved a client. Goto security, and untick "Disable implicit OAuth". We are doing that because we are going to implicitly call the APIs (without providing password everytime)

Copy paste this URL in your browser : https://instagram.com/oauth/authorize/?client_id=[CLIENT_ID_HERE]&redirect_uri=http://localhost&response_type=token&scope=basic+likes+comments+relationships+follower_list

2) Watch the 2 min video, if step#1 is not clear -> https://www.youtube.com/watch?v=LkuJtIcXR68

3) Save the access token in config.txt file as:-

access_token=newly generated token

for ex: access_token=575199251.7in678i.g23atb436f6ba0fs8gi587f6a4esdcg3

We need this access token to make requests to instagram.

4) And that's it, download the executable instaUnfollower.exe.

5) Place config.txt in the same folder as executable

6) Double click the .exe file, sit back, grab a beer, and let the script do its work.

You're welcome.
