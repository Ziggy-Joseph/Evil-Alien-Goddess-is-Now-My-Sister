# The script of the game goes in this file.

# Define characters used by this game. The color argument colorizes the name of the character.
# Define characters used by this game. The color argument colorizes the name of the character.
define l = Character("Live", image = "live", color="#9AFEFF")
image live = "images/EAG Temp Sprites/Temp_Live.png"
image live smile = "images/EAG Temp Sprites/Temp_LiveSmile.png"
image live annoy = "images/EAG Temp Sprites/Temp_LiveAnnoy.png"
image live angry = "images/EAG Temp Sprites/Temp_LiveAngry.png"
image live regret = "images/EAG Temp Sprites/Temp_LiveRegret.png"


define r = Character("Re-Venus", color="#B7F347")
image revy = "images/EAG Temp Sprites/Temp_Revy.png"
image revy happy = "images/EAG Temp Sprites/Temp_RevyHappy.png"
image revy fluster = "images/EAG Temp Sprites/Temp_RevyFlush.png"
image revy cry = "images/EAG Temp Sprites/Temp_RevyCry.png"
image revy pout = "images/EAG Temp Sprites/Temp_Revypout.png"
image revy menace = "images/EAG Temp Sprites/Temp_RevyMenace.png"

define k = Character("Kashmal", color="#F6F7CC")
image K = "images/EAG Temp Sprites/Temp_Kashmal.png"

define n = Character("News Lady", color="#ED9106")

define p = Character("P. Minion", color="#1B8F1A")
image PM = "images/EAG Temp Sprites/Temp_PM.png"


#Set temporary Backgrounds
image LiveOffice = "images/LiveOffice.png"
image hallway = "images/Hallway.png"
image RevysRoom = "images/RevysRoom.png"
image Cave = "images/PlantCave.png"

#Set CGs
image Revymonster = "images/Requested_Construction.png"
image PlanetBoom = "images/PlanetBoom.png"
#image RevyNow
#image RevyCleaning
#image Ice Cream
#image flashback

#Set variables that control endings
$persistent.goodEnding = False
$persistent.routeBEnd = False


# ________________________________________________________________________________________________

# The game starts here.
#Special Scene to direct players who've completed both Good Endings to Secret Epilogue
label start:

    # Check if players have reached the secret ending and send them where to go accordingly
    if persistent.goodEnding == True and persistent.routeBEnd == True:
        
        #dark screen
        scene dark background with fade
        show K
        k "Oh, hello there."

        k "It appears you've already seen the various endings to this story."

        k "Now that you have, would you like to see what happened {i}after{/i} those two finsihed cleaning?"

        menu:
            "I would like to.":
            #Go to the secret ending
                hide k
                jump secret_epilogue
            "No thanks. I want to see the bad endings.":
            #Start normally
                jump prolouge
                hide k

    else:
        jump prolouge
        hide k

#_________________________________________________________________________________
    
# Prologue 
# Opening Narration
label prolouge():
    # scene Re-Venus Destroying Stuff
    scene Revymonster
    stop music fadeout(3)
    play music 'audio/BGM Pack 1 MP3/BGM Pack 1 MP3/woo_scary.mp3' fadein 0.2

    "A few years back, a threat unlike anything in history ravaged my world. A giant, plant-like monstrosity, named Re-Venus, invaded and wreaked havoc with her creations."
    
    "Even the other heroes and I, warriors blessed by the {i}gods{/i}, couldn't do anything."
    
    "That's why people called her the {b}Alien Goddess{/b}."
    
    "After years of fruitless efforts, the other heroes gave up on defeating her."

    "I didn't."

    "I stopped her."

    "{i}But she didn't die{/i}."

    "I can't explain how if I wanted to. All I know is I've found myself in a particular {u}situation{/u}."

    #scene Revy (human form) on the Floor covered in junk food with a video game in her hand.
    scene RevysRoom
    stop music
    pause 1.5
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/beanfeast.mp3" fadein 0.2
    with dissolve

    show revy happy
    r "BIG BROOOOTHEEER! I want more snacks. Cotton Candy Ice Cream!"

    "Behold! The Alien Goddess in her slovenly glory."

    show live at right
    l "{i}sigh{/i} I am not your slave, Revy. Besides, I have work to do."

    show revy pout with dissolve
    r "But I'm HUNGRY! I wanna eat more sweets! I wanna!!!"
    show live angry at right
    l "I can't do it right now. I have a nation to run! Besides, you will get your human body fat if you keep this up."

    show revy cry with dissolve
    r "WAH! Why are you so mean to me? Can't you see I'm trying to blend into human society? Maybe I should destroy the world after all."
   
    stop music fadeout(1.0)
    show live annoy at right
    l "..."

    "This is her now. A lazy woman with the mind of a child who can destroy the world at any moments notice..." 
    
    "... My {b}adopted little sister{/b}."

    "Welcome to my life." 

    jump liveOffice

#__________________________________________________________________________________________
label liveOffice():

    #Switch to Live's Office Bg
    scene LiveOffice
    with fade
    
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/beanfeast.mp3" fadein 0.2
    n "{i}Good morning, {u}Venera City{/u}! Are you having a good rest? Well, get excited because tomorrow marks the third anniversary of our victory against the Evil Alien Goddess, Re-Venus!{/i}"
    
    show live annoy at right
    l "Almost... done..."

    "I rain my fingers on the keyboard, pelting the smooth keys like a rain storm." 
    
    "The morning sun breaks past the skyscrapers in the corner of my vision, heating the cold air blending with the salty scent of sweat mixed with my city's musk pouring through the window." 
    
    "From the other monitor, a newcaster recounts a story I know all-too well in her annoyingly bubbly voice."

    "After all, I was there for the full of it." 
    hide live 
    menu:
            "Listen to the News Lady":
                jump listen_to_exposition
            "Focus on work":
                jump focus_on_work

# Define the labels for the choices.

label listen_to_exposition:
    
    play music 'audio/BGM Pack 1 MP3/BGM Pack 1 MP3/woo_scary.mp3' fadein 0.2
    # Your exposition text goes here.
    n "{i}Isn't it unbeleivable how nearly half a decade ago the skies were filled with horrific alien plant monsters? Hideous maws as long as crocodiles and some tore through buildings with their tendrils!{/i}" 
    
    n "{i}Our cities became forests from our worst nightmares. But that was {b}nothing{/b} compared to their leader, the Alien Goddess herself.{/i}"

    "My eyes betray me, drifting to the monitor playing the news. The sight of Revy's grotesque monstrous form brings back memories. None pleasant."

    "Towering over skyscrapers, destructoying all indiscriminately, as if programmed. All those monsters she spawned were a part of her mind and acted on her emotionless will."
    
    "On the rare occasions she spoke her tone lacked a shred of emotion."

    "And of course, her overwheliming power that invalidated anything on the planet, including us heroes."

    n "{i}The Divine Heroes, as their names suggest, receive power directly from one of the gods, acting as their personal prophet Only the greatest people can recieve their honor.{/i}"
    
    n "{i}Like Venera City's beloved leader, The Hero of Lightning, Live.{/i}" 
    
    n "{i}He's done so much for us with keeping us safe and running our... Oh, my apologies. I went ahead of myself.{/i}" 

    "Her tone reminds me of high-quality plastic, as if some resentment is mixed with her genuine admiration. I'll add addressing PR to the To-Do List."
    
    n "{i}In other news, I hope you are all prepared for the Triumph Festival for our with the other heroes' nations...{/i}"

    "I snap my attention to my project's monitor and let the News Lady's voice flow through my ears." 

    # Continue with the story or dialogue.
    jump focus_on_work

