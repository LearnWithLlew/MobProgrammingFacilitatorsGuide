# Mob Programming Facilitors Guide
By [@LlewellynFalco](https://twitter.com/llewellynfalco)


This is a short guide to facilitating your 1st Mob Programming session with your team. 

## Picking the problem  
You should start with an easy problem. The goal should be to do something simple and have fun learning to mob. 
It could be part of your normal work, or it could be a sample exercise. 
If you want a sample exercise, [The FizzBuzz kata]() is a rather good starting point.

Either way, you want to have the computer your are going to code on  setup before you start the mob as installing and setup is not very fun.


**Test** : How do you know if the problem is easy enough? Ask your developers if they believe they can solve this problem alone in under an hour.

**Antipattern** : Let's do something no one on the team has ever done before... 


* [ ] I have a easy problem selected and a computer ready to go.

## Picking a time

A good starting time is between 90-120 minutes. Try not to do this durning lunch if possible.
Also, Don't overrun by missing lunch or staying late. 

``` The primary goal is to have fun and have people want to Mob again tomorrow.```

* [ ] I have a time on everyones calendar

  
## Setting up the Space

![Mob Programming Setup](images/MobProgrammingSetup.png)

The default configuration of most rooms is not suitable for mobbing. 
As a facilitator it is your job to rearrange the room to the best of your ability.
Tips:
 * Try to remove any distractions
 * Make it easy to move around the space
 * Have everyone facing the same direction, ideally looking at the same screen.
 * Bring a external mouse (external keyboard is a plus)
 * Have a whiteboard or simular place they can write.
 * While darkmode is great for solo programming, White backgrounds are easier to see on a projector or tv.
 
 
 * [ ] The space is setup
   * [ ] The Font is big enough that everyone can read it from everywhere
   * [ ] The screen is easy to see
   * [ ] It is easy to move around
   * [ ] I have set a timer to leave space for the retrospective at the end   
    (30 minutes for the 1st time, 10-15 minutes thereafter)
   
 
## 1st Rotation

The 1st rotation is where the most things can go wrong. 
You will want to lead this one stronger than the rest. 
As soon as possible, though, loosen up and let the mob take over.

### State the Rules

#### Working agreements

We agree to 
 * Treat each other with 
   * Kindness
   * Consideration
   * & Respect
 * No phones or laptops during the mob
 * yes, and...
 
 It is worth writing these down so everyone can see and refer back to them during the mob.
 
 The `yes, and...` rule refers to building on whatever came before you. It means you can't delete and start over when it is your turn. 
  
#### The Driver

``` No thinking at the keyboard ```

The person at the keyboard is called `The Driver`. They are only typing. It is ok for them to ask question, but no decisions should be made by them.

Tip: If the driver starts doing things on their own, just repeat the `No Thinking at the keyboard` rule out load.

* [ ] The driver is listening and following the navigator

#### The Navigator
  Speak in this order:
 ```
  Intention    "Please create a variable called count"
  Location     "Line 27 and a half (a new line between #27 & #28)"
  Details      "Type v,a,r space count equals 1"
 ```
This is where all the thinking should occur. 
Make sure to make space for the navigator to try to talk (This mean silencing the mob), 
it takes some practice to get right.

The intention of the navigator should be clear. 
This often means writing an example on the white board,
an english comment in the code, or a check list in notepad

Always check that the navigator is doing something and that they moving us toward action.
If they are stuck prod them with questions. If they are discussing, force a **small** decision (we can revisit it later.)

#### The Mob

In The beginning the rest of the mob is going to practice listening while being quiet. This is quite hard and will take some practice. If the navigator is stuck, they can ask the mob, but they must repeat anything they want to happen to the driver:

Example:  
*Navigator*:  What should we do?  
*Mobber 1*: I think we should try debugging.  
*Mobber 2*: Yes I agree  
*Navigator*: Driver, can you start the debugger.   


* [ ] Your phone has a 2-4 minute timer with a sound when done.
* [ ] The Team has made some (small) progress
* [ ] Everyone is talking and listening

Tips: If you have 2 people that are scared or new to the domain seperate them so they aren't the driver/navigator pair.


## Rotations

Congratulations, you have gotten everyone to the keyboard at least once, now we can start the working on improving the flow.

At this point you should endeavor to talk only in questions. 
Keep an idea out for 

* Small victories to celebrate
* People not listening
* Not rotating / slow rotations
* Confusion in the new navigator
* New ways of using the tooling
* Long periods between running or checking in  the code
* Misunderstandings
* Skipping Intention and moving straight to details. 

As facilitator you are here to help us learn and enjoy. If people are confused slow them down and make space to regain understanding. If someone in the group has that, make space for them to teach the rest of us. If we are stuck call it out and get us moving again. If we are not treating each other well, call that out as well.


## Common Problems

### Vocabulary
 Person doesn't know how to describe something on the screen. Maybe really wants to grab the keyboard/mouse   
 Phrase: `use your words`  
 Exercise: [Strong Style Vocab](http://github.com/learnwithllew)

### I don't know what to do...
 Person isn't sure what to do, and won't try anything.  
 Action: Pick something, anything  
 Phrase: `Failure helps us learn what success looks like`
 Tips:  
  * Try smaller numbers. Don't try 4 if you haven't yet tried 1
  * Guess. `3 should give llama right?`
  * Multiple Ideas? try all of them then vote.
  
### Let me discuss
 An other form of inaction is talking about the possible solutions.
 Make the navigator move, then they can explain why later (if people are still confused). Don't let this turn into a meeting.
 
 There are 2 reason I commonly see for this. The first is the navigator is scared of being wrong, or only knows a bit of what to do.
 
 Phrase: `It's in the doing of the work that we discover the work we have to do - @WoodyZuill`

 The second is there are many choices. (see above)
 
### That idea sucks
 Sometimes the someone (the driver / navigator / or mobber ) doesn't like a certain idea we are doing. That's ok, but it is not ok to not do it. Do it first then do the other way. Then vote.
 Even if one of the ways is "Let's not do anything". Try that (it's quick), then try the idea. Then vote.
 
 Part of what we are learning is it's ok to make mistakes and do dumb things. This is a cornerstone of philological safety.
 

## Retro

### Videos (1st time only)

[You'll miss obvious things]()  
[You'll mishear things]()  
[This is confusing]()  

[How to use sticky notes]()  
[Online MindMap](http://mindmup.com)  

### Smaller focus for better seeing
Go through each of the following areas for observations. What did you see new in:
* Tooling
* Language 
* Product Domain
* Process
* The Team
* Emotions felt (Need the emotion + the triggering event)

#### Emotions

Emotions are often something not brought to work. But they are powerful indicators that something is **important**. Our job is to engage our analytical mind and find out what.

[Language of emotions]()  

| Emotion | Meaning | Explore |
|---------|---------|---------|
| Happy | a surprizing good thing happened | What was it, how to reproduce it |
| Angry| something important was threatened | What is important, why is it vunerable? Was it really in danger? |
| Sad | something important isn't helping us any more | What was important, why has it changed, how can we let go |
| Fear | Stay alive! | What was the danger? How did we escape? How can we avoid it in the future? |
| Anxious | Stop procrastinating, trouble is coming | What was the trouble, why is it troubling. How can we take action  |
| Bordom | My energy can be better used | What is boring? Can this be removed or automated? Is it actually unimportant? |
| Confusion | Focus, somethings wrong | What am I confused about? Do I need to understand this completely. Can this be simpler |



### Steps
1) Collect Observations
1) Read and group Observations

## More Information

[Download the full guidebook](http://mobprogrammingguidebook.com)
[This guide at](http://github.com/learnwithllew/)

