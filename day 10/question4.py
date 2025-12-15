#Task A: The Cleaner Variable: raw_data = " $$Bill Gates$$ "
#Use .strip() to remove spaces.
#Use .replace() to remove the $ signs.
#Print the clean name ("Bill Gates").

raw_data = " $$Bill Gate$$ "
clear_space = raw_data.strip()
main_data = clear_space.replace("$","")
print(main_data)