label focus_on_work:
    pause (1)
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/beanfeast.mp3" fadein 0.2
    # Continue with the story or dialogue.
    show live annoy at right
    l "{i}sigh{/i} That's right. The Triump Festival is tomorrow. Each city presents a new innovation before the gods in celebration of our victory against Revy. First I have to clean up the mess left by the incompetents."

    "I rummage through many open computer tabs to find the To-Do list, squinting with tired eyes until I can read it."
    
    
    l "Let's see... There's finishing up Venera City's contribution to the festival, helping our Oracle prepare for tomorrow's speech, the ends of the construction deal to finish off repairs on the city..." 
    
    l "... a group of bandits in the mountains has been revealed, monsters have taken up trade routes, five charities to dole out funds to, Mrs. Sprocket needs help with her car, about 20 lost pets..." 
    
    show live annoy at right
    l "{i}Give me a break{/i}."

    "A groan escaping my lips, I lean back in my office chair. The momentum generated by my shifted weight rolls the seat towards the wide window behind me." 
    
    "I spin around on the chair and take in the view."

    show live smile at right
    l "It's amazing we've managed to recover this much in only three years." 

    "I remember when Venera, like the major cities, were a pile of debris and swarmed with giant vegetation. The only traces of destruction left are some half-complete buildings."

    "This was thanks to the gods lending a hand. Reconstruction was smoother in the first year than any nation in history. But I can't discount how all the people worked together tirelessly to repair what we lost."

    show live angry at right
    "{b}So it baffles me when people turn in such low-quality work!{/b}"

    show live at right
    "Regardless, if I didn't do what I did then life wouldn't be able to resume like this. It would all be gone."

    "But being a hero is massive undertaking. Without big threats like Revy, the job becomes more administrative than combative. {i}I love it{/i} but it's work." 
    
    "Besides, without the power, influence, and wealth of my job, keeping Revy safe while providing would be impossible."
    
    pause 0.5

    "Those solar energy converters I installed and the various food and soil testings... just so I'd {u}know what she needed to eat{/u} were neither easy nor cheap to develop." 

    "I borrowed my network to forge some identities for her and naturally keep everything about her quiet."

    show live at right
    "And speak of the gremlin herself as I hear her childish cries down the hall."

    show revy happy at left
    r "BROOOTHEEEER!"

    "That annoying screech of a young girl who doesn't realize the stupidity of what she just did could only be one person."

    "Channeling electric magic from my fingers, I thrust out my arm to the intercom I built for this situation. It only goes to Revy's room and this one can only be used with my magic."

    "I press the green button and light shines in matching colors."

    #Choice: Respond Angrily vs Respond Annoyed
    menu:
        "Respond Angrily":
            show live angry at right
            l "What do you think you're doing, yelling down the halls, you idiot?!"

        "Respond Annoyed":
            show live annoy at right
            l "Revy, stop making me remind you to not yell down the halls."

    show revy cry with dissolve
    "The entire world believes Re-Venus is dead. She may look different now, and is not as powerful as she used to be, but she's still more than strong enough to end the world."

    "It may seem foolish to hide her in the same place I do work but it's ironically the perfect hiding spot. Nobody would think that the feared apocalyptic plant goddess was hiding out in a hero's company."
    
    show live regret at right
    "Although, to be fair, there were likely better options for her if I wasn't bogged down by reconstructing society, but here we are."

    "After a few seconds of crocodile sniveling, Revy's whines boom through the intercom. The sound grating my ears."

    show revy pout with dissolve
    r "There's no point, you big meanie pants! Nobody's here right now."

    "A fair point. However..."

    show live
    l "By the way, how has controlling your powers been going?"

    show revy fluster with dissolve
    r "{i}Urp...{/i}"

    show live annoy
    l "That's what I thought."

    "Plant manipulation abilities do exist in this world but none match Revy's in looks or power. If anyone, ESPECIALLY another Hero, see her use them, she'll never be left alone again."

    "Revy may be... this way now, but she's stronger than anything in this world. Combine that with her immaturity and moodiness and going outside without me is an automatic {b}no{/b}."

    "And yet she listens to {i}me{/i}. Sometimes, anyways."

    l "Anyways, what do you want? What're you even doing up at this hour? Did you spend all night gaming again?"

    show revy 
    r "O-Obviously not, dummy! I'm just... hungry, yeah! Gimme breakfast. Pancakes with extra syrup and chocolate, now."

    "I bite my tongue to stop my retort. With a human body, Revy awakened to the taste of human food, especially sweets." 

    "But that's ALL she eats aside from sucking the nutrients out of meat! I understand not wanting to eat vegetables as a plant-person, but if she doesn't balance her diet she will get fat."

    "Although, saying that will make things end up like last time. Not a good idea."

    l "I'll have Chef-Bot make some for you."

    show revy fluster with dissolve
    r "{i}laughs hesitantly{/i} About that..."

    show live angry at right
    l "You broke him again?!"

    show revy cry
    r "Eek! Don't yell at me."

    show live
    l "{i}sigh{/i} Sorry."

    show revy with dissolve
    r "I didn't break him. I just... {i}want you to make them for me{/i}. Yours are better anyways."

    l "I can't. I'm busy with work."
    
    show revy pout
    r "Then I'm gonna shout really loud so the people outside can hear me!"
    
    "HAH! As if I'm not prepared for that." 
    
    "When I had my home reconstructed after Revy's invasion I {i}soundproofed{/i} the walls."

    "But... it'll be annoying if she does yell."

    show live annoy
    l "{i}SIGH{/i} Alright. Just be patient, okay? I'll bring them up in a bit."

    show revy happy with dissolve
    r "Yay! Thanks, big brother."

    show revy with dissolve
    r "Oh, one thing."

    l "What is it now?"

    stop music
    show revy menace at left
    r "{b}Make double{/b}."


    hide revy menace with dissolve
    show live regret
    "An icy tone followed by a hang up. The cold delivery on her words reminds me of how she used to speak. What a way to start the day."

    show live
    "I stand from my chair, stretching my arms to the sky, and yawn as the sensations of exhaustion creep over me."

    "Come to think of it, I didn't sleep much either."

    "{i}RING RING{/i}"

    "Suddenly, my phone rings aloud." 

    "I pick it up and I'm greeted with static violating my ears."

    "{b}Just perfect.{/b}"

    "I hang up."

    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/frozen_winter.mp3" fadein 0.2

    show K 
    k "It's rude to hang up on someone like that, you know."

    "Suddenly, steel tablet pops out of the wall, electricity pulsing from the screen. A jagged wavelength like a soundbar fluctuats as a mature woman's voice reverberats with a powerful pulse."

    "A cold sweat beads on my brow. Without hesitating, I bow before Venera's {i}Patron Deity and the Goddess of Electricity{/i}."

    k "Rise, Live. I am not here to punish you. Besides, our relationship is much more than Deity and Subject. Why don't you call me {i}Big Sister{/i} like you used to as a kid?"


    l "With all due respect, Lady Kashmal, I need to respect your standing at all times."

    "Yeah, our relationship is complicated."

    "The gods' true forms exist outside the bounds of reality but they like to take the form of humans and mingle with us. They aren't perfect beings, but they care for us even if sometimes they don't look like they do."

    "Kashmal always stayed in her temple and innovated new inventions which she'd then pass as wisdom to great minds among her people." 
    
    "However, she took me in and raised me when I lost my parents. She was weird, though. While I consider her more a mother, she treats me like a younger brother instead. Don't ask me why." 

    "I guess she and Revy have that in common." 
    show live annoy
    l "What do you need... {b}Big Sister{/b}?"

    "The vile pain called cringe rips through me as I said those words."

    k "I was experimenting to see if my electricity could manipulate gamma radiation backwards... It did not work out."

    show live
    l "Well, if {i}you{/i} can't then I don't think anyone can."

    "Electricity is HER domain after all." 

    k "You're such a good boy, you know that? You should really take a break once in a while?"

    "I can do without the teasing, thank you."
    show live annoy
    l "{i}I can't{/i}. Everyone is stressed repairing their lives and can't focus on work. I have to make sure this country you love is as prosperous as I can."

    k "Yet you can give the tasks currently on your list to others. I reviewed the work you did on your computer. I'm quite impressed with thought out and detailed it was." 
    
    k "I'm certain people will be able to follow it with no trouble."

    l " If I do, they'll mess everything up. All these people... all they do is get anxious and make mistakes--making me clean it all up last minute! It's much easier if I handle it all."

    k "Why don't you calm down a little?"
    show live angry
    l "I am {b}CALM{/b}!"

    stop music
    pause 1
    
    "An electronic giggle bounces across my ears."

    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/frozen_winter.mp3" fadein 0.2
    show live regret
    l "Urp..."

    #Choice: say nothing vs apologize
    menu:
        "Say nothing":
          
            "..."
        "Apologize for my outburst":
            
            l "Please forgive me..."


    k "All is well. That is why I came as I did. If I appeared before you as my true self I'd have had to punish you. {u}Neither of us want that{/u}."

    l "O-Of course."

    k "Go and make you and Revy breakfast. Then maybe you'll see the irony of your actions."
    show live
    l "All right."

    "I breathed deeply and let out a gentle breath."

    show live smile
    l "Would you like me to make you some too, Lady Khasmal?"

    "Gods don't {i}need{/i} to eat but they do appreciate offerings. Kashmal won't admit it but she has a sweet tooth."

    k "I would absolutely adore some, but please ease on the carbs for mine. Also, coffee would be appreciated."

    k "Oh, and when you deliver Revy's food, {u}think carefully on what you say to her{/u}." 

    k "Be sure to call me if you need something, but please don't use radiation-based devices." 

    hide K with dissolve
    pause 2.0
     
    show live
    "The screen slides away as fast as it appeared. I still don't know how she makes those things appear, and I designed this house!" 
    show live annoy
    "I also didn't get why she even cares about carbs when she can take whatever form she wants."

    "Why does she need to remind me about radiation all the time too. I guess even the gods get bitter when they lose?"
    show live angry
    "I can't help if I don't know what the problem is!"
    show live regret with dissolve
    l "Can't help..."

    stop music fadeout(1)
    "Flashes of despair and anxiety of the war against Revy's invasion go off in my mind. I still haven't forgiven her entirely but those feelings stuck out among the memories."

    "We {b}should have{/b} lost to Revy. I'm the only one in the world who knows the truth. Everyone else thinks we killed her." 
    
    "We got extremely lucky she decided to stop."

   
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/beanfeast.mp3" fadein 0.2 
    show live
    l "{i}sigh{/i}"

    "Well, there's no use dwelling on the past."

    l "All right."

    "I stretch some more, twisting and pulling my muscles to their limits until I felt my flowing blood wash away some of the numbness."
    
    "After another deep breath, I allow my electric powers to build within me, circulating until they're about to burst."

    "Finally, they explode in an aura of cackling electric charge." 
    
    "In a flash I speed to the kitchen, the walls of my house blurring beside me. I made the pancakes as ordered, setting aside some normal ones for Kashmal. I made some coffee as well, two cups for me and her. "

    "As I set aside her pancakes and coffee, a piece of the wall flipped open and mechanical arms quickly snatch the food and beverage, yanking it into the darkened shoot before it seals shut."

    k "Thank you!"

    "I scratch my head. I'm getting used to it now but back in the day it would always scare me."
    show live annoy
    l "I do not understand them, at all."

    "{u}Divine beings{/u}. Kashmal and the other gods could've probably defeated Revy. And yet they did nothing until the end."

    "I know why--Kashmal told me herself--this is our world. The human world. They run the stuff behind the scenes and help us out if faithful. I could ask further why, but I worry about prying where I'm not welcome."

    "Was Revy a god too? She needs to eat so maybe not. I understand her just as much, though, and her powers are beyond any creature on the planet."

    "{i}Why did she choose this life when she could take whatever she wanted?{/i}"
    
    show live
    "I decide to stop thinking about it."
    
    "As the last bit of bitter coffee slides past my lips and feeling that necessary jolt of caffeine, I plate the double-order sugar disaster pancakes and headed to her room." 
    show live regret
    l "Oh, gods help me..."

    "What I saw {i}horrified{/i} me."
    stop music fadeout (.2)
    #Moves to the first Choice section
    jump choice1
#________________________________________________________________________________________
label choice1():
    #Change Scene to Revy's Dirty Room
    scene RevysRoom
    with fade
    pause .5
    show live angry at right
    l "Can you explain to me why this is such a mess?!"
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/dramatic_boi_v5.mp3"

    "Revy lies on her bed surrounded in crumbs, empty wrappers, and filthy clothes, her eyes trained on the video game held directly over her face. A strange drama played on the monitor behind her, something about a family."

    "The rest of her room faired no better. Clothes, garbage, the works all over the floor place. Items strewn about everywhere with zero shreds of organization."

    show live annoy
    "But somehow, it is {b}worse{/b} as her plants, dark, thick roots and vines with glowing red flowers, blanketed the walls. If not taken care of, those things might eat spawn nasty monsters." 
    
    "And if they got outside, people could get hurt and Revy won't be able to live a normal life anymore."

    show live angry
    "No! This was {i}worse{/i} than a disaster. The only way this could be worse was if things were moldy and decaying."

    show live annoy
    l "How in the world did it even get like this in less than a day? It wasn't like this yester--{i}Answer me{/i}!"

    "Revy finally looks up from her game."

    stop music fadeout (.5)
    pause 1.0
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/beanfeast.mp3" fadein 0.2 
    show revy happy at center
    r "Oh, yay, the food is here! Just a bit. I gotta finish this online match."

    show revy pout with dissolve
    show live angry
    "She's not even {i}touching{/i} the food! She doesn't even seem interested anymore. Why that little..."

    show live annoy
    "Okay. Okay. I have to calm down. I'm lucky she's absorbed in the game or she might have been startled by my outburst."

    show live
    "Now that I have a good look, there are some places to put the food down. If I can get the food close enough to her then the smell should get her attention."

    "I can either place it on the bedstand, which is farther, or the dresser, which is near a fan but with a more cluttered path."

    #choice Place the food on the bedstand vs the dresser
    menu:
        "Bedstand":
            jump bedstand
        "Dresser":
            jump saltEnd

label saltEnd():
    show live at right
    "I make my way to the dresser, trying to avoid stepping the filth but the density makes that impossible."

    "With no choice, I dip my toes in the cesspool of a mess."

    "It's restricting my movement. But I should be fine as long as nothing comes flying at me faster than the speed of sound."

    stop music

    show revy pout at left
    r "Why that poopy-head! He stole my objective!"

    show live regret
    l "What the--?!"

    "Before I could react, a pillow, thrown by the Alien Goddess with alien strength, smashes into my face."

    "The last thing I hear is the sound of my skull caving in."

    "{b}Ending Acheived: Death by Pillow to the Face!{/b}"

    return

