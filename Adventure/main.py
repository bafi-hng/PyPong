from curses import BUTTON1_CLICKED
from turtle import screensize
import pygame
from pygame.locals import *
from sys import exit

#initialize pygame
pygame.init()


#colors
white = (255, 255, 255)
black = (0, 0, 0)


#fonts
font = "Adventure/font/Shadowrun4.ttf"
title_font = pygame.font.Font(font, 70)
text_font = pygame.font.Font(font, 30)
setting_font = pygame.font.Font(font, 50)

#draw screen
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("ADVENTURE GAME")
clock = pygame.time.Clock()


#show title
title_surf = title_font.render("ADVENTURE GAME", True, "White")
title_surf_width = title_surf.get_width()
title_surf_heigth = title_surf.get_height()


#button class
clicked = False
class button():
			
	#colours for button and text
	button_col = (0, 0, 0)
	hover_col = (255, 255, 255)
	text_col = white
	width = 0
	height = 0
	borderwidth = 6
	action = False


	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def isClicked(self):

		global clicked

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create text surface 
		text_img = text_font.render(self.text, True, self.text_col)
		text_wid = text_img.get_width()
		text_hei = text_img.get_height()

		#place position marker to upper middle
		self.width = text_wid + 40
		self.height = text_hei + 30
		new_x = self.x - self.width/2

		#create pygame Rect object for the button
		button_rect = Rect(new_x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			self.text_col = (0, 0, 0)
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				self.action = True
			pygame.draw.rect(screen, self.hover_col, button_rect)

		else:
			self.text_col = (255, 255, 255)
			pygame.draw.rect(screen, self.button_col, button_rect)

		#refresh text surface
		text_img = text_font.render(self.text, True, self.text_col)
		
		#add shading to button
		pygame.draw.line(screen, white, (new_x, self.y), (new_x + self.width, self.y), self.borderwidth)
		pygame.draw.line(screen, white, (new_x, self.y), (new_x, self.y + self.height), self.borderwidth)
		pygame.draw.line(screen, white, (new_x, self.y + self.height), (new_x + self.width, self.y + self.height), self.borderwidth)
		pygame.draw.line(screen, white, (new_x + self.width, self.y), (new_x + self.width, self.y + self.height), self.borderwidth)

		#add text to button
		screen.blit(text_img, (new_x + int(self.width / 2) - int(text_wid / 2), self.y + 17))

		return self.action


#story class
class story():

	white = (255,255,255)
	Clicked = False

	def __init__(self, text):
		self.text = text
		storyline = list(self.text)			#split componentents of text
		self.setting = storyline[0]     	#setting/location of story
		self.story = storyline[1]			#text of story
		self.button1 = button(screen_width/4 + 100, 500, storyline[2].upper())   #button option 1
		self.button2 = button(screen_width*3/4 - 100, 500, storyline[3].upper())  #button option 2


	
	def story_option(self):

		pygame.display.set_caption("Adventure Game")
		
		running = True
		while running:

			#reset screen to black
			screen.fill("black")

			#position and length of textbox
			box_len = 1000
			x_origin = screen_width - box_len
			y_origin = 200

			x = x_origin
			y = y_origin

			#convert text string into list
			words = self.story.split(" ")

			#blit setting
			setting_surf = setting_font.render(self.setting.upper(), True, white)
			setting_width = setting_surf.get_width()
			setting_posx = screen_width/2 - setting_width/2  #center setting
			setting_posy = 70                                #setting position 
			screen.blit(setting_surf, (setting_posx, setting_posy))

			#blit story
			for word in words:
				word_surf = text_font.render(word, True, white)
				word_width, word_height = word_surf.get_size()

				if word_width + x >= box_len:
					x = x_origin
					y += word_height + 2
					screen.blit(word_surf, (x, y))
					
				screen.blit(word_surf, (x, y))
				x +=  word_width + 8


			#quit game
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()                
					exit()
			
			#option 1
			if self.button1.isClicked():
				running = False
				return True
			
			elif self.button2.isClicked():
				running = False
				return False

			pygame.display.update()



###PLOT POINTS###
plot_point1 = story(("[wald]","Du bist in einem dunklem Wald. Um dich herum sieht du keine weitere Person, "\
	"sondern nur ein kleine Hütte. Aus den Fenstern leuchtet Licht und aus dem Schornstein steigt Rauch auf. " \
	"Was willst du machen?", "Wald erkunden", "Hütte erkunden"))

plot_point2_1 = story(("[wald]", "Du läufst durch den Wald und gelangst nach einiger Zeit zu einer kleinen Straße. "\
	"Zu deiner Linken schlängelt sich die Straße weiter durch den dichten Wald. Zur deiner Rechten steht "\
	"einige Meter weiter  ein Straßenschild auf dem steht: SAMVILLE [500m]. Wohin willst du laufen? ", "links", "rechts"))

plot_point2_2 = story(("[hütte]", "Du läufst zu Hütte und klopfst an die Tür. Es kommt keine Antwort. "\
	"Du machst die Tür auf und du siehst vor dir eine alte Frau die an die Wand starrt. Was willst du machen?", "Frau ansprechen", "zurück in den wald"))

plot_point3_1 = story(("[straße]", "Du bist der Straße einige Zeit gefolgt und siehst, dass sie direkt vor dem Wald aufhört. "\
	"Nach einem kurzen Blick durch die Umgebung, erkennst du die wieder die Hütte in der Ferne. "\
		"Was willst du machen?", "umkehren", "zur hütte laufen"))

plot_point3_2 = story(("[samville]", "Nach einiger Zeit siehst du vor dir ein kleines Dorf.  "\
	"Was willt du machen?", "schreien", "rennen"))


#buttons
exit_button = button(screen_width/2, 500, "EXIT")
start_button = button(screen_width/2, 350, "PLAY")
hit_button = button(screen_width/3, 500, "EXIT")

def main_menu():

	pygame.display.set_caption("Adventure Game")

	running = True
	while running:

		# show title
		screen.blit(title_surf, (screen_width/2 - title_surf_width/2, 200) )

		#exit game event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()                
				exit()
			
		if start_button.isClicked():
			#show plot_point1
			if plot_point1.story_option():
				if plot_point2_1.story_option():
					if plot_point3_1.story_option():
						pass
			
			else:
				if plot_point2_2.story_option():
					if plot_point3_2.story_option():
						pass
			
		if exit_button.isClicked():
			pygame.exit()
			exit()
			
		pygame.display.update()
		clock.tick(30)


main_menu()