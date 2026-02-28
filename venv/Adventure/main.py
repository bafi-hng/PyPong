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
		self.storyline = list(self.text)			#split components of text
		self.setting = self.storyline[0]     	#setting/location of story
		self.story = self.storyline[1]			#text of story
		self.button1 = button(screen_width/4 + 100, 500, self.storyline[2].upper())   #button option 1
		self.button2 = button(screen_width*3/4 - 100, 500, self.storyline[3].upper())  #button option 2


	
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
			if self.storyline[2] == "empty":
				pass
			else:
				if self.button1.isClicked():
					running = False
					return True
			

			#option 2
			if self.button2.isClicked():
				running = False
				return False

			pygame.display.update()



###PLOT POINTS###
plot_point1 = story(("[wald]","Du bist in einem dunklem Wald. Um dich herum sieht du keine weitere Person, "\
	"sondern nur ein kleine Hütte. Aus den Fenstern leuchtet Licht und aus dem Schornstein steigt Rauch auf. " \
	"Was willst du machen?", "Wald erkunden", "Hütte erkunden"))

plot_point2_1 = story(("[wald]", "Du läufst durch den Wald und gelangst nach einiger Zeit zu einer kleinen Straße. "\
	"Zu deiner Linken schlängelt sich die Straße weiter durch den dichten Wald. Zur deiner Rechten steht "\
	"einige Meter weiter ein Straßenschild auf dem steht: SAMVILLE [500m]. Wohin willst du laufen? ", "links", "rechts"))

plot_point2_2 = story(("[hütte]", "Du läufst zu Hütte und klopfst an die Tür. Es kommt keine Antwort. "\
	"Du machst die Tür auf und du siehst vor dir eine alte Frau die an die Wand starrt. Was willst du machen?", "Frau ansprechen", "umkehren"))

plot_point2_2_1 = story(("[hütte]", "Du läufst zu Hütte und klopfst an die Tür. Es kommt keine Antwort. "\
	"Du machst die Tür auf und du siehst vor dir eine alte Frau die an die Wand starrt. Was willst du machen?", "empty", "umkehren"))

plot_point3_1 = story(("[straße]", "Nach dem du der Straße einige Zeit gefolgt bist, steht auf einmal eine dunkle, sehr große Gestalt vor dir. "\
	"Du glaubst Fell an dieser Gestalt zu sehen... Was willst du machen?" ,"zur Gestalt laufen", "umkehren"))

plot_point3_2 = story(("[straße]", "Nach einiger Zeit siehst du vor dir ein kleines Dorf.  Du siehst ein Schild mit der Aufschrift: "\
	"WILLKOMMEN IN SAMVILLE. Außerdem siehst du, dass auf der anderen Seite der Straße Rand ein altes Auto steht, du kann jedoch niemanden darin sehen. "\
	"Was willt du machen?", "zum auto laufen", "weiterlaufen"))

plot_point3_3 = story(("[hütte]", "Du spricht die Frau an und sie dreht sich langsam zu dir um. Du erschreckst dich als du siehst, dass sie keine Augen hat "\
	"und Blut aus ihrem kalten Grinsen fließt. Nun siehst du auch, dass vor hinter ihr die blutige Leiche eines kleinen Kindes liegt. "\
	"Was willst du machen?", "angreifen", "rennen"))

plot_point3_4 = story(("[wald]", "Du machst die Tür wieder zu und kehrst um. Du bist keine 10 Meter gelaufen als du auf einmal hinter der Tür ein kreischen hörst. "\
	"Ein Blick nach hinten zeigt dir die alte Frau, die keine Augen hat und mit blutverschmiertem Gesicht an der Tür steht. "\
	"Was willst du machen?", "losrennen", "angreifen"))

plot_point3_1_1 = story(("[straße]", "Nach dem du der Straße einige Zeit gefolgt bist, steht auf einmal eine dunkle, sehr große Gestalt vor dir. "\
	"Du glaubst Fell an dieser Gestalt zu sehen... Was willst du machen?" ,"empty", "umkehren"))

plot_point3_2_1 = story(("[straße]", "Nach einiger Zeit siehst du vor dir ein kleines Dorf.  Du siehst ein Schild mit der Aufschrift: "\
	"WILLKOMMEN IN SAMVILLE. Außerdem siehst du, dass auf der anderen Seite der Straße Rand ein altes Auto steht, du kann jedoch niemanden darin sehen. "\
	"Was willt du machen?", "empty", "weiterlaufen"))