label bedstand():
    "On my way to the bedstand, Revy suddenly shouts,"

    r "Why that poopy-head! He stole my objective."

    "She hurls a pillow in my direction, rocketing at high speeds. With nothing in the way I easily dodge it as it flies out the door."

    "I place the food on a small bedstand. Maybe the smell of her favorite breakfast will get her off her butt?"
    show revy with dissolve 
    "The warm smell of fresh pancakes wafted across the room, the aroma rising in a snake-like cloud." 
    
    "Revy's nose twitches; the scent must have reached her."

    "Now I have her attention!"

    show revy pout
    r "Hmmmm!"

    "She moans before straining her focus on her game harder than before, her buttons presses growing louder and faster." 

    "I should have done this from the start."

    l "If you don't stop playing now and clean your room I won't give you the pancakes."

    r "I'll do it later. You're so annoying, you know that! Can't you see I'm busy?"
    
    show revy fluster
    r "{i}Ack!{/i}"

    show revy cry with dissolve
    "The Alien Goddess grows somber as her eyes drooped at the screen. A defeating sound effect plays from her device."

    stop music
    show revy menace
    show live regret
    r "!"

    "She turns to me, eyes full of anger. I battle the urge to swallow my spit before her gaze."
    show revy pout with dissolve
    r "Look what you did! Now I lost to this guy who was being a jerk earlier!"

    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/dramatic_boi_v5.mp3" fadein 0.2
    show live
    "False alarm. Phew! I thought she was about to attack me."

    l "Sure, it's my fault. Now clean your room so we can eat."

    #pout
    r "No! Not until I beat this guy."

    "With a heavy pout, Revy slams herself back into her bed and dives straight into another game."

    "I ball my fingers into a fist. This wasn't working. I need a new plan of attack."

    "What are my options?"
    # Insert menu for Choice 1
    menu:
            "Leave it alone and go back to work":
                # Proceed to Loop End
                jump loopEnd
            "Call Kashmal for advice":
                # Proceed to Route B
                jump routeB
            "Handle it yourself":
                # Proceed to Choice 2
                jump choice2
#________________________________________________________________________________________________
label loopEnd:

    # Loop End content here
    stop music fadeout 0.5
    pause 1.5
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/beanfeast.mp3" fadein 0.2
    show live annoy
    l "{i}sigh{/i} Fine. I'll leave breakfast here and you'll eat when you're ready."

    "I can deal with Revy's room later. Right now I have a bunch of work to do. I brought her the food like she asked. My job is done."

    "Sighing, I leave to the door, putting this nightmare of a room behind me."
   
    "As I wrap my fingers around the circular knob, a voice calls out behind me."
    show revy fluster
    r "W-Wait!"

    "I turn to Revy, who has at least one eye looking in my direction."

    l "What do you need?"
    
    show revy with dissolve
    r "Please don't go..."

    "Her voice is soft and somber, like she's pleading." 
    
    show revy fluster
    "Then her cheeks tinge red before burying herself in her game again."

    show live 
    l "Sorry. I can't..."

    show revy pout with dissolve
    r "Hmmmmmmmmmmm!"

    "A high-pitched, angry groan resounds from her puffed cheeks. Then, with the snap of her fingers, two vines larger than me instantly grow from the foliage on the wall."
    
    show live annoy
    "I pinch the bridge between my eyes and mutter,"
   
    l "I won't be getting back to work until resolve this."   
     
    show live
    l "{i}sigh{/i} You can put those away. I'm not going anywhere right now."

    r "Hmph!"

    "With an angry huff, the vines retract."

    "At least I know she is listening, sort of."

    show live annoy
    l "Good greif."

    "I don't understand her at all."

    #Give the other options
    menu:
            "Call Kashmal for advice":
                # Proceed to Route B
                jump routeB
            "Handle it yourself":
                # Proceed to Choice 2
                jump choice2
#_______________________________________________________________________________________________________
label choice2:

    # Choice 2 content here
    show live at right
    show revy with dissolve
    "I'll try handling this myself."

    "First I need to grab her attention. I'll start by getting closer so I have more presence."

    "I tiptoe around the room, weaving around clothes and alien vine roots strewn about like they security lasers." 
    
    "It was a {u}mess{/u}, my gods." 
    
    "Looking at it was one thing, but now I am swimming through a swamp made of a young woman's trash!" 
    
    "Hold on. I don't even recognize some of this stuff, but I'd rather {i}stay ignorant{/i} to how the ended up here!"

    show live 
    l "How do you even live like this?" 

    "Apparently, she overheard my exclamation."

    show revy pout with dissolve
    r "I need all of this where it is, duh. So don't touch it."

    show live annoy
    l "Because {i}of course{/i} you need all the leftover wrappers for your arts and crafts project." 
    
    show live angry
    l "{b}As if{/b}! Gaming is about all you do around the house!"

    show revy fluster with dissolve
    r "W-Well... I also watch shows! Now let me focus on the match. This guy's my nemesis!"

    show revy pout with dissolve
    "She pulls the screen closer to her face. Now I'm worried she'll get bad eyesight, too. Guess I'll add an eye checkup to the To-Do List."

    show live smile
    "While I lose her attention a flash of wisdom restores my hope." 
    show live
    "I pull my out my phone and quickly navigate through the various apps. Finding the one I needed, I point the front end at the monitor playing her show and press the input."

    stop music fadeout 0.5
    pause 1.0
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/beanfeast.mp3" fadein 0.2
    show revy fluster with dissolve
    r "H-Hey! I was watching that."

    "The small girls' teary eyes lock on to me, her teeth gritting with frustration."

    show live annoy
    "When I became the Hero of Lightning, Kashmal made me ban as much radiation-based devices as I could, even though not all radiation interferes with electricity." 
    
    "So naturally, I redesigned my phone. Then I figured I might as well hook everything in my house, that I also designed, up to it in case of stuff like this."
    stop music fadeout 1.5
    "But the upset person before me had the mentality of a child and the power to make all advantage moot."
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/dramatic_boi_v5.mp3" fadein 0.2
    show revy cry with dissolve
    r "{i}Wah!{/i} My show. Turn it back on, {b}now{/b}!"

    "Her voice rings with frustration as dark green power envelops her, steadily building power." 
    
    "The plants covering the walls move in rhythm with her mood, their branches and vines inching towards me."

    show live
    "But now I had her attention. Next, I'd have to calm her down."
    show live annoy
    "I'm prepared for this. It's my job to ensure she grows up responsibly!"

    "I must tread carefully. One wrong mistake here could end in a massive, {i}destructive mood swing{/i}." 
    
    "I could play it safe or risk going down my current line of thinking."

    menu:
            "Do what would work for me":
                # Proceed to World End
                jump worldEnd
            "Try something risky.":
                # Proceed to Choice 3
                jump choice3        
#_________________________________________________________________________________________________________
label worldEnd:

    "I think I'll try to play it safe." 
    
    "Besides, this is becoming a massive waste of time.."

    show live annoy
    l "You know what, Revy? I'm really not in the mood today. Why don't I just clean this room up for you and be done with it?"
    show revy fluster
    r "Hey, wait--"

    "But I didn't listen. Breifly charging my lightning magic, I let it burst before zipping around the room, sparks flying everywhere I went." 
    
    "I gather all the trash, put all the clothes in the laundry, and stripping the walls of all alien plants. Then I dash to the kitchen and supply closet and began cleaning."

    "It was like an electric blender of scrubbing and organizing, a new record for fastest room cleaning for sure."

    show live smile
    "Finally, I stop and wipe the seat of my brow with a towel." 
    
    "I now stood in a shiny, spotless bedroom that appeared like new. A job well done if I do say so myself."
    
    "Unfortunately, the menacing aura coming from Revy meant I was alone in the sentiment."
    stop music fadeout 0.2
    play music 'audio/BGM Pack 1 MP3/BGM Pack 1 MP3/woo_scary.mp3' fadein 0.2
    show revy cry with dissolve
    r "How... HOW COULD YOU DO THAT TO MY FRIENDS?!"

    "I think back to the alien minion spawners I trashed and then look at her face."

    show live regret
    l "Oh."

    "My eyes widened like satellite dishes. Did she mean the plants I disposed of? She thought of them as friends?"

    show revy menace with dissolve
    r "Grrr. RAAAAAAAAAAAAAAAAAAAAAAAAAH!!!"

    "I move to stop her but it's too late. Revy releases a massive blast from herself, engulfing the entire area and myself in that burning light."
    stop music fadeout 0.2
    #Destroy the world!
    scene PlanetBoom
    with fade

    "{b}Achieved Ending: Yes, the World Ended over Cleaning a Room. Why do you ask?{/b}"

    return
#_______________________________________________________________________________________________________
label choice3:

    show live
    "I already have her where I wanted her. Continuing this line of thought is the best choice."

    "However, I should choose my words {i}carefully{/i}."

    "I take a moment to think over what I'd say. Parlyzing fear sinks its fangs into me as I did. Blast! This was more difficult than I imagined."

    show revy with dissolve
    r "Why aren't you doing anything! Turn back on my show."

    show live regret
    "Her whines weaken my resolve and grant the demon of fear more strength." 
    
    "Sweat oozes from my brow from as my thoughts slow. {i}This is bad{/i}. I'd thought it would get easier after a few years but children are still terrifying to deal with!" 

    "Even though Revy isn't a kid--she doesn't even know her real age--her human body was only present for three."
    
    "She may have matured mentally faster than a three year-old girl but she was hardly at an adult's level." 

    show live annoy
    "Ugh. Now I'm getting a migraine from all these complications!"

    r "Are you even listening to me?! Hey!"
    
    "I feel my forehead vein tense."

    "Did she not see the {i}hypocrisy{/i} in her words?! That's it. She has {b}one{/b} chance."

    show live
    l "I turned it off as punishment. Your room is a mess and you were igrnoring me after I made you breakfast. Now pay attention or I'll make the punishment worse."

    r "{b}Hmph!{/b}"
    stop music fadeout 0.2
    pause 1.0
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/beanfeast.mp3" fadein 0.2
    "She went back to her game, huh? Well, I have bad news for her."

    "I'd need to be careful with this since I need this active more than she did."

    #Choice: Do it vs Try something else.
    menu:
        "Do the thing":
            jump theThing
        "Try another thing":
            jump tryAnotherThing
            
label tryAnotherThing():

    "Maybe I shouldn't do that. Let's see if I can just take the game from her."

    "So I built up a bit of magical charge and speed towards Revy so I can snatch her game."

    show live annoy
    l "{i}Oomph!{/i}"

    "Or so I thought. Instead, I trip over some clothes. FOCUS, Live. FOCUS!"

    "Well, at least Revy's so focused on her game I don't have to worry about anyone seeing my shame."

    show revy happy with dissolve
    r "HAHAHAH! You look so stupid, brother!"

    "As she bellows laughter, I angrily shed all the trash and clothes attatched to me."

    "No more holding back. I'm doing the thing!"

    jump theThing

