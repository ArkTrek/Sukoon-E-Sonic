# Sukoon-E-Sonic

## Overview
- Sukoon-E-Sonic is an interactive quiz application designed to engage users in a fun and educational manner. 
- This is used to learn the cognitive behavioural thinking (CBT) capacity of a person based on their responses.
- Leveraging the power of OpenAI's GPT for generating questions, this app provides a unique experience centered around emotional well-being. 

---

## Features
- Interactive quiz with multiple-choice questions
- Real-time scoring and feedback
- Audio integration using Pygame for a lively experience
- User session management with Flask
- Responsive design for various devices

---
## Index Page (Design)

![Page Look](https://github.com/user-attachments/assets/169d6034-cbdb-4383-a568-c67a20d8598b)


## CBT Page
![CBT Page](https://github.com/user-attachments/assets/a19dc681-1f5f-4fb2-a6c9-713901388d9a)


## Result Page
![resultPage](https://github.com/user-attachments/assets/26b5ada0-c67f-434d-a91e-ddebb29a7aa7)


---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ArkTrek/Sukoon-E-Sonic.git
   cd Sukoon-E-Sonic
   ```
---

## Usage
- Create a virtual environment using python or anaconda and install the necessary libraries.
- Run the command "python app.py".
- Open your browser and navigate to http://127.0.0.1:5000/ to access the quiz.
- Follow the prompts to answer questions and receive feedback.

---

**Note:**
- The "vid.py" file is able to combine a gif file with an audio file to generate a video file. Use it as needed.
- If the gif holds a transparent bg, it will get overwritten by a white background during encoding.
- The duration of the video file will be determined by the length of the audio file.
- If the audio is making too much noise, just cut the source. Closing the browser won't stop the audio from playing - Cancel the command "python app.py"

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for discussion.
