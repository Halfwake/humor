import time

def display(text):
	print text
	time.sleep(SLEEP_TIME)

SLEEP_TIME = 0.1
symbols = [r"      /\ ",
	r"      ||",
	r"      ||",
	r"      ||",
	r"      ||",
	r"      ||",
	r"      ||",
	r"      ||",
	r"      ||",
	r"      ||",
	r"     //\\",
	r"    //  \\",
	r"   //    \\",
	r"  // H  H \\",
	r"  \\ U  U //",
	r"   \\    //"]
for symbol in symbols: display(symbol)
while True:
	symbols = [r"  //    //",
	r" //    //",
	r"//    //",
	r"\\    \\",
	r" \\    \\",
	r"  \\    \\"]
	for symbol in symbols: display(symbol)
