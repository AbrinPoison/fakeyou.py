import fakeyou

fy = fakeyou.FakeYou()

# Call the login method with email and password and await the result
fy.login("< email >", "< password >")


#Insert text you want to be generated in parentheses
text= ""

#Insert voice model Ex: weight_d12c6mztpdcejj7g8maqfb4ja
voice_id= ""

#add directory in front of fakeyou.wav
fy.say(text, voice_id).save("fakeyou.wav")