plot_point3_3_1 = story(("[hütte]", "Du spricht die Frau an und sie dreht sich langsam zu dir um. Du erschreckst dich als du siehst, dass sie keine Augen hat "\
	"und Blut aus ihrem kalten Grinsen fließt. Nun siehst du auch, dass vor hinter ihr die blutige Leiche eines kleinen Kindes liegt. "\
	"Was willst du machen?", "empty", "rennen"))
	
plot_point3_4_1 = story(("[wald]", "Du machst die Tür wieder zu und kehrst um. Du bist keine 10 Meter gelaufen als du auf einmal hinter der Tür ein kreischen hörst. "\
	"Ein Blick nach hinten zeigt dir die alte Frau, die keine Augen hat und mit blutverschmiertem Gesicht an der Tür steht. "\
	"Was willst du machen?", "empty", "angreifen"))

plot_point4_1 = story(("[straße]", "Du versuchst näher an die Gestalt zu gehen. Bevor du aber reagieren kannst, greift dich die Gestalt an! "\
	"Tut mir Leid... DU WURDEST VON BIGFOOT GETÖTET!", "zurück", "Spiel beenden"))

plot_point4_2 = story(("[straße]", "Du näherst dich langsam dem Auto. Die Fahrertür des Autos wird plötzlich geöffnet und ein Mann steigt aus. "\
	"Zu spät siehst du die Pistole in seiner Hand... er erschießt dich und du fällst zu Boden! Bevor du das Bewusstsein verlierst, siehst du, dass der Mann "\
	"sich vor dich kniegt und dich anlächelt. Tut mir Leid... DU WURDEST VOM ZODIAC KILLER GETÖTET!", "zurück", "Spiel beenden"	))

plot_point4_3 = story(("[samville]", "Du bist nun in Samville und läufst die Straße entlang. Etwa 100 Meter vor dir, direkt an der Straße, siehst du ein Haus. "\
	"Das Haus ist beleuchtet und du kannst riechen, dass jemand etwas kocht. Was willst du machen?", "weitergehen", "zum haus laufen"))

plot_point4_3_1 = story(("[samville]", "Du bist nun in Samville und läufst die Straße entlang. Etwa 100 Meter vor dir, direkt an der Straße, siehst du ein Haus. "\
	"Das Haus ist beleuchtet und du kannst riechen, dass jemand etwas kocht. Was willst du machen?", "empty", "zum haus laufen"))

plot_point4_4 = story(("[hütte]", "Du stürmst in die Hütte und versuchst ihr einen Schlag zu versetzten. Sie ist jedoch schneller als du dachtest, weicht aus "\
	"und greift dich an. Du fällst wehrlos zu Boden und kannst nur dabei zu sehen, wie dir die alte Frau in den Hals beißt. Tut mir Leid... BABA JAGA HAT DIE GEFRESSEN!",
	"zurück", "Spiel beenden"))

plot_point4_5 = story(("[wald]", "Du rennst los und kannst den Abstand zwischen dir und der Frau erweitern, als du plötzlich stolperst. "\
	"Leider kannst du nicht schnell genug aufstehen und das Letzte, das du siehst, ist wie sich die Frau auf die lostürzt. "\
	"Tut mir Leid... DU WURDEST VON BABA JAGA GETÖTET!", "zurück", "Spiel beenden"))

plot_point4_6 = story(("[wald]", "Während sich die alte Frau dir schnell nähert, entdeckst du neben dir einen großen Stock. "\
	"Du hebst ihn auf, holst aus und genau als sie auf die zuspringt, schlägst du ihr ins Gesicht! Sie fällt zu Boden und bewegt sich nicht mehr. "\
	"Was willst du machen?", "Frau untersuchen", "weiterrennen"))

plot_point4_6_1 = story(("[wald]", "Während sich die alte Frau dir schnell nähert, entdeckst du neben dir einen großen Stock. "\
	"Du hebst ihn auf, holst aus und genau als sie auf die zuspringt, schlägst du ihr ins Gesicht! Sie fällt zu Boden und bewegt sich nicht mehr. "\
	"Was willst du machen?", "empty", "weiterrennen"))

plot_point5_1 = story(("[samville]", "Du folgst der Straße weiter. Auf einmal wirst du von hinten durch ein helles Licht erleuchtet und du kannst den Motor eines Autos hören. "\
	"Du bist jedoch nicht schnell genug, um auszuweichen und... DU WURDEST ÜBERFAHREN!", "zurück", "spiel beenden"))