label theThing():
    "I then shut down {i}another{/i} thing with my phone."

    show revy fluster with dissolve
    r "Wha-? Hey. What's going on. My game disconnected."

    "The confused Alien Goddess fiddles with her game console, moaning and twisting around in frustration, tangling herself in her bed sheets."
    
    show revy cry with dissolve
    "It wasn't long before she bursts into tears and stares daggers at me."

   
    r "Why did the internet stop working? I was about to beat my nemesis!!!"

    show revy pout
    "In an instant, the Alien Goddess had left her bed and stood before me, hands poised on her hips."

    "I admit, it's humorous seeing how her head barely reaches my chest and how she cranes her neck to look me in the eyes."
    
    "The salt in her words makes it all the sweeter. I fold my arms triumphantly."

    show live smile
    l "That's because I shut off the {i}internet{/i}. I warned you that I'd punish you further if you didn't listen."

    show revy pout with dissolve
    r "Hmmm!"

    show live
    l "Pouting won't get me to change my mind."

    r "HMMMMMMMM!"

    "I could feel my blood begin to boil from the annoyance. I tap my finger impatiently."

    show live annoy
    l "Like I said pouting won't change my mind!"

    stop music fadeout 0.5
    show revy menace with dissolve
    "At first, Revy seemed to be stubborn in her pouting method, making sounds for several minutes straight."
    play music 'audio/BGM Pack 1 MP3/BGM Pack 1 MP3/woo_scary.mp3' fadein 1.5

    "Then, her pouts break up like stuttering, her eyes darkening with the room's atmosphere." 
    
    "Something {i}big{/i} was coming. Like her true form but somehow worse."

    "I instinctively swallow some spit while readying myself for the worst, regulating my breath to dampen my rising anxiety."

    show live regret
    l "Oh no..."

    "A {i}storm{/i} was coming, one I feared to brave even with my element."
    stop music fadeout 0.5
    show revy cry
    "Before I could ready myself, tears flowed from the Alien Goddess's eyes."
    
    show revy cry at left
    "Then she throws herself on her bed."

    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/dramatic_boi_v5.mp3" fadein 0.2
    r "WHYYY?! Why? Why? I don't wanna clean my room. Don't you know how boring it is? I wanna play games and eat ice cream..."

    "Her loud screeches nearly tear my eardrums asunder as the room itself trembles!" 
    
    "Revy flails her limbs about--twisting herself deeper into her bed and making it more of a mess."

    "She may not have destroyed the world but this almost made me wish she had."

    "For I am amidst the {b}temper tantrum{/b}." 

    "Gods help me."

    r "... I {u}HATE {/u} boring things. Do you know what it's like being bored? It sucks! Sucks, sucks, sucks, sucks, sucks! My plant friends always entertained me and did whatever I say too. I'm a {u}QUEEN{/u}. Queens shouldn't have to clean! That's the minions's job..."

    show live annoy
    "I duck to the floor and pulled out my specially made noise-cancelling headphones but her screeches somehow made it through those."

    "Good thing her limbs are trapped beneath her favorite sheets or she may have been more destructive!"
    
    show live regret
    "Oh no. Would people notice something this intense? It was early morning so there shouldn't be too many people nearby."

    "How much longer until this agony will end?" 
    stop music fadeout 0.2
    show revy
    r "..." 

    show live
    "Huh? She stopped?"

    #Choice: Wait or Check
    menu:
        "Wait":
            jump wait
        "Check": 
            jump check

label wait():
    "I decide to wait her out."

    "..."

    "......."

    "............................................"

    show live annoy
    "Okay, seriously, what is happening?"

    show revy pout with dissolve
    r "Hmmmmmm."

    "Well, she pouted to get my attention. Like I'd fall for that."

    r "Hmph!"

    "I have a feeling she's growing angrier. Maybe I should check to be safe."

    menu:
        "Wait more":
            jump earEnd
        "Check":
            jump check

label earEnd():
    "I continue waiting for her to snap and do something."

    show revy menace
    r "Why, won't you {b}listen to me?!{/b}"
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/woo_scary.mp3" fadein 0.2
    show live regret
    "Uh oh."

    "I jump up to show her I'm aware but Revy's cheeks were puffed full of her."

    r "WHYYYYYYY?!"

    "A massive sonic wave slams into me, knocking me to the floor."

    "Earsplitting pain tears through the sides of my head as I collapse to the ground."

    "{b}Ending Acheived: Well, You didn't Die this Time, But your Eardrums Sure Did!{/b}!"

    return

label check():
    "I impulsively check to see why Revy stopped."

    show revy
    r "{i}grins smugly{/i}"

    "An error on my part."
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/dramatic_boi_v5.mp3" fadein 0.2
    show revy cry with dissolve
    r "I DON'T WANNA CLEAN. I DON'T WANNA. I DON'T WANNA!"

    show live annoy
    "Ugh! She was checking to see if I was paying attention. That little gremlin!"

    "I clutch my ears and press the headphones in as much as possible to muffle the sound. {u}It was futile{/u}." 

    "In the corner of my vision, I noticed the plants on the walls reaching out to comfort her, failing to reach in their current state. At least they aren't focused on me."

    "She kept going on like this for what felt like hours." 
    
    "As painful as it is, waiting until she exhausted herself is my best bet at surviving without doing anything reckless."

    "The wails and whines assaulted my ears like tidal waves on a stormy sea. I did my best to keep myself afloat, but every second felt like the next would be my last. All I could do was brave the waters and pray it would end soon and safely."
    show revy fluster with dissolve
    "And sure enough, she did." 

    stop music fadeout 3.0
    
    show revy pout with dissolve
    "The wails became cries, then sniffles, and finally silence. Sweet, sweet silence. Or maybe she realized it wasn't working no matter how loud she got."

    r "..."
    
    show live
    "Revy is now tangled in her bedding, head sticking out like she was the filling of a roll cake." 
    
    "Naturally, the place was even {u}more{/u} of a mess now."
    
    show live annoy
    l "... Had enough?"

    "Rising to my feet, I glared at her. It was a little hard, considering the dizziness and ringing in my ears." 
    
    "It was uncomfortable and made me feel stiff as a board, but it's better than nothing." 

    "Now, what will she try next?"

    show revy 
    r "Heehee."

    l "What are you planning now?"

    "Then she shined puppy dog eyes at me."

    r "Oh, would you help you helpless, little girl? Pretty please?"

    show live angry
    l "Kh!"

    "My anger soars. Was she trying to {i}put on an act{/i} by being cute?! Did she think that would work?!"

    #Choice Keep yourself calm vs Discipline the action
    menu: 
        "Keep yourself calm":
            "No. I {i}must{/i} remain calm and handle the situation civilly."
        "Discipline the action":
            "I can't let this slide. This subject is inappropriate, and I can't let it fester in a young girl's head!"
    stop music fadeout 0.2
    show live annoy
    "That being said, losing my cool means I might do something stupid and get myself killed."

    show revy fluster with dissolve
    r "Please can you do this once for me? I'll tell you where to put everything, so just this once, can you help your adorable little sister?"

    "Then she winked."

    "And with that, my self-restraint vanishes."

    show live
    l "Why you..."

    r "Eh?"
    pause 2.0
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/dramatic_boi.mp3" fadein 0.2
    show live angry
    l "!"

    show revy fluster at center
    "My arm shoots forward, grabbing Revy by the head and yanking her out of her covers like uprooting a radish." 
    
    "My fingertips dig into the edges of her scalp like a vice and hold her straight in the air. Her short stature made this feat easier while flailing her limbs in the air." 

    r "{i}Wah!{/i} Stop it please!"

    "A humanoid plant monster spawned itself from the wall from the corner of my vision, peeling from the walls out of its pod."

    show PM at left
    p"!"

    "It reels out its claws made of sharpened treebark."

    l "I'LL DEAL WITH YOU NEXT!"

    p "..."

    hide PM

    "My shout and glare at the thing caused it to freeze up. Despite having no face and therefore eyes and ears, it sat down politely on the ground and waited."
    l "Now... {b}you{/b}!"
    
    r "EEK!! P-Please calm down. You're scaring me!"

    l "I've had it up to HERE with you! First, you ignore the rules I established when you moved in about cleaning and not using the Intercom. Then you're rude when I make you breakfast while interrupting my work!"

    r "I was hungry and in the middle of an online game. I can't pause those!"

    l "You better or I'll take away video games for a month!"

    show revy cry with dissolve
    r "{i}WAH!{/i} Noooo! ANYTHING BUT THAT! I'm sorry. Okay. I'm really, really sorry for everything!"

    show live regret
    l "!"
    stop music fadeout 0.2
    pause 1.0
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/frozen_winter.mp3" fadein 0.2
    "Coming to my senses, I gently lower Revy to the ground." 
    
    "She sits on the messy floor, her knees atop messy clothes. Her tiny fingers massage the spots beneath her leaf-like hair in soft circles."

    "I messed up now. I should apologize before she gets violent." 

    l "Revy, I'm--"

    show revy with dissolve
    r "{i}sniff{/i} It's okay."

    "Her gaze falls to the messy floor, the ends of her small mouth droop downwards."

    r "I messed up. I was right to be punished. Maybe I should go back to being an evil monster."

    "It feels like a knife stabs me through the gut. The thought that I did something wrong to her unknowingly makes my heart sink." 

    show live
    "I should offer some words of encouragement. Or, maybe I should tell her what she's feeling straight to her face."

    menu:
            "Be kind with her":
                # Proceed to Good Ending
                jump goodEnding
            "Be real with her":
                # Proceed to Bad Ending
                jump badEnding
