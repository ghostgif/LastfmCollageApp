# LastfmCollageApp
Last.fmCollageApp

# Album Collage Generator - READ ME

## Project Title:
Album Collage Generator

## Project Description:
In today’s digital age, music streaming platforms have become the central hub for discovering and enjoying music, but many of these platforms, including Last.fm, only provide basic listening history without much in the way of visual representation. While tracking listening habits can be informative, it can also be a bit dry and impersonal. That’s where the Album Collage Generator comes in; a unique tool designed to give users a fun, creative, and shareable way to display their top albums, track trends over time, and share their musical tastes with the world. This project is not just about displaying numbers; it’s about turning raw listening data into a visually compelling story that users can interact with and share with their social circles.

The Album Collage Generator fetches data from Last.fm, a service that tracks users’ listening habits, and turns that information into stunning visual collages made from the album artwork of the most played albums over a defined time range. Users can select time periods like the past week, month, or year, and choose from grid layouts (3x3, 4x4, or 5x5) to generate the collage. This allows users to reflect on their favorite albums and provides them with a unique, shareable visual representation of their listening habits. Whether it’s to showcase their favorite music or just to admire their own music history, this project makes the process enjoyable and easy.

The primary focus of this project is to fill a gap in how Last.fm presents listening trends. Many users enjoy looking back at their listening history, but there is no built-in tool for visualizing that data in a format that’s engaging and easy to share. The Album Collage Generator transforms listening history into art by providing a quick and intuitive way to generate a collage and export it. The app gives users the ability to view, save, and share a visual of their music preferences, making it perfect for social media users and music enthusiasts who want to share their musical journeys. 

The application is built with the user experience in mind—easy to use, minimalistic, and functional. The focus is on providing a smooth and intuitive experience where users simply enter their Last.fm username, select a time range, and generate their album collage. By creating this tool, we are not only giving music lovers a way to share their music history, but also providing a fun and creative outlet for them to explore their listening habits in a visually meaningful way. Whether you're a casual listener or a hardcore music aficionado, this app will help you visualize and celebrate your music preferences with ease.

## Team Name and Mission:

### Team Name:
TrackStats

### Mission:
Our mission is to help music lovers visualize and share their listening habits through personalized album collages. We aim to make music data more accessible, interactive, and visually engaging, allowing users to turn their listening history into a shareable work of art.

## Team Members:
- **Billy Dickey** – Lead Developer – williamrdickey@lewisu.edu
    - *Qualifications:* I am qualified to take on this role because I have experience with Python programming, GUI development, and working with APIs. This project aligns with my passion for music and the desire to create something that’s both fun and useful for other music enthusiasts.

## Project Pitch:
In today’s digital world, music streaming platforms are central to our entertainment, but visualizing listening habits is often a cumbersome task. The Album Collage Generator bridges this gap by turning Last.fm data into visual collages, allowing users to track and reflect on their music trends in a fun and engaging way. With this project, users can see a visual representation of their most played albums over time and even share those representations with their friends or on social media. By simply selecting their Last.fm username and a desired time range (week, month, year), users can generate a personalized collage of their listening history. The project fills a major gap by transforming otherwise static data into shareable and interactive visual content.

## Users:
- **Music Enthusiasts**: People who want to track and reflect on their music history.
- **Social Media Users**: Music lovers who want to share their listening habits with friends or followers.
- **Music Fans**: Those interested in comparing their listening trends over time.

## List of Features:
- **Customizable Collages**: Users can generate album collages in 3x3, 4x4, or 5x5 grids, depending on the number of albums they wish to showcase.
- **Time Range Selection**: Users can select a time range (1 week, 1 month, 3 months, 6 months, 12 months) to filter their listening data and generate collages based on specific timeframes.
- **Album Info Display**: Display a simple, clean list of album information such as album title, artist, and playcount.
- **Save and Share Collage**: Users can download the collage image to share on social media or use it for personal enjoyment.
- **Dynamic Collage Generation**: As more albums are played, the collage updates dynamically, giving a fresh look at the user’s listening trends.
- **Music Stats Visualization**: Collages act as a visual summary of music statistics, allowing users to compare their favorites across time.

## Modality:
The Album Collage Generator is a desktop application, specifically designed to run on Windows. It uses a graphical user interface (GUI) built with Tkinter and integrates with Last.fm API to fetch user data. The user can easily view and save the generated album collage, making the app a straightforward and practical tool for music lovers.

## Technologies:
- **Programming Language**: Python
- **Frameworks and Libraries**:
    - Tkinter: Used for creating the desktop GUI.
    - PIL (Pillow): Used for image processing (resizing, collage generation).
    - Requests: Used to make HTTP requests for fetching album data from Last.fm.
- **API Integration**: Last.fm API to fetch album information and listening data.
- **Data Storage**: Local storage of images and generated collage files.

## Data:
- **Data Source**: The project fetches user listening data from the Last.fm API, which includes album names, artist names, playcounts, and album artwork.
- **Local Data Storage**: Collage images are temporarily stored on the local machine to allow for saving and sharing.
- **Data Privacy**: The project does not store any personal data externally. User data is fetched on-demand from Last.fm, and users’ listening data stays private.

## Convincing Explanation of the Project’s Value:
This project adds immense value to music lovers and social media users by transforming boring data into a visually captivating format. Last.fm tracks listening habits, but users don’t have a way to visualize their music history. This tool solves that problem by providing a way to track trends, generate customized collages, and share them with others. It makes music data more engaging, fun, and interactive.

## Skills Required:
- **Python Programming**: Knowledge of Python, including working with APIs, image processing, and GUI design.
- **GUI Design with Tkinter**: Familiarity with Tkinter for building user interfaces in Python.
- **API Integration**: Experience with integrating third-party APIs (specifically the Last.fm API) to fetch data.
- **Image Processing**: Working with Pillow (PIL) for manipulating images (resizing, creating collages).
- **Debugging and Testing**: Ability to identify and fix bugs, and to ensure smooth functionality of the app.

## Realistic Estimate of Personnel Requirements:
- **1 Backend Developer**: Responsible for fetching and processing data from the Last.fm API, handling errors, and managing image processing.
- **1 Frontend Developer**: Responsible for building and maintaining the graphical user interface (GUI).
- **1 Tester/QA Specialist**: Responsible for testing and debugging the application, ensuring that the collage is generated correctly and all features work as expected.
  
## Challenges & Considerations:
- **API Rate Limits**: The Last.fm API may have rate limits, and handling this efficiently will be essential to avoid overloading the server.
- **User Authentication**: Ensuring a smooth authentication process for fetching Last.fm data securely.
- **Error Handling**: Dealing with potential errors in fetching data (e.g., missing album artwork) will need to be handled gracefully.

## Other Features:
- **Dark Mode**: The option to toggle between light and dark themes for the interface.
- **Advanced Collage Layouts**: Future updates could allow for even more collage layouts, such as custom-sized grids.
- **Monthly Summary Emails**: "Here’s what you listened to most in January!"
