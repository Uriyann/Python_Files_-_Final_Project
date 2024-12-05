print("\n\tPersonal Bio Data Registration:")

f_name = input("\n\t\tEnter Your First Name: ")
m_name = input("\t\tEnter Your Middle Initial: ")
l_name = input("\t\tEnter Your Last Name: ")

age = int(input("\n\t\tEnter Your Age: "))
gender = input("\t\tEnter Your Gender: ")

birthdate_m = input("\n\t\tEnter Your Birth Month: ")
birthdate_d = int(input("\t\tEnter Your Birth Day: "))
birthdate_y = int(input("\t\tEnter Your Birth Year: "))
birthplace = input("\t\tEnter Your Birth Place: ")

weight = float(input("\n\t\tEnter Your Weight: "))
height = float(input("\t\tEnter Your Height: "))

civ_stat = input("\n\t\tEnter Your Civil Status: ")
rel = input("\t\tEnter Your Type of Religion: ")
citi = input("\t\tEnter Your Citizenship: ")
lang = input("\t\tEnter Your Known Language: ")

strt = input("\n\t\tEnter Your Street: ")
brgy = input("\t\tEnter Your Barangay: ")
city = input("\t\tEnter Your City: ")
prvnc = input("\t\tEnter Your Province: ")

num = int(input("\n\t\tEnter Your Phone No.: "))
email = input("\t\tEnter Your Email: ")
bsit = True

print("\n\n\tPersonal Complete Bio Data:")

print("\n\t\tHello "+f_name,m_name,l_name+"! You belong to the gender of "+gender+" and you are at the age of\b",
      age,". With your birthdate at "+birthdate_m,birthdate_d,birthdate_y,"and in the birthplace of "+
      birthplace+". You weight at an average of",weight,"kg, and with the height of",height,"cm. You are "+
      civ_stat+", belonging to the religion of "+rel+" with your citizenship of "+citi+" and you have known "+
      lang+" languages. You currently live in "+strt+", "+brgy+", "+city+", "+prvnc+". You currently use the phone number",
      num,"and the email "+email+". Lastly, you are a student of DLL from department of BSIT:",bsit)