#______________________________________________________________________________________________________________
label goodEnding:

    show live
    "Well, I doubt anyone in her situation would want to be yelled at. Besides, I'm the one who caused her pain."

    "I take a knee and brought my eyes to Revy's level. Fingers spread like net, I reach slowly for her head."
    stop music fadeout 3.0
    pause 1.0
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/frozen_winter.mp3" fadein 0.2
    show revy cry 
    r "!"

    "The Alien Goddess winces on reaction, snapping her eyelids closed. I didn't stop."

    "Finally, placing my hand on her head, the sensation of a strange smooth yet rough texture of leaf-like hair, I gently rub her scalp."

    show revy with dissolve
    r "..."

    l "Does it hurt?"

    r "A-A bit more softly."

    "I ease the strength behind my hand. Her face loosens as the massage releases her tension." 

    "We stay like this for a few minutes until I confirm she was stable." 
    
    #Focus on Revy vs Check on Plant Minion
    "I check on the monster again, just in case he tries anything."
    hide revy with dissolve
    show PM at left
    p "..."
    "He's still sitting like a well-behaved kid in the corner. He's well-trained for a newborn."

    hide PM

    show revy with dissolve
    "Now back to Revy."

    l "Revy, why don't you tell me what's {i}actually{/i} bothering you?"

    "The Alien Goddess's face shifts between several emotions. Fear, discomfort, longing, fear again, anger, and so on."

    "Then she speaks."

    r "... I don't know. I've been feeling really strange on my own lately. No matter how many games I play, sweets I eat, nothing gets rid of that feeling."

    l "So you've been distracting yourself from it with games and shows?"

    r "Mhm! I don't understand what this emotion is and I don't like it."

    show live regret
    "That explains {i}a lot{/i}." 
    
    show live
    "So she was struggling with {u}understanding emotions{/u}. I doubt she'd understand what she's feeling, especially since she never possessed them before she turned human." 
    
    "If I'd wanted to help her, I'd have to think outside the box."
    menu:
            "Ask her about her interests.":
                pass

            "Ask her what kind of video games she likes.":
                pass
    l "Can you tell me what kind of games you've been playing?"

    r "How will that help?"

    l "The things we--{u}Humans{/u} do are often a result of something how we feel, even if we don't understand it."

    r "I don't get it, but I'll tell you. I've been playing multiplayer games lately although sometimes I make Mr. Plant Minions to play with me."

    "There it is. Now I {b}know{/b} why she's been more annoying than ever before."

    "Why her room is messy,"
     
    "...bothering me on a constant basis,"
     
    "breaking my rules..."
    
    "Every single thing she did was because of one reason." 

    show live regret
    "Me."
    
    "A sickening feeling assaults my ego. Guilt. I let it run its course for I deserve it." 

    "Then a realization hits me like a flash of lightning."
    
    show live smile
    l "So that's what Lady Kashmal was trying to tell me."

    r "Huh? Wha-{i}Umbf!{/i}"
    
    show revy fluster with dissolve
    "I pull the Alien Goddess into my chest and gently wrap my arms around her."

    r "Huh? Huh, huh, HUH?! What're you doing?"

    show live
    l "I'm sorry you're feeling lonely. It's my fault. I've been working hard to rebuild Venera City and build a life where you can live normally without stress, but my methods seem to be hurting you... And me too."

    show live smile
    l "You're doing {b}great{/b}, Revy." 
    
    l "We may have had a few close calls but you've generally kept yourself hidden and haven't hurt any bystanders." 
    
    l "And, the way you shuffled through those emotions and told me how you feel is a far cry from how you were when we first met." 
    
    l "Keep up the good work."

    show revy with dissolve
    "The Alien Goddess, who three years ago was a threat to humanity and the world, nuzzles herself deeper into my chest."

    show revy happy with dissolve
    r "Thank you, big brother."

    "We stay like this for a little while, letting the emotions run their course." 
    
    "It is strangely peaceful like this. I might've stayed longer but there are things I had to do."

    "So, I let her go."

    show live
    l "Now then, about {u}cleaning your room{/u}."

    show revy fluster with dissolve
    r "Wah! I thought I didn't have to do that because we made up and stuff?"

    show live annoy
    l "Where in the universe did you get that idea?"

    "I shake my head."

    show live
    l "{u}It doesn't matter{/u}. You need to take care of yourself and your room better, especially those plants of yours."

    "I direct my index finger at the politely sitting plant monster."

    show PM at left
    l "You {i}know{/i} your spawns are dangerous to humans. It may have listened to me but putting it before a normal person would place them in danger." 
    
    l "Not to mention the other heroes would know you're alive and that'd be the end of your life with me."

    show revy cry with dissolve
    r "B-But I don't wanna kill them. They're my {i}friends{/i}!"

    show live smile
    l "Who said we have to kill them?"

    show revy fluster
    r "Huh?"

    show live
    "I straighten myself, dusting whatever stains or clothes latched onto me."

    l "I'm going to clean out an old storage room. Then we'll move all your plant friends there until I can set up an artificial greenhouse." 
    
    show live annoy
    l "AFTER that, I'm going to teach you how to clean a room and watch you until you finish."

    "I thought she would cry and whine again but Revy instead gazes at me with wide, beady eyes."

    show revy with dissolve
    r "You'd do that for me?"

    show live smile
    l "Of course. It's my job as your older brother."

    "I cringe at the cheesy line but Revy's subtle smile dimmed those feelings."

    r "But what about breakfast?"

    "I follow her extended finger to the two piles of now soggy pancakes sitting atop the bedstand."

    show live
    l "{i}sigh{/i} I'll make us some new ones after we finish moving the plants. Once the clergy and other employees arrive it'll be harder to do so without being noticed." 
    
    l "Besides I have to tell them something when they arrive."

    r "What do you have to tell them?"

    show live smile
    l "I'm taking the day off to spend with my little sister."

    "I've finished all the ground work for the important tasks anyways and those bandits and monsters aren't stronger than the armed forces." 
    
    "I can let the workers handle the rest." 

    show live regret
    "Besides, it might be a bad idea to let Revy clean her room by herself. She might use her powers to make things easier and that could get out of hand."

    show revy happy with dissolve
    r "Yay!"

    show live
    "She cheers bearing a goofy childish grin. Her bubbly chirps ease the tremendous well of anxiety I've built up."

    show live smile
    l "Don't relax yet. Once we finish breakfast I'm going to work you until this room is spotless. No breaks."

    show revy fluster with dissolve
    r "You wouldn't. Y-You're not serious are you?"

    show live annoy
    l "Okay. So you want me to take away not just the internet but all your games too? I'm all right with that."

    show revy cry 
    r "NO! PLEASE DON'T. I'LL CLEAN!"

    l "Good girl."

    "{i}A few hours passed...{/i}"

    #Scene CG Live coaching Revy holding a vacuum cleaner cleaning her room, the latter flustered and crying.
    scene Revy Cleaning Her Room
    with dissolve
    stop music fadeout 0.2
    pause 0.5
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/beanfeast.mp3" fadein 0.2
    l "Hey, you missed a spot. No slacking!"

    #fluster
    r "But I don't know how to use this thing!"

    l "I told you how to use it five times now! Gently move it back and forth along the floor. I better not catch you using your powers either."

    r "Wahaaah! I don't wanna do this anymore. I wanna play games and eat candy!"

    "It took all morning and deep into the afternoon but I finally got the Alien Goddess to clean her room."

    "The other tasks I had to do were settled by the clergy and workers. Apparently, they were happy I was letting them do more work. I thought it would be the opposite but for once I'm glad to be wrong."

    "And so, another day with this little sister of mine comes to a close."

    #set ending to True to indicate this ending was completed
    $persistent.goodEnding = True
    "{b}Ending Acheived: Congrats! She Cleaned Her Room!{/b}"

    return
#__________________________________________________________________________________________________________
label badEnding:

    "I'll tell it straight to her face. Sometimes people just need to hear the truth."
    show live 
    l "Yeah. You were being annoying and hypocritical, but that's normal for kids."
    stop music fadeout 0.2
    r "{i}sniff{/i}"

    show live regret
    l "Hold on! That's not what I meant. Please let me finish--"
    play music "audio/BGM Pack 1 MP3/BGM Pack 1 MP3/dramatic_boi_v5.mp3" fadein 0.2
    show revy cry
    r "{i}UWAAAAAAAAHAAAAAH!!!{/i}"

    "Uh oh. I went too far."

    r "How could you be so mean to me?"

    "Tears pour like waterfalls. Now that I think about it, I did just insult her." 

    "That was a huge mistake!!"

    l "Revy. Please, forgive me. I went too far--"

    "I slowly approach her, holding my arms forward like signals to stop and wait while charged some magic."

    r "Big Brother... Live, I..."

    l "Revy, please calm down. I'm--"
    stop music
    show revy menace
    r "{B}I hate you{/B}."

    "Her frigid words and menacing aura oozing from her froze the room. Her eyes glowed cherry-red like they used to when we fought." 
    
    "Only this time all her rage is focused on me."

    "I rose, charging my super-speed spell."

    "{u}Too slow{/u}."

    show PM behind live 
    "A brutal piercing sensation rips through my chest. My eyes lay upon the massive tree root extended from behind me." 
    
    "Warm liquid expels from my mouth leaving an irony taste on my tongue." 
    
    "I force my head around and saw it was the monster Revy spawned earlier who pierced me from behind."

    "Then, everything fades to black."

    "{b}Achieved Ending: You Done Died{/b}"

    return

#_____________________________________________________________________________
#Begin alternate route
label routeB:

    "Maybe I should ask Kashmal for help?"

    "Even after three years I'm still not good at understanding Revy." 

    "Kashmal may never give straight advice but her wisdom has saved me more times than I could count. Besides, I have feeling she {i}wanted{/i} me to call her."

    l "I'll be right back, Revy. I need to make a quick call."

    #pout
    r "Hmph!"

    "The Alien Goddess huffed at me without removing her face from her game."

    "Why was she upset? Ugh, I'll save that question for later."

    #scene hallway
    scene hallway
    with fade

    "I left Revy's room and shut the door. I walked down the hall a bit, making sure Revy's room is in sight but far away enough that she couldn't hear." 

    l "Lady Kashmal! I need to speak with you please."

    "I gently called out to her, my voice hardly echoing down the hall. I {i}knew{/i} she was listening since she was aware of everything that went on this nation combined with her habit of randomly popping her screens out of nowhere."

    "..."

    "Dead silence."
    
    "Strange. She usually never hesitated to speak with me."

    "I clasped my hands in prayer and focused intently."

    l "Lady Kashmal. Please, I need your advice."

    "I waited a few minutes this time."

    "..."

    "Still no response, I see. Maybe she wanted me to say something specific?"

    "I held back bile as I forced embarassing cringe out my mouth."

    l "Oh great and mighty Kashmal. This humble one requests a meeting with a fair and beautiful goddess like yourself."

    "I felt a strange energy pulse through the walls. Now I {i}knew{/i} she was listening."

    "A sudden idea like a lightning flash lit up in my head. I fold myself at the waist, the cringe physically affecting my stomach." 
    
    #choice Say the thing vs Think a Little harder on it
    menu:
        "Say the thing":
            "I guess she {i}really{/i} wants me to call her that."
        "Think a little harder on it":
            "I weigh my options and decide it'll be better to humor her desires than return without a plan."

    "I swallow as much air as I can before forcing out those words that chipped at my pride."

    #annoy
    l "{i}Big sister{/i}, your younger brother needs some help."

    "As soon as I finish that painful sentence, a piece of the wall spins around on a horizontal hinge, a screen appearing on the other side."

    k "What can Big Sis' do for you, Live? Your earlier flattery was so nice I'm feeling a little generous today."

    "You teasing snake." 

    k"Dear me, that scowl of yours is no good. Why not speak your mind? As long as you mind your language you can express yourself as you do normally."

    "Well, now that she's give me permission I can be a little less cautious."

    l "You {i}know{/i} I don't like being teased."

    k "You are the only one I tease this way. Any of my followers would consider it an honor." 

    k "So, you need help with getting your sister to clean her room."

    "I can't get used to the fact that I have regular conversations with someone who knows everything about my life. The awkwardness never goes away."

    "At least it saves time explaining."

    #Regret
    l "Y-Yeah."

    k "I suppose it must be hard. You always listened to your father and later me. You were such a well-behaved boy that comprehending what a regular kid is like must be difficult."

    #annoy
    l "I feel like I'm being teased again."

    k "{b}You are{/b}."

    "She admits it!"

    k "However, it is for your qualities such as those that I chose you as my Hero. Therefore, I know you are capable of reforming Re-Venus as you set out to do."

    l "I appreciate the compliment."

    "Even though reforming Revy was {i}her{/i} idea, I did agree to it. I agree it's the best option for the world too."

    l "However, as much as it pains me to admit I can't understand what Revy wants."

    "I rake the hairs on the back of my head, stroking the area with my fingers."

    l "She asked me to make her double her usual portion and then ignored me when I came in." 

    l "If that wasn't confusing enough, she was upset when I left which tells me she was paying attention." 

    #annoy
    l "I can't take care of her if she doesn't tell me what's bothering her."

    k "{i}giggle{/i} Young women are mysterious aren't they? We always want something but can never simply say it. We want the other person to figure it out."

    "I let out a chuckle."

    k "What is so amusing?"

    "The slight frigidity in her tone sends a chill down my spine."

    #choice say it vs hold it in
    menu:
        "Hold it in":
            jump holdIt
        "Say what you found funny":
            jump sayIt
