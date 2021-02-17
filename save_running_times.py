# This program saves a sequence of video running time to the video_times.txt file.

def main():
    # Get the number of videos in the project.
    num_video = int(input('How many videos are in the project?: '))

    # Open the file to hold the running times.
    video_file = open('video_times.txt', 'w')

    # Get each video's running time and write it to the file.
    print('Enter the running time for each video')
    for count in range(1, num_video + 1):
        run_time = float(input('Video #' + str(count) + ': '))
        video_file.write(str(run_time) + '\n')

    # Close the file.
    video_file.close()
    print('The times have been saved to video_times.txt')

# Call the main function.
main()