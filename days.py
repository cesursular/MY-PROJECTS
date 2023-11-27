def days():
  today = input("entry a day: ")
  if today == "monday":
    print("I had a packed schedule over the weekend with family commitments and unfortunately didn't get enough rest. I need some additional time on Monday to recuperate to ensure I can focus at work.")
    monday()
  elif today == "tuesday":
    print("There's an urgent repair issue at home that needs to be addressed, and the only time the technician can come is on Tuesday. I need to be at home to oversee the work.")
    tuesday()
  elif today == "wednesday":
    print("I have a previously scheduled doctor's appointment that cannot be postponed. I will need to take a few hours off on Wednesday for my health check-up.")
    wednesday()
  elif today == "thursday":
    print("My car's service is taking longer than expected, and I need to pick it up on Thursday afternoon, requiring me to be away from work for a few hours.")
    thursday()
  elif today == "friday":
    print("I've been experiencing persistent headaches and have an appointment with a neurologist on Friday that I must attend.")
    friday()
  elif today == "saturday":
    print("If working on weekends: There's a family member’s birthday celebration that I can't miss. May I take a few hours off on Saturday?")
    saturday()
  elif today == "sunday":
    print("If working on weekends: We have an important family gathering that requires my attendance. Could I possibly have a few hours off on Sunday?")
    sunday()
  else:
    raise ValueError("Unknown today")

def monday():
  try:
    score = int(input("How do you feeling on mondays (1-10)? "))
		if score <= 5:
			print("I'm sorry to hear that. Take your time and rest well with your family.")
		elif score >= 5:
			print("You are feeling good my friend")
		except ValueError:
			print("enter a valid number between 1-10")

def tuesday():
  try:
    score = int(input("is it urgent problem on tuesday (1-10)? "))
		if score <= 5:
			print("You have to come to work my friend, its not looking urgent.")
		elif score >= 5:
			print("Take your time my friend.")
		except ValueError:
			print("enter a valid number between 1-10")

def wednesday():
  try:
    score = int(input("How can you describe your health situation on wednesday (1-10)? "))
		if score <= 5:
			print("I'm sorry to hear that. Take your time and rest well with your family.")
		elif score >= 5:
			print("You are feeling good my friend")
		except ValueError:
			print("enter a valid number between 1-10")

def thursday():
  try:
    score = int(input("How do you feeling on mondays (1-10)? "))
		if score <= 5:
			print("Almost the weekend. If you need to pick up your car from the service, go ahead..")
		elif score >= 5:
			print("Great to see you're feeling good on a Thursday.")
		except ValueError:
			print("enter a valid number between 1-10")

def friday():
    try:
        score = int(input("How do you feel on Fridays (1-10)? "))
        if score <= 5:
            print("It's been a long week. A doctor's visit might be just what you need to start the weekend right.")
        elif score > 5:
            print("Friday's looking good! Ready for the weekend?")
    except ValueError:
        print("Please enter a valid number between 1-10.")

def saturday():
    try:
        score = int(input("How do you feel on Saturdays (1-10)? "))
        if score <= 5:
            print("Take it easy. Weekends are for family time and celebrations.")
        elif score > 5:
            print("Enjoy the weekend vibes!")
    except ValueError:
        print("Please enter a valid number between 1-10.")

def sunday():
    try:
        score = int(input("How do you feel on Sundays (1-10)? "))
        if score <= 5:
            print("A day of rest before the new week is always a good idea.")
        elif score > 5:
            print("End the weekend on a high note!")
    except ValueError:
        print("Please enter a valid number between 1-10.")
	days()

    
    
    