#_____________________________________________________________________________
label holdIt():
    #regret
    l "Never mind."

    "I shouldn't have found that funny."

    k "Go on. Speak up. I permit you to."

    l "I really don't--"

    k "{b}Do it{/b}"

    "I can feel my entire being shudder. Kashmal is terrifying when she wants to be."

    jump sayIt
#_____________________________________________________________________________
label sayIt():
    "Well, I don't have a choice."

    l "That you said {i}we{/i}."

    "Suddenly, dozens of holes opened in the floor, ceiling, and walls." 

    "Various glowing firearms and electric weapons pop out, their barrels inches from my face. The subtle whir of their energy charging and mana building rang in my ears." 

    "Each weapon was more advanced than anything on Venera's arms market. And this all happened faster than I could react." 

    k "How rude! You know that gods and goddesses have no age. Besides, you've seen my avatar. I don't look a day past 20 and haven't for millenia."

    k "I know you see me mostly eat sweets and junk food and never leave my lab but my body doesn't get fat either. We don't need the same nutirition as you--."

    #live regret
    l "Alright, I understand! I'm sorry. You are young and beautiful. Can we please put the weapons away?"

    "The weapons immediataely slipped back into their holes and the hallway returned to normal."

    k "Do not worry. I am not upset. I acted out to help explain to you her behaior."

    #live annoy
    l "Well, you certainly fooled me... But I'm afraid I don't follow."

    k "Do you see what I mean? Our minds think differently than each other's. However, children are often more sensitive and cannot take jokes like I can."

    "You could take a joke alright."

    k "My advice is to go back into her room and observe her behavior when you do things. Decipher the meaning behind her actions. She wants something from you, that much is clear."

    l "Ugh! Why is this so difficult?"

    k "I gave you the tools. I am confident you can figure it out. Oh! My experiment is done cooking. I must go." 

    k "And by the way, if you make fun of my age again, I {i}will{/i} kill you, hero or not."

    "With that, the panel flipped around and the wall was as whole as always."

    "I kneaded my face with my hands as groans of discomfort exited my mouth." 

    l "She may be a goddess, but she can be as cryptic as Revy sometimes. I don't understand women. At all."

    "Things won't improve if I sat around and did nothing. Revy will grow up irresponsible and spoiled which would put the world back where it was with an obnoxious tyrant with cataclysmic powers at our throats." 

    "That is if her plants don't overgrow and kill everyone first."

    "Still... Lady Kashmal's advice has always been helpful. She's cryptic, though. As all gods are. They view things on another plane--comprehending what they see is impossible for us. However, they always had us in mind, even when things like Revy happened."

    "Then again, if Revy was, in fact, an alien deity, it'd make sense why she might make them struggle."

    #Annoy
    l "..."

    "That didn't make Kashmal's advice any less annoying to decipher!"

    "Time is of the essence. I {i}need{/i} to make a choice."

    menu:
            "Follow Advice":
                # Proceed to Choice 3B
                jump choice3B
            "Try your own thing":
                # Proceed to Choice 2
                jump redirect
#_____________________________________________________________________________
label redirect():
    "I think I'll try my own thing. I'm too worried about those plants to decipher some riddles."

    "With that, I headed back to Revy's Room."

    scene RevysRoom
    with fade
    
    jump choice2
#_____________________________________________________________________________
label choice3B():

    "I'll try understanding what Revy wants. Like Lady Kashmal suggested."

    "I dove into my mind and recalled all my previous interactions with Revy, primarily since we began living together."

    "..."

    "Nothing but her whining about things in various forms come to my head in a blurred soup."

    #regret
    l "I'm not very competent at this."

    "A thought crossed my mind."

    l "Huh. Have I ever thought about things from other people's perspective?"

    k "You haven't."

    l "Ah!"

    "I force all my weight onto my feet and tense my muscles as tight as possible to not fall." 
    
    "Anger rises but seeing the screen that once again pop out of the wall, I calm myself before I made a bigger mistake."

    l "Please, stop scaring me like that."

    k "That time wasn't on purpose."

    "And the other times were?"

    k "More importantly, you should check Revy's room. {i}Now{/i}."

    "A sense of dread roots in my stomach. Legs pumping as fast I could, I ran back to her room. Opening the door, I saw a horrific sight."

    #scene change
    scene RevysRoom
    with fade

    p "..."

    "An elite plant monster... She made one."

    "The being, that looked like a a humanoid doll the size of a bear weaved together from roots and vines and a Venus Flytrap where its head should be, sat beside Revy."

    "That thing can take out an an elite armed guard single-handedly and are intelligent enough to perform covert operations."

    "And... It was playing {i}video games{/i} with her?!"

    "Without thinking, I stomp over to the perpetrator and rip the game system out of her hands."

    r "H-Hey! What are you doing?"

    "Her voice rings out with confusion and sadness. Her minion turns to me with its eyeless face and flexed its arm, sharp, barky claws enforced by thick woven vine-like muscle."

    l "You pipe down too!"

    "My shout made the monster relax and sit because it knew I could bite as hard. These things were nothing for me, especially one on one. Although it could still kill me without my armor, if I used my head it couldn't win."

    "Firstly, I use my phone to electronically shut the windows."

    l "Do you realize what you did?!"

    #Revy cry
    r "Give it back to me, now! I want it..."

    "She was too flustered. I had to calm her down."

    #Choice
    menu:
        "Continue following Kashmal's advice":
            jump choice4
        "Input your own ideas from what you know works":
            jump youThoughtEnd
#_____________________________________________________________________________
label youThoughtEnd():
    "Alright, I think I get it now. I don't need Kashmal's advice anymore."

    l "No. Not until I discipline you for--"

    #cry
    r "But I didn't do anything wrong!"

    #angry
    l "Don't interrupt me. You summoned an elite monster spawner that will overwhelm the city. And for what--"

    "I freeze in my spot as dozens of Plant Minions spawn from the wall. Monsters over eight feet tall appearing one after the other."

    #regret
    l "Why is it making more of those things? And why isn't it {i}stopping{/i}?"

    #fluster
    r "I-I dunno? It's acting on its own!"

    l "WELL GET IT TO STOP!"

    r "I CAN'T!"

    "The minions continue spawning faster and faster, quickly filling the room to bursting."

    "Naturally, everything inside the room is crushed between the filling of mindless plant monsters."

    "Myself included."

    "{b}Ending Acheived: You know, a room can only hold so many Plant Minions.{/b}"
    
    return
#_____________________________________________________________________________
label choice4():

    l "Urk..."

    "I almost forgot about what I discussed with Lady Kashmal!"

    "Alright. I need to focus on what she is trying to tell me."

    #Revy cry
    r "Give it back! Gimme back my game system!"

    "While I was thinking, Revy rose on all fours from her bed and reached for her console, swiping like a cat."

    "I easily backstep, evading the swing."

    #fluster
    r "Oop!"

    "She grunted as she fell onto the bed, having put too much force into the swing."

    "However, my victory was short lived as I realized I was about to bump into the now standing plant monster. He was using his body to block me off. "

    #happy
    r "I got you now!"

    "She flashes a smug look on her face. The Alien Goddess curls back, attempting to lunge forward."

    l "Nope."

    #Choice Surprise her vs Go on the offensive
    menu: 
        "Dodge":
            "I pivot around the attack and leap at the Alien Goddess from an angle."
        "Run at her":
            "Instead, I run towards her."
    r "Huh?"

    "My action bewilders Revt, stunning her and her minion in confusion."

    "I place my palm on her back and forced Revy deeper into the mattress, softly imprinting her impression onto the squishy furniture."

    l "Yeah. I'm not having you accidentally fly though the wall again. Building repairs aren't cheap, especially with all the reconstruction."

    "Those walls were steel too. Several inches in fact. I have no idea how she did it with that tiny body of hers."

    "The roar of defeated mumbles and wines growl from beneath the mass topped with hair-like leaves. She wildly wave her arms and legs gently beating the soft sheets."

    "I let go."

    r "Pah!"

    "She shot up like a whale leaping from the water, sucking in all the air she could. Her eyes widen like a fish as her head sweeps side-to-side like scanning for something."

    r "Give it back!"

    "Another swipe."

    "I back away, her fingers clawing the air where I just was."
    
    r "{i}Grrr{/i}... Give it to me!"

    "She swipes again, leaning forward while she does."

    "Was she trying to tell me she wants to be a cat?"

    "Regardless, another easy backstep."

    #fluster
    r "Just give it back already!"

    l "No. Just sit down and--"

    "But Revy kept trying to snatch the device out of my hands. This time vegetation-like appendages grew from her arms to extend her reach." 
    
    "However, she was dealing with the fastest of the Heroes. Dodging was easy."

    "However, the dog-teaming with her plant-minion made things annoying. "

    #happy
    r "Hahaha! You're no match for our tag-team combo attack."

    p "..."

    "She's been playing too many {i}games{/i} lately."

    "Games..."

    #Choice Continue playing with Revy or Call it off
    menu:
        "Continue Playing":
            jump playTime
        "Call it off":
            jump slamEnd
#_____________________________________________________________________________
label slamEnd():
    "You know, I think I should stop this before it gets out of hand."

    l "You know, Revy. We should stop this--WOAH!"

    "I duck, avoding her swing that would have taken my head off."

    #angry
    l "Wait! I told you to calm down!"

    #happy
    r "Yay! Play time."

    "She's in her own little world!"

    r "Get him, Plant Friend!"

    p "!"

    "The Plant Minion tries to swipe at me from behind."

    "I barely dodge in time."

    r "Hah! I got you now."

    "While shifting to avoid the last attack, I find myself staring down Revy's massive tree trunk hammer limb to big and close to dodge!"

    "{i}Doesn't she realize how excessive that is?{/i}"

    r "Taaake this!"
    
    "I could only yell in pain as the oversized limb bludgeons my body to pieces, and my consciousness along with it."

    "{b}Ending Acheived: Playtime's Done when She Says it's Done!"

    return
