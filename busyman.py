import os,sys,random,subprocess
suffix = 'busyman'
repos = ['busycommit']

messages = ["There will be a happy romance for you shortly.",
"Your fondest dream will come true within this year.",
"You have a deep interest in all that is artistic.",
"Your emotional nature is strong and sensitive.",
"A letter of great importance may reach you any day now.",
"Good health will be yours for a long time.",
"You will become better acquainted with a coworker.",
"To be old and wise, you must first be young and stupid.",
"Failure is only the opportunity to begin again more intelligently.",
"Integrity is doing the right thing, even if nobody is watching.",
"Conquer your fears or they will conquer you.",
"You are a lover of words; One day you will write a book.",
"In this life it is not what we take up, but what we give up, that makes us rich.",
"Fear can keep us up all night long, but faith makes one fine pillow.",
"Seek out the significance of your problem at this time. Try to understand.",
"Never upset the driver of the car you're in; they're the master of your destiny until you get home.",
"He who slithers among the ground is not always a foe.",
"You learn from your mistakes, you will learn a lot today.",
"You only need look to your own reflection for inspiration. Because you are Beautiful!",
"You are not judged by your efforts you put in; you are judged on your performance.",
"Rivers need springs.",
"Good news from afar may bring you a welcome visitor.",
"When all else seems to fail, smile for today and just love someone.",
"Patience is a virtue, unless its against a brick wall.",
"When you look down, all you see is dirt, so keep looking up.",
"If you are afraid to shake the dice, you will never throw a six.",
"Even if the person who appears most wrong, is also quite often right.",
"A single conversation with a wise man is better than ten years of study.",
"Happiness is often a rebound from hard work. (1 comment)",
"The world may be your oyster, but that doesn't mean you'll get it's pearl.",
"Your life will be filled with magical moments.",
"You're true love will show himself to you under the moonlight. (1 comment)",
"Do not follow where the path may lead. Go where there is no path...and leave a trail",
"Do not fear what you don't know",
"The object of your desire comes closer.",
"You have a flair for adding a fanciful dimension to any story.",
"If you wish to know the mind of a man, listen to his words",
"The most useless energy is trying to change what and who God so carefully created.",
"Do not be covered in sadness or be fooled in happiness they both must exist",
"You will have unexpected great good luck.",
"You will have a pleasant surprise",
"All progress occurs because people dare to be different.",
"Your ability for accomplishment will be followed by success.",
"The world is always ready to receive talent with open arms.",
"Things may come to those who wait, but only the things left by those who hustle.",
"We can't help everyone. But everyone can help someone.",
"Every day is a new day. But tomorrow is never promised.",
"Express yourself: Don't hold back!",
"It is not necessary to show others you have change; the change will be obvious.",
"You have a deep appreciation of the arts and music."]


message = random.choice(messages)
repo = random.choice(repos)
dir = 'C:\\Users\\Vasia\\Documents\\PycharmProjects\\' + repo + '\\'


filename = dir + ''.join([random.choice('p22am1zln3xkwqs6edor59091itu9yhf') for i in range(0,12)]) + suffix
filename_choice = []
if (random.randint(0,10) != 1):
	
	for file in os.listdir(dir):
		if file.endswith(suffix):
			filename_choice.append(dir+file)
			print 'found existing busy file'
			
	if len(filename_choice):
		filename = random.choice(filename_choice)

f = open(filename,'ab')

f.write(str(bytearray([random.randint(0,42) for i in range(random.randint(200,300))])))
f.write(''.join([random.choice(message) for i in range(random.randint(10,20))]))

print dir, filename
p = subprocess.Popen("git add " + filename, shell=True,cwd=dir)
p.wait()
print 'added',filename
p = subprocess.Popen('git commit -m "' + message + '"',shell=True,cwd=dir)
p.wait()
print 'commited'
p = subprocess.Popen("git push",shell=True,cwd=dir)
p.wait()
print 'PUSHED!'