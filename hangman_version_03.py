import pygame 
import math 
import random 

pygame.init() 
WIDTH, HEIGHT= 500, 700
win=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("HANGMAN") 

FPS=60
clock=pygame.time.Clock() 
run=True
imag=pygame.image.load('lose.png')

#buttons 
radius=20
space=20
letters=[] #[399,122,"A",True] 
x_start=round(130+(WIDTH-(radius*2 + space)*13)/2) 
y_start=500

A=65 # Using ACII value to print letters on the button. A->65, B->66 and so on 

for i in range(26): 
	x=x_start + space*2 + ((radius*2 + space)* (i%13)) 
	y=y_start + ((i//13) * (space + radius*2)) 
	letters.append([x,y,chr(A+i),True]) 

# Fonts 
font=pygame.font.SysFont("Pokemon GB.ttf",55) 
WORD=pygame.font.SysFont("Pokemon GB.ttf",50,) 
TITLE=pygame.font.SysFont("Releway Black",70,) 
TI=pygame.font.SysFont("alile",20,italic=True)
NUM=pygame.font.SysFont("alile",50,italic=True)

# Time to load images so we can draw a hangman 
images=[] 
for i in range(0,7): 
	image=pygame.image.load("hangman"+str(i)+".png") 
	imagee=pygame.transform.scale(image,(300,600))
	images.append(imagee) 

print(images) 

# game variable 
hangman=0
lists=["GEEKS","GFG","DOCKER","DEVELOPER","RUST","GITHUB","R","PYTHON","BASH"  "ALGORITHM", "DATA", "SCIENCE", "MACHINE", "LEARNING",
       "ARTIFICIAL", "INTELLIGENCE", "NETWORK", "SECURITY", "CRYPTOGRAPHY", "DATABASE",
       "WEB", "DEVELOPMENT", "MOBILE", "APPLICATION", "OPERATING", "SYSTEM", "LINUX",
       "WINDOWS", "ANDROID", "IOS", "JAVA", "JAVASCRIPT", "HTML", "CSS", "PHP", "MYSQL",
       "POSTGRESQL", "MONGODB", "REDIS", "DOCKER", "KUBERNETES", "AWS", "AZURE", "GCP",
       "SERVERLESS", "MICROSERVICES", "CONTAINERIZATION", "DEVOPS", "GIT", "VERSION", "CONTROL",
       "AGILE", "SCRUM", "KANBAN", "TEST", "AUTOMATION", "CI/CD", "DEPLOYMENT", "INFRASTRUCTURE",
       "ARCHITECTURE", "FRAMEWORK", "LIBRARY", "PACKAGE", "MODULE", "RECURSION", "ITERATION",
       "FUNCTION", "VARIABLE", "CONSTANT", "CONDITIONAL", "LOOP", "OBJECT", "ORIENTED",
       "PROGRAM", "INTERFACE", "ABSTRACTION", "ENCAPSULATION", "INHERITANCE", "POLYMORPHISM",
       "ALGORITHMIC", "PROBLEM", "SOLUTION", "EFFICIENCY", "OPTIMIZATION", "DATA", "STRUCTURE",
       "QUEUE", "STACK", "LINKED", "LIST", "TREE", "GRAPH", "HASH", "TABLE", "SEARCH", "SORT",
       "BINARY", "HEAP", "BFS", "DFS", "RECURSIVE", "ITERATIVE", "DYNAMIC", "PROGRAMMING",
       "GREEDY", "BACKTRACKING", "SLIDING", "WINDOW", "STRING", "MATCHING", "PATTERN",
       "REGULAR", "EXPRESSION", "OPERATOR", "PRECEDENCE", "ASSOCIATIVITY", "MEMORY", "MANAGEMENT",
       "ALLOCATIONS", "DEALLOCATIONS", "POINTERS", "REFERENCES", "ALLOCATION", "DEALLOCATION",
       "SEGMENTATION", "FAULT", "STACK", "OVERFLOW", "UNDERFLOW", "GARBAGE", "COLLECTION",
       "CYCLE", "DETECTION", "MEMORY", "LEAK", "VIRTUAL", "PAGING", "SWAPPING", "FRAGMENTATION",
       "CACHE", "MISS", "HIT", "THREADED", "MULTITHREADING", "SYNCHRONIZATION", "CONCURRENCY",
       "DEADLOCK", "LIVENESS", "STARVATION", "PRODUCER", "CONSUMER", "MONITOR", "SEMAPHORE",
       "MESSAGE", "PASSING", "PROCESS", "THREAD", "CONTEXT", "SWITCH", "SCHEDULING", "FCFS",
       "SJF", "RR", "PRIORITY", "PREEMPTIVE", "NON-PREEMPTIVE", "KERNEL", "USER", "SPACE",
       "PROCESS", "COOPERATION", "PREEMPTION", "SYSTEM", "CALL", "API", "LIBRARY", "KERNEL",
       "DEVICE", "DRIVER", "FILE", "DIRECTORY", "I/O", "INTERRUPT", "HANDLER", "BUFFER",
       "CACHE", "CIRCUIT", "DIGITAL", "ANALOG", "VOLTAGE", "CURRENT", "RESISTANCE", "CAPACITANCE",
       "INDUCTANCE", "OHM", "KIRCHHOFF", "LAWS", "ANALYSIS", "DESIGN", "SIMULATION", "ELECTRONICS",
       "ELECTRICAL", "ENGINEERING", "CIRCUIT", "DESIGN", "DIGITAL", "LOGIC", "GATE", "COMBINATIONAL",
       "SEQUENTIAL", "FLIP-FLOP", "TRIGGER", "MICROPROCESSOR", "MICROCONTROLLER", "ARM", "RISC",
       "CISC", "MIPS", "INTEL", "ATMEL", "ARDUINO", "RASPBERRY", "PI", "SENSOR", "ACTUATOR",
       "CONTROLLER", "EMBEDDED", "SYSTEM", "REAL-TIME", "APPLICATION", "INDUSTRIAL", "AUTOMATION",
       "ROBOTICS", "MECHATRONICS", "MECHANICAL", "ENGINEERING", "THERMODYNAMICS", "FLUID", "MECHANICS",
       "SOLID", "MECHANICS", "KINEMATICS", "DYNAMICS", "MATERIALS", "STRUCTURES", "MANUFACTURING",
       "PROCESS", "AUTOMATION", "CAD", "CAM", "CAE", "3D", "PRINTING", "CNC", "MACHINING",
       "LASER", "CUTTING", "WELDING", "ROBOT", "PROGRAMMING", "INDUSTRIAL", "DESIGN", "PARAMETRIC",
       "MODELING", "FINITE", "ELEMENT", "ANALYSIS", "SIMULATION", "OPTIMIZATION", "PRODUCT", "LIFECYCLE",
       "MANAGEMENT", "PLM", "ERP", "ERP", "MATERIAL", "REQUIREMENTS", "PLANNING", "MRP", "CAPACITY",
       "REQUIREMENTS", "PLANNING", "CRP", "SHOP", "FLOOR", "CONTROL", "SFC", "SCHEDULING", "MES",
       "MANUFACTURING", "EXECUTION", "SYSTEM", "QUALITY", "MANAGEMENT", "TQM", "QMS", "SIX", "SIGMA",
       "LEAN", "MANUFACTURING", "ISO", "CERTIFICATION", "SUPPLY", "CHAIN", "MANAGEMENT", "SCM", "LOGISTICS",
       "WAREHOUSE", "MANAGEMENT", "INVENTORY", "MANAGEMENT", "DISTRIBUTION", "TRANSPORTATION", "FREIGHT",
       "FORWARDING", "CUSTOMS", "CLEARANCE", "INTERNATIONAL", "TRADE", "EXPORT", "IMPORT", "TRADE", "FINANCE",
       "FOREX", "HEDGING", "RISK", "MANAGEMENT", "INSURANCE", "BANKING", "LOAN", "MORTGAGE", "INVESTMENT",
       "PORTFOLIO", "MANAGEMENT", "STOCK", "MARKET", "COMMODITY", "MARKET", "DERIVATIVE", "MARKET",
       "FUTURES", "OPTIONS", "SWAPS", "FORWARDS", "CRYPTOCURRENCY", "BLOCKCHAIN", "BITCOIN", "ETHEREUM",
       "SMART",] 
words=random.choice(lists) 
guessed=[] # to track the letters we have guessed 

# function to draw buttons, and hangman 
def draw(): 
	# win.fill((255, 255, 255)) # display with white color
 # baground 
	size=pygame.transform.scale(imag,(1100,700))
	win.blit(size,(0,0))
	# TITLE for the game 

	title=TITLE.render("HangMan",1,(0,0,0,0)) 
	win.blit(title,(WIDTH/1.8 -title.get_width(), 10)) # Title in center and then y axis= 24 
	ti=TI.render("Classic Word-Guessing.........",1,(0,0,0,0))
	win.blit(ti,(580,55))
	num=NUM.render(str((6-hangman)),1,(0,0,0,0))
	win.blit(num,(1000,20))
	

	# draw word on the screen 
	disp_word="" 
	for letter in words: 
		if letter in guessed: 
			disp_word += letter + " "

		else: 
			disp_word +="_ "

	text=WORD.render(disp_word,1,(0,0,0,0)) 
	win.blit(text,(650,300)) 

	#buttons at center 
	for btn_pos in letters: 
		x,y,ltr,visible=btn_pos # making button visible and invisible after clikcing it 

		if visible: 
			pygame.draw.rect(win,(0,0,0,0),(0,540,0,0))
			txt=font.render(ltr,1,(0,0,0,0)) 
			win.blit(txt,(x-txt.get_width()/2,y-txt.get_height()/2)) 

	win.blit(images[hangman], (70, 63)) 
	pygame.display.update() 



while run: 
	clock.tick(FPS) 
	draw() 

	for event in pygame.event.get(): # Triggering the event 
		if event.type==pygame.QUIT: 
			run=False

		if event.type==pygame.MOUSEBUTTONDOWN: 

			x_mouse, y_mouse=pygame.mouse.get_pos() 
			#print(pos) 

			for letter in letters: 
				x,y,ltr,visible=letter 

				if visible: 
					dist = math.sqrt((x - x_mouse) ** 2 + (y - y_mouse) ** 2) 

					if dist<=radius: 
						letter[3]=False #to invisible the clicked button 
						guessed.append(ltr) 
						if ltr not in words: 
							hangman +=1

# -------------------------------------------------------------------------------- 
# deciding if you won the game or not 
	won=True
	for letter in words: 
		if letter not in guessed: 
			won=False
			break

	if won: 
		draw() 
		pygame.time.delay(1000) 
		win.fill((0,0,0,0)) 
		text=WORD.render("YOU WON",1,(129,255,0,255)) 
		win.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2)) 
		pygame.display.update() 
		pygame.time.delay(4000) 
		print("WON") 
		break

	if hangman==6: 
		draw() 
		pygame.time.delay(1000) 
		win.fill((0, 0, 0, 0)) 
		text = WORD.render("YOU LOST", 1, (255, 0, 5, 255)) 
		answer=WORD.render("The answer is "+words,1,(129,255,0,0)) 
		win.blit(text, (WIDTH / 2 - text.get_width() / 2, 
						HEIGHT / 2 - text.get_height() / 2)) 
		win.blit(answer, ((WIDTH / 2 - answer.get_width() / 2), 
						(HEIGHT / 2 - text.get_height() / 2)+70)) 

		pygame.display.update() 
		pygame.time.delay(4000) 
		print("LOST") 
		break




pygame.quit()
