import pygame
import webbrowser

if __name__ == "__main__":
	class Password:
		def __init__(self,username,password):
			self.username = username
			self.password = password

	class Video:
		def __init__(self, title, link):
			self.title = title
			self.link = link
			self.seen = False

		def open(self):
			webbrowser.open(self.link,new=0)
			self.seen = True

	class Playlist:
		def __init__(self, name, description, rating, videos):
			self.name = name
			self.description = description
			self.rating = rating
			self.videos = videos

	class Text_position:
		def __init__(self,text,position):
			self.text = text
			self.position = position

			

		def check_mouse_position(self):
			mouse_x,mouse_y = pygame.mouse.get_pos()
			if (mouse_x >= self.position[0]) and (mouse_x <= (self.position[0] + self.text_box[2])) and (mouse_y >= self.position[1]) and (mouse_y <= (self.position[1] + self.text_box[3])):
				return True

			else:
				return False
																											
		def draw(self):
			font = pygame.font.SysFont('sans',20)
			text_render = font.render(self.text, True, (0,0,255))
			self.text_box = text_render.get_rect()

			if self.check_mouse_position():
				text_render = font.render(self.text, True, (0,0,255))
			else:
				text_render = font.render(self.text, True, (255,255,255))


			scream.blit(text_render,self.position)


	def read_video_from_txt(file):
		title = file.readline()
		link = file.readline()
		video = Video(title, link)
		return video

	def read_videos_from_txt(file):
		videos = []
		total = file.readline()		
		for i in range(int(total)):
			video = read_video_from_txt(file)
			videos.append(video)
		return videos

	def read_playlist_from_txt(file):
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
		playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
		return playlist

	def read_playlists_from_txt():
		playlists = []
		with open("data.txt", "r") as file:
			total = file.readline()
			for i in range(int(total)):
				playlist = read_playlist_from_txt(file)
				playlists.append(playlist)
		return playlists

	if __name__ == "__main__":
		pygame.init()
		scream = pygame.display.set_mode((563,375))
		pygame.display.set_caption("Space")
		Clock = pygame.time.Clock()
		running = True
		background_picture = pygame.image.load("TXT_PICTURE\Space1.jpg")
		playlists = read_playlists_from_txt()
		# rating = Text_position("Rating playlist: " + playlist.rating.strip(),(1,1))
		playlists_btn_list = []
		videos_btn_list = []
		margin = 50
		playlist_choice = None
		for i in range(len(playlists)):
			playlist_btn = Text_position(playlists[i].name.rstrip(), (50,50+margin*i))
			playlists_btn_list.append(playlist_btn)

		while running:
			Clock.tick(60)
			scream.fill((255,255,255))
			scream.blit(background_picture,(0,0))
			# rating.draw()

			for playlist_button in playlists_btn_list:
				playlist_button.draw()
			for video_button in videos_btn_list:
				video_button.draw()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				
				
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						for i in range(len(playlists_btn_list)):
							if playlists_btn_list[i].check_mouse_position(): 	
								playlist_choice = i				
								videos_btn_list = []
								for j in range(len(playlists[i].videos)):
									video_btn = Text_position(str(j+1) + ". " + playlists[i].videos[j].title.rstrip(), (250,50+margin*j))
									videos_btn_list.append(video_btn)

						if playlist_choice != None:
							for i in range(len(videos_btn_list)):
								if videos_btn_list[i].check_mouse_position():
									playlists[playlist_choice].videos[i].open()
							
								
								
			pygame.display.update()