plot_point5_2 = story(("[haus]", "Du öffnest die Tür des Hauses und merkst, dass das Innere das Hauses dir bekannt vorkommt. "\
	"Eine Frau rennt auf einmal durch eine der Türen vor dir und schaut dich geschockt an. Sie rennt auf dich zu und nimmt dich in ihren Armen. "\
	"Du erinnerst dich wieder wer du bist... Herzlichen Glückwunsch, du hast überlebt!", "zum Startmenu", "Spiel beenden"))

plot_point5_3 = story(("[wald]", "Du näherst dich langsam den regungslosen Körper der Frau. Du stubst sie mit dem Stock an und sie bewegt sich immer noch nicht. "\
	"Vor Erleichterung seufzt du auf. Plötzlich springt sie wieder, du bist jedoch zu langsam um zu reagieren und sie greift dich an. "\
	"Tut mir Leid... DU BIST BABA JAGA ZUM OPFER GEFALLEN!", "zurück", "spiel beenden"))

plot_point5_4 = story(("[wald]", "Du sprintest los und kannst nach kurzer Zeit die Hütte hinter dir nicht mehr sehen. Herzlichen Glückwunsch... Du bist Baba Jaga entkommen!", "zum Startmenu", "Spiel beenden"))


#buttons
exit_button = button(screen_width/2, 500, "SPIEL BEENDEN")
start_button = button(screen_width/2, 350, "SPIEL STARTEN")


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
						if plot_point4_1.story_option():
							if plot_point3_1_1.story_option() is False:
								if plot_point3_2.story_option():
									if plot_point4_2.story_option():
										if plot_point3_2_1.story_option() is False:
											if plot_point4_3.story_option():
												if plot_point5_1.story_option():
													if plot_point4_3_1.story_option() is False:
														if plot_point5_2.story_option():
															break
														else:
															break
									else:				
										break
								else:
									if plot_point4_3.story_option():
										if plot_point5_1.story_option():
											break
										else:
											break
									else:
										if plot_point5_2.story_option():
											break
										else:
											break
						else: 
							break
					else: 
						if plot_point3_2.story_option():
							if plot_point4_2.story_option():
								break
						else:
							if plot_point4_3.story_option():
								if plot_point5_1.story_option():
									break
							else:
								if plot_point5_2.story_option():
									break
				else:
					if plot_point3_2.story_option():
						if plot_point4_2.story_option():
							break
					else:
						if plot_point4_3.story_option():
							if plot_point5_1.story_option():
								break
						else:
							if plot_point5_2.story_option():
								break
			else:
				if plot_point2_2.story_option():
					if plot_point3_3.story_option():
						if plot_point4_4.story_option():
							if plot_point3_3_1.story_option() is False:
								if plot_point4_5.story_option():
									if plot_point2_2_1.story_option() is False:
										if plot_point3_4.story_option():
											if plot_point4_5.story_option():
												if plot_point3_4_1.story_option() is False:
													if plot_point4_6.story_option():
														if plot_point5_3.story_option():
															if plot_point4_6_1.story_option() is False:
																if plot_point5_4.story_option():
																	break
																else:
																	break
													else:	
														if plot_point5_4.story_option():
															break
														else:
															break
										else:
											if plot_point4_6.story_option():
												if plot_point5_3.story_option():
													if plot_point4_6_1.story_option() is False:
														if plot_point5_4.story_option():
															break
														else:
															break
											else:	
												if plot_point5_4.story_option():
													break
												else:
													break
								else:
									break
						else:
							break
					else: 
						if plot_point4_5.story_option():
							break
				else:
					if plot_point3_4.story_option():
						if plot_point4_5.story_option():
							if plot_point3_4_1.story_option() is False:
								if plot_point4_6.story_option():
									if plot_point5_3.story_option():
										if plot_point4_6_1.story_option() is False:
											if plot_point5_4.story_option():
												break
											else:
												break
								else:
									if plot_point5_4.story_option():
										break
									else:
										break
					else: 
						if plot_point4_6.story_option():
							if plot_point5_3.story_option():
								if plot_point4_6_1.story_option() is False:
									if plot_point5_4.story_option():
										break
									else:
										break
						else:
							if plot_point5_4.story_option():
								break
							else:
								break

		if exit_button.isClicked():
			pygame.exit()
			exit()
			
		pygame.display.update()
		clock.tick(30)


main_menu()