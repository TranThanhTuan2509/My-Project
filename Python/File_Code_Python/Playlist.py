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

	def read_video():
		title = input("Enter title: ") + "\n"
		link = input("Enter link: ") + "\n"
		video = Video(title, link)
		return video

	def print_video(video):
		print("Video title: ", video.title, end="")
		print("Video link: ", video.link, end="")

	def read_videos():
		videos = []
		total_video = int(input("Enter how many videos: "))
		for i in range(total_video):
			print("Enter video ", i+1)
			vid = read_video()
			videos.append(vid)
		return videos

	def print_videos(videos):
		total = len(videos)
		for i in range(total):
			print("Video " + str(i+1) + ":")
			print_video(videos[i])

	def write_video_txt(video, file):
		file.write(video.title)
		file.write(video.link)

	def write_videos_txt(videos, file):
		total = len(videos)
		file.write(str(total) + "\n")
		for i in range(total):
			write_video_txt(videos[i], file)

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

	def read_playlist():
		playlist_name = input("Enter playlist name: ") + "\n"
		playlist_description = input("Enter playlist description: ") + "\n"
		playlist_rating = input("Enter rating (1-5): ") + "\n"
		playlist_videos = read_videos()
		playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
		return playlist

	def write_playlist_txt(playlist):
		with open("data.txt", "w") as file:
			file.write(playlist.name)
			file.write(playlist.description)
			file.write(playlist.rating)
			write_videos_txt(playlist.videos, file)
		print("Successfully write playlist to txt")

	def read_playlist_from_txt():
		with open("data.txt", "r") as file:
			playlist_name = file.readline()
			playlist_description = file.readline()
			playlist_rating = file.readline()
			playlist_videos = read_videos_from_txt(file)
		playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
		return playlist

	def print_playlist(playlist):
		print("-------")
		print("Playlist name: " +  playlist.name, end="")
		print("Playlist description: " +  playlist.description, end="")
		print("Playlist rating (1-5): " +  playlist.rating, end="")
		print_videos(playlist.videos)

	def show_menu():
		print("Main Menu:")
		print("-----------------------------")
		print("| Option 1: Create playlist |")
		print("| Option 2: Show playlist   |")
		print("| Option 3: Play a video    |")
		print("| Option 4: Add a video     |")
		print("| Option 5: Update a video  |")
		print("| Option 6: Remove a video  |")
		print("| Option 7: Save and Exit   |")
		print("-----------------------------")
		

	def select_in_range(prompt, min, max):
		choice = input(prompt)
		while not choice.isdigit() or int(choice) < min or int(choice) > max:
			choice = input(prompt)

		choice = int(choice)
		return choice


	def play_video(playlist):
		print_videos(playlist.videos)
		total = len(playlist.videos)

		choice = select_in_range("Select a video (1," + str(total) + "): " , 1,total)
		print("Open video: " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].link, end ="")
		playlist.videos[choice-1].open()

	def add_video(playlist):
		print("Enter new video information:")
		new_video_title = input("Enter new video title: ") + "\n"
		new_video_link =  input("Enter new video link: ") + "\n"
		new_video = Video(new_video_title, new_video_link)
		playlist.videos.append(new_video)
		return playlist

	def up_date(playlist):
		print('1.Up Date Playlist Name')
		print('2.Up Date Playlist description')
		print('3.Up Date Playlist Rating')
		choice = input(select_in_range('Enter option you want to update: ',1,3))
		if choice == 1:
			new_playlist_name = input('Enter new playlist name: ')
			new_playlist_name = playlist.name
			print('Update was successfully')
		elif choice == 2:
			new_playlist_description = input('Enter new playlist description: ')
			new_playlist_description = playlist.description
			print('Update was successfully')
		else: 
			choice == 3
			new_playlist_rating = int(input('Enter new playlist rating (1-5): '))
			new_playlist_rating = playlist.rating
			print('Update was successfully')

		return playlist


	def remove_video(playlist):
		total = len(playlist.videos)
		print_videos(playlist)
		choice = int(select_in_range('Enter video you want to delete: ',1,total))

		del playlist.videos[choice-1]
		print('Delete processing was successfully')

		return playlist


	def main():
		try:
			playlist = read_playlist_from_txt()
			print("Data saving process was successfully")
		except:
			print("Welcome first user !!!")		
		
		while True:
			show_menu()
			choice = select_in_range("Select an option (1-7):", 1, 7)
			if choice == 1:
				playlist = read_playlist()	
				input("\nPress Enter to continue.\n")	
			elif choice == 2:
				print_playlist(playlist)
				input("\nPress Enter to continue.\n")	
			elif choice == 3:
				play_video(playlist)	
				input("\nPress Enter to continue.\n")	
			elif choice == 4:
				playlist = add_video(playlist)	
				input("\nPress Enter to continue.\n")
			elif choice == 5:
				playlist = up_date(playlist)	
				input("\nPress Enter to continue.\n")
			elif choice == 6:
				playlist = remove_video(playlist)	
				input("\nPress Enter to continue.\n")
			elif choice == 7:
				write_playlist_txt(playlist)
				input("\nPress Enter to continue.\n")	
				break
			else:
				print("Wrong Input, Exist.")
				break
				
	main()
			
			