#______________________________________________________________________________
label playTime():
    "Duck. Pivot. Jump the sweep. Redirect the swipe. Pat down the vine swipe."

    "With ease I parried and dodged Revy and the Plant Minion's tag team combo, the game system kept safe. Their moves grew faster, so my moves did too. I could end this now but I was asking myself a question."

    "Why?"

    "Revy's stronger than me, as painful as I admit it. If she wanted to, retrieving the game system would be easy for her. Just pin me down and and take it that way."

    "But she wasn't."

    "And even more confusingly, she was smiling."

    "I continued bobbing and weaving, swimming between the now speedy flurry of swipes on both sides. It was almost as chaotic as my thoughts, diving deep to discover the answer."

    "If I let this go on longer she may start breaking the place. But she doesn't care! Was this all a game to her?"

    "A game?"

    "A burst of electric wisdom flashed in my head. My eyes shoot open from the epiphany."

    "In that moment my focus shatters, one of the Plant Minion's swings grazes with my cheek."

    "The force behind it intense, I lurch, flying off my feet."

    r "Brother!"

    "The dazed feeling didn't last long. Curling myself, I used the momentum to flip and land onto my hand, then spring off of it and onto my feet. The pain throbbed still, but it wasn't enough to deter me. It seemed the creature was holding back."

    "And I didn't drop the game system."

    "Revy shreiekd and curled herself up into a ball. She's obviously afraid"

    l "I-It's fine. How about, we make a deal. If you can steal the game system back from me in five minutes without your powers I'll let you off the hook. If you lose, you have to clean your room."

    #pout
    r "Hmmm!"

    #regret
    l "!"

    #pout
    r "Ice cream. I want ice cream."

    "Where did that come from? Ice cream in the morning? And what made her think she was in a position to bargain?"

    "But, she may at least clean her room now."

    l "Fine! If you win, I'll take you out for ice cream later. But again, no powers or I won't return this."

    "I wave the console as I said that."

    "I know I said no powers earlier, but I need to be sure."

    r "Okay! But you can't use your powers either."

    "She seems oddly happy about the fact I threatened her. I thought she'd be mad or at least stressed. "

    l "... Fine. I promise."

    r "Okay! Here I cooome!"

    "Revy and I played keepaway like that for a while. "

    "The challenge was a pleasant surprise. Revy carried over her combat instincts into her human form and despite not fighting for years now she was hardly rusty. Her tactical prowess as a leader of a hive-mind like colony also peetered through the scuffle."

    "I struggled without my powers. I know that's strange since I have a significant height advantage over the Alien Goddess right now, but remember, I'm also dealing with her Plant Minion. It's 2 versus 1. Not my kind of odds."

    "But I wouldn't be a hero if something like that discouraged me."
    

    "It took all my focus to stay in it. The lack of sleep made things difficult too."

    "Barring a couple close calls, Revy couldn't even hope to get the console from me even with help."

    "As the contest went on, I even started to have a little fun."

    "But time flies when you have fun. "

    "{i}RING RING{/i}"

    "My cellphone buzzed to life. "

    "I checked the Caller ID and the time."

    l "Oh no! The construction materials meeting!"

    "I lost track of time playing with Revy. Now I'm late."

    #pout
    r "HMMMMMMMMMMM!"

    "That was the loudest pout I ever heard her do. "

    "I checked the time again. {u}Two hours{/u} had passed. Alright, so I don't have to be the kind of jerk that goes back on his word."

    l "I gave you double the time limit to get the console from me. Now I have to get to work. Don't worry I'm not mad."

    "Revy pouts harder as I ponder what her deal was. I already played a game with her."

    #pout
    r "{i}Fine{/i}. I'll do it I'll clean my room."

    "She sounds like she's forcing her anger back down her throat. I am a little concerned but she appears calm."

    "Still, even though work is important is it the best idea to leave her to her own devices right now?"

    menu:
        "Let her clean her room by herself":
            # City End
            jump city_end
        "Help her":
            # Proceed to Ice Cream End
            jump routeBEnd           
#______________________________________________________________________________
label city_end():

    "Sorry, Revy. Work comes first."

    l "I have to go, but I'll be back to check on you when I'm done. And you better hold up your end of the bargain."

    #cry
    r "B-But I've never cleaned my own room before like this!"

    l "I'll have a bot come help and bring you supplies as needed."

    "I am rushing things but it's justified. This meeting is important for continuing repairs to the city. Repairs necessitated by her! Someone {b}has{/b} to be there to manage it all."

    r "But I don't wanna do it alone!"

    l "Sorry. I'll be back later."

    "With that, I left to the meeting."

    scene LiveOffice
    with fade

    "Things went fine at first."

    "Then, about an hour into the meeting, it became bad. Really bad."

    "No, the meeting was good." 

    "It were the {b}screams{/b} outside."

    "And the Plant Minions outside the window."

    p "!"

    "{i}Oh gods{/i}, there was a lot of them." 

    "And they were all coming from..."

    "With super speed I fly on my legs back to Revy's room and burst open the door."

    scene RevysRoom
    with fade

    #angry
    l "REVY!! What the..."

    #regret
    l "Urk..."

    p "..."

    "Instead of a half-decently clean room, or at least all the trash and laundry picked up, the entire space had transformed into a {i}Plant Minion Factory{/i}, birthing several of those things a minute!"

    r "Big brother!"

    "The green-haired perpetrator calls out amidst her bed, extreme guilt on her flushed face."

    #anger
    l "WHAT IN THE PITS OF PURGATORY DID YOU DO?!!!"

    #cry
    r "WAH! I'm sorry. I got stressed and didn't know what to do so I made a bunch of friends to help."

    #fluster
    r "B-But the first one didn't know anything. And the other, and then before I knew it I had too many to fit in the room!"

    l "THE CITY IS GOING TO BE DESTROYED, YOU IDIOT!!!"

    r "But... heehee... Now we have a bunch of servants to work at home, right?"

    "AIIIIIGH!!!"

    "CRASH!!!!"

    "CRUMBLE!!!!"

    "MY NEW CAAAAAAAR!!!"

    #regret
    l "Too... Late..."

    "Yeah. The city's in flames and people are dying in the streets, ripped apart by rapidly-multiplying plant monsters." 

    "Even if Revy calls them back now the damage was done."

    "Just. Great."

    "{b}Ending Acheived: Home for an Army of Servants?{/b}"

    return
#______________________________________________________________________________
#Ice Cream End
label routeBEnd():
    
    "You know, as important as the meeting is, reforming the walking apocalypse button in front of me should be priority."

    "I thumb the call button and press the device to my ear."

    l "Yeah. Sorry, but can you handle it without me? I'm not available. Ask my secretary to fill everything out. They'll forward any issues to me. Got it? Goodbye."

    "I hang up as the confused, angry voice of the contractor on the other end squeeked."

    r "..."

    "Her vapid eyes stare at me all confused. "

    l "Change of plans, I'm taking the day off today. We're cleaning your room."

    "The Alien Goddess slowly beams but the corners of her lips quickly dip into a sheepish frown."

    r "It's fine. Go and work. I can... figure it out on my own."

    "She was being oddly reasonale for once. However..."

    l "Sorry. I made up my mind. This place is a mess and I can't have you potentially birthing an army of your friends by accident and wrecking the city."

    r "Please don't get rid of him or my plants! I don't wanna be alone."

    "{i}Alone{/i}, huh?"

    "At that moment, I realize what Revy was after this whole time. The games. The Plant Minion. Her being upset when I left. {i}She wanted to spend time with me!{/i}"

    l "..."

    "For an older brother, and her guardian, I was rarely around. Now that I thought about it, I could qualify as an absentee parent!"

    "The realization send a sickening sensation slithering through my body. So this is what it's like to be self-humbled."

    l "What if we built an indoor garden for them?"

    r "!"

    l "If I clear out some storage I could remodel a few ones. I've been looking for an excuse to empty those places anyways."

    "I pinch the bridge of my nose and sighed. With my super speed it shouldn't be hard for me to get all the plants into the rooms without being noticed. Naturally, I control all the security systems too. Good grief, this was going to be a pain."

    "But, it may be worth it in the end."

    #pout
    r "I still don't wanna clean my room. It's hard."

    l "That's why I'm helping you. This place is such a mess I am sure most cleaning services would refuse even without the monster spawning plants."

    #Revy Cry
    r "!"

    "Oh no. She was about to cry. Did I accidentally insult her? Or was she about to throw a tantrum? Either option was less than desirable."

    l "How about this, if we can finish most of the work cleaning your room by noon I'll get us some ice cream. Does that sound good?"

    #Happy
    r "Yay!"

    "{i}GLOMP!{/i}"

    l "Oof!"

    "Her soaring tackle collides with my stomach. The blow knocks me off my feet and sent me into the wall, cracking but not breaking it. I'm lucky I'm still in one piece."

    r "You're the best, Big Brother!"

    #Live smile
    l "You're welcome."

    "I'll ignore the damaged wall for now and fix it later."

    #{b}Ending CG of Live and Revy enjoying ice cream{/b}
    scene Live and Revy getting ice cream
    with fade

    "Hours later we finish cleaning, so as promised we go out to get some food, and then, ice cream."

    #r Happy
    r "Human food is awesome! I could never eat this stuff as I used to be."

    "The Alien Goddess beams, kicking her legs like a little kid beneath her seat as she peppers the frozen desert with licks. She's very happy with all those extra scoops."

    "I sip my milkshake and remark,"

    l "It was all soil and occasionally sucking the nutrients out of things, right?"

    r "Anything foolish enough to approach, duh. But as the queen I always had offerings. But--"

    "I made us disguises so people wouldn't bother us. I was heavily against going outside to eat but Revy begged and begged. She may have laced in a few world-ending threats amidst her tantrum too."

    "Still, she seemed generally happy right now. "

    "Sitting together with her, eating our ice cream while basking in the afternoon sun, not worry about work or play. It was surprisingly pleasant."

    #Revy fluster
    r "Aaaah! My head hurts."

    #annoy
    l "How many times do I have to tell you to slow down or you'll get brain freeze!"

    #cry
    r "BUT IT'S SO GOOD!"

    #l smile
    l "Hehe. Just follow my instructions."

    "Sitting here, doing mundane things in a crazy world."

    "It was nice."

    #Set routeB end to True to indicate completion
    $persistent.routeBEnd = True
    "Achieved Ending {b}Alien Plants Love Ice Cream, Apparently.{/b}"

    return
