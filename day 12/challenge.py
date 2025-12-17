#Daily Challenge: "The Digital Diary"
#Scenario: You want a quick way to log your thoughts.

#Instructions:
#Use input() to ask: "What is on your mind?"
#Open a file named diary.txt in Append Mode ("a").
#Write the user's input into the file.
#Bonus: Add a \n so the next entry starts on a new line.
#Print "Entry saved."
#Run the program 3 times with different inputs.
#Open the diary.txt file in VS Code (click it in the sidebar) to prove the data is actually there!


task = input("What is on your mind? ")

with open("diary.txt","a") as daily_dairy:
	daily_dairy.write(f"{task}\n")
	print("Entry Saved")