#______________________________________________________________________________
#Secret Ending obtained when both good endings are found
label secret_epilogue():

    #Revy's room but clean. 
    #Maybe have a 2 layered CG where the dirty stuff is overlaid atop the clean room to save money
    scene RevysRoom

    #happy
    r "I got you this time!"

    #l smile
    l "Think again."

    "Revy and I pound the controllers from atop our cushions as the sun slowly sliddx behind the tall buildings. The characters we controlled move vigourously on the wide screen before us, puppetted by the intense competition between their controllers. "

    "We're the only things on the floor. Everything is as spotless and clean as if it were the day she moved in."

    #Choice 
    menu: 
        "Beat Revy":
            l "And that makes 10-8 in our set. I win."
        "Destroy Revy":
            l "And that makes 10-2 in our set."

    r "Damn it!"

    "The Alien Goddess throws her controller on the floor in rage as the sound of my character's victory blasted from the stereo. I dove to grab it, rolling over my shoulder from the momentum. "

    l "Language. And be careful with this."

    "She accepts the controller with a pout."

    #pout
    r "Sorry. I mean, how are you so good? All you do is work."

    #annoy
    l "A long time ago, I played games a lot too."

    "Revy looks at me with surprise."

    l "Do you take me for a ridiculous workaholic who has no life outside of it?"

    r "Duh!"

    "Well, I walked into that one..."

    "While on the subject of work, I thought to check on everything's progress."

    "Pulling up my phone, I notice the messages from all the people I delegated the tasks too."

    #regret
    l "..."

    r "What's wrong, brother?"

    l "No... it's not... Well, actually everything went great with work. It's just..."

    r "It's just what?"

    l "The progress without me exceeded what I would have gotten done if I was there."

    "The contractor agreed to do more for what we were offering, the army cleared out the bases and nests of most of the bandits and monsters, etc. We even have a completed version of our contribution for the festival. Every task I was worried about was not only done, but accomplished with 110/% quality!"

    #happy
    r "BWAHAHA! What a loser-pants."

    "I didn't know whether to be glad Revy isn't crying due to whining or mad that she's bellowing laughter while pointing her tiny finger at me."

    p "..."

    "That things seems to find it amusing too!"

    #anger
    l "Stop that."

    "But she kept laughing."

    "If she were anyone other than Lady Kashmal then I'd tear into her. However, this is such a rare moment that I'll let it slide."

    r "HAHAHA! The workaholic boss gets less done than the employees he hired to do the job."

    "And now she was rolling on the floor. "
    
    p  "..."

    "And that thing was still in the background."

    "Still, I never thought I'd see the Alien Goddess roll on the floor laughing her heart out like this. The juxtaposition was bizarre."

    #Flashback begins. Ideally, Live wuld be in his hero outfit for sprites.
    #
    scene Cave
    with dissolve

    "{i}Three years ago...{/i}"

    "I stood outside the cave where I knew Re-Venus was, panting and clutching my magic bow. A storm raged around me and the remains of alien plants sprawled around me. I was losing blood, but I came this far. She was hiding in here after our last battle."

    l "Finally...."

    "The other heroes debated giving up. Indeed this was a desperate move and likely wasn't going to work. However, in a hopeless scenario any potential is better than none."

    "I have one shot at this. A new weapon Lady Kashmal designed. Re-Venus was weakened and had nowhere to run so it might work. It {b}had{/b} to."

    "An electric sensation ran through my nerves. "

    l "More of them are coming... Blast."

    "It seemed more of her endless army tripped the barrier I set up. I still had time but had to hurry."

    l "I'm coming for you, you monster."

    "Remembering all the people she killed, the destruction she caused, it gave me all the fuel I needed to push my aching body into the dark cavern."

    "The sounds of booming thunder and pounding rain dulled as I trekked deeper into the hole, careful to mask my movements. She must have been desperate to hide in a place without light as a plant. Maybe she didn't like the storm."

    "The perfect background to the Hero of Lightning."

    "As all light but the magic from my bow and armor disappeared, a new light source appeared. Several alien plants glowed softly along the walls. I used my speed to tiptoe around the vines like a super-gymnast who did parkour. A bit ingelegant of a comparison but that was the best way I could phrase it."

    "Soon enough, I arrived at what appeared to be a gigantic hollowed out space within the cave. In the center was the massive, hulking form of the Alien Goddess herself. Re-Venus lay in her gigantic, grotesque form with a gigantic Venus Flytrap-like maw and many vines that extended like tendrils. It was dark, but I could easily make out how she looked. "

    "Something was strange about her though. I have seen this form of hers many times but I never got a better look at her appearance from this close. The main core of her body heaved like an animal that breathed and there were some strange moans coming from her head area. "

    "The sounds of movement stirred. Some Plant Minions emerged from the walls."

    "Now's the time to move."

    "Charging my leg with a kick, I spin around, whipping my electric-charged roundhouse and tearing through the monsters. Their charred bodies fell in two."

    "The monstrous Alien Goddess's eyes opened, beaming their intense redness at me. They seemed confused and angry."

    "But they wouldn't be for long."

    "Before she could react, I loaded the special weapon, a strange arrow, into my bow and lept into the air. Her giant extended at the same time, shooting to me like rockets. "

    "One bludgeoned my side, sending me sprialing into the wall. The pain of the impact was excruticating. I grit my teeth and funneled my magic to keep myself together. "

    "But I had already fired my shot."

    "The arrow pierced the air and penetrated the goddess's eye."

    "{i}WAAAAAAAAAAAAAAAAAAA{/i}!"

    "As I rose shakingly from where I landed I smiled as the enemy of humanity let out a pained wail."

    "It was too soon to celebrate, but I wouldn't deny the satisfaction of that hit felt sweeter than anything I ever had."

    "But then something strange happened."

    "Re-Venus glowed bright, strange dark energy leaking out of her. Then her form shrank, like that stuff oozing out of was the air in a balloon."

    "She grew smaller with every second and her form morphed before my eyes. Her pained wails changed as well. At first they were nearly ineligible. But slowly, they became something I could recognize."

    "Something more human."

    "Shock and surprise froze me in my tracks. Ironic as it may have seemed for me, I'm certain anyone would have agreed it was warranted."

    "Finally, the dark mist cleared. Re-Venus, or what I thought of her, was gone. Instead, what laid before me was something I never expected."

    #CG of Hero Live meting kid Revy
    scene Revystransformation

    r "..."

    "A {b}kid{/b}."

    "A human kid."

    "Sure, she was a lot larger than a toddler, her body seemed around the same age as a teenager. Fitting as she spent many years traversing space. Her plant heritage carried over as well with her hair looking like a Venus Flytrap and a couple vines wrapped around her skin."

    "But the way she looked was unmistakably human."

    "Revy cry" "!"

    "She curled herself up into a ball, her face drenched in fear."

    "{i}Terror{/i}. She was afraid of me."

    "She is smaller and not fighting back. Maybe I could beat her right now. I could save the world."

    #annoy
    l "..."

    "I let the arm holding my bow fall to my side."

    "I thought I'd stay shocked but another emotion overpowers that feeling. "

    r "W-Wait!"

    l "Hm?"

    r "Aren't you gonna kill me?"

    #Choice "Yes" vs "No"
    menu:
        "Say what I intend":
            "No."
        "Say what I want to":
            "I do, but I won't."

    "I want to kill her, avenge those who died. But that mysterious feeling welled up to the point it rose up my throat making me spit out my next words."

    #annoy
    l "I refuse to take the life of an ignorant child."

    "That's what she was. The true form of the monstrous threat to humanity. A child."

    "A being who was innocent; doing bad things not out of malice but because they didn't know any better." 

    "Even after all the things they did, I could not take the life of someone like that. That is not the kind of person I am."

    #Flashback ends
    #return to Revys room
    scene RevysRoom
    with dissolve

    "And now, here she is rolling on the floor with a big goofy smile."

    r "Bwahaha! It's so funny."

    #annoy
    l "How long are you going to do this for?"

    "It went on for another five minutes before her eyes began to close."

    l "Time for bed, I see?"

    "That makes sense. We did do a lot of work today. It wasn't much for me but this was more than anything in her human body."

    r "Okaaay. Carry me to bed, please. Like a princess."

    "She unfolds her arms towards me while laying on her side."

    #l annoy
    l "Do I look like your butler to you?"

    #pout
    r "Hmmmmmm."

    #annoy
    l "{i}sigh{/i}"

    l "Only if you ask politely."

    r "Please carry me to my bed like a princess."

    "I scoop up the the Alien Goddess and carry her gently to her bed. Peeling back the covers, I lay her down and tucked her in."


    l "Sleep well--Wah?"

    "Two vines ensnare my frame, yanking me off my feet and pulling me into the bed next to Revy."

    r "Got you... heehee!"

    "She entangles her thin arms around me and nuzzles herself deep into my side. Her face bears a smug, satisfied expression as she closes her eyes and her breathing slowed." 
    
    p "..."

    "The Plant Minion sits politely in front of the door."

    "I guess I'm not sleeping in {i}my{/i} bed tonight."

    r "Good night, Big Brother."

    #smile
    l "Sleep well. Good night Revy."

    "After a few minutes, the only sound coming from the normally loud kid was a soft beat of gentle breaths."

    "At that time, Kashmal's screen extends from the wall over my face like a canopy."

    k "Awe, aren't you two adorable?"

    "It took her longer than I thought to come tease me."

    k "You can speak. Little Revy's a deep sleeper."

    "I reply quietly,"

    l "Are you fond of her as well?"

    k  "I would say I like you both for different reasons. But yes, I adore her."

    l "I still remember when you appeared after the battle and told me to bring her back home."

    k "And you had the most {i}adroable{/i}, awkward period between deciding on refusal to approval."

    #annoy
    l "Well, what you asked was absurd but ultimately was the best call."

    "The storm that distracted the monsters was her doing, naturally. But taking the enemy's weakened leader hostage was a solid option, especially since I didn't know that I still lacked the poer to kill her at the time."

    "Somehow, Revy was compliant and clung to my side as we traveled."

    "The weather was like a protective shroud on the way home. When I got there, Kashmal took Revy aside."

    "When she called for me again, Revy was suddenly acting affectionate towards me."

    k "She demanded you be her big brother so fervently I simply {b}had {/b}to accept."

    l "I still don't know why she asked me to be her {i}brother{/i}. Why not her father? That's basically my role in her life anyways."

    k "That may have had to do with what influenced her to ask for that relationship."

    "Lady Kashmal's screen flashes and that same cheesy show from earlier played on her screen."

    "Now that I got a good look at it, it was about..." 
    
    #Choice Caring or Serving
    menu: 
        "A sibling drama?":
            l "{b}An older brother caring for his little sister{/b}?"
        "A family show?":
            l "{b}A brother and sister scene from a family comedy show?{/b}"
    
    "The screen cuts back to Kashmal's usual pulse lines."

    k "It's one of my favorite shows. I'm so glad Little Revy also enjoys it."

    "At that moment, everything clicks into place. The satsifaction of finally understanding washes over me like a gentle breeze."

    l "So, Revy turning into this was your plan all along."

    "An electronic giggle resounds across the room."

    "What a devious goddess."

    "Suddenly, a wave of tiredness floods me. With no hand to cover my mouth, I couldn't stifle the coming {i}yawn{/i}"

    k "It appears you are ready to retire for the evening."

    "Revy snuggles deeper into my chest."

    r "Heehee! Brother... I love you."

    k "Oh my me! Such an adorable sleeptalker."

    "You know, spending time with Revy like this was a lot different than I tought."

    "{i}It wasn't bad hanging out with my little sister.{/i}"

    "END"

    "{b}Acheived Ending: A Good Night's Rest{/b}"

    return





