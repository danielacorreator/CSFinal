# **💪 Digital Personal Trainer**
#### Video Demo: [Insert URL Here]
#### Description:
The **Digital Personal Trainer** is an interactive web application designed to provide users with a personalized workout experience. This project leverages **Streamlit**, a powerful Python framework, to create a user-friendly interface where fitness enthusiasts can choose their target muscle group and receive a curated list of exercises to follow. Each exercise is accompanied by detailed information including sets, reps, rest times, intensity levels, and video tutorials to ensure users perform each exercise with proper form.

Whether you're a beginner looking to start a fitness journey or an experienced athlete trying to perfect your form, this web app serves as a digital guide to help you stay on track with your goals. By integrating motivational features and a well-organized workout structure, the app encourages consistency and performance improvement. The application is also designed with simplicity and aesthetics in mind, making it visually appealing and easy to use.

### **🔄 Key Features:**
1. **📋 Muscle Group Selection**:
   - The app allows users to select a muscle group they want to focus on, such as legs, chest, back, shoulders, arms, or core. Each muscle group has a unique set of exercises curated specifically for it.
   
2. **📋 Detailed Exercise Information**:
   - Each exercise comes with detailed information about the number of sets, reps, rest time, and the required equipment (e.g., dumbbells, barbell, or bodyweight exercises). This helps users know exactly what to do to achieve the best results.
   
3. **🎬 Exercise Tutorial Videos**:
   - Each exercise is paired with a YouTube video tutorial embedded directly into the interface. These video tutorials provide step-by-step instructions on how to perform the exercise with proper form, ensuring users minimize the risk of injury.
   
4. **📝 Personalized Workout Plans**:
   - Users can easily switch between different muscle groups to get a workout plan tailored to their fitness goals. Whether it’s strength training, hypertrophy, or endurance, the app can help with a diverse range of workout routines.
   
5. **🌟 Interactive and Dynamic User Interface**:
   - The user interface is designed to be clean, dynamic, and easy to navigate. Muscle group buttons are displayed with icons representing each area of the body (e.g., legs, chest, arms), making it intuitive for users to interact with the app.
   
6. **💡 Motivational Footer**:
   - A motivational footer encourages users to maintain proper form during exercises and reminds them that they are one step closer to achieving their fitness goals. This feature enhances the overall user experience and adds a sense of encouragement.

### **💻 Technologies Used:**
- **Streamlit**: Streamlit is a popular open-source framework that enables quick development of interactive web apps with Python. It was used to create the main interface for this project, handling everything from rendering the workout details to the interactive muscle group selection buttons.
- **JSON**: The workout data (including exercise names, sets, reps, equipment, intensity, and tutorial video URLs) is stored in a JSON file. This allows the app to easily load and display workout details dynamically.
- **YouTube iFrames**: To integrate video tutorials, YouTube iFrames are used, enabling users to watch embedded workout videos directly in the app. Each video corresponds to a specific exercise to demonstrate proper technique.
- **CSS**: Custom CSS styling is used to create a visually appealing and professional interface. The styling is applied to the exercise cards, buttons, and overall layout to ensure that the app is both functional and aesthetically pleasing.

### **🌍 User Experience:**
The app begins with a welcome screen where users can choose which muscle group they want to train. They can click on one of the muscle group icons (e.g., chest, back, arms) to load the corresponding exercises. Once a muscle group is selected, the user sees a list of exercises with the following details for each one:
- **🏅 Exercise Name**: A clear, concise title of the exercise.
- **🔢 Sets and Reps**: Information on how many sets and repetitions the user should aim for.
- **⏱️ Rest Time**: The recommended rest period between sets.
- **🛠️ Equipment Needed**: A description of the equipment required (e.g., barbell, dumbbells, or bodyweight).
- **⚡ Intensity**: The exercise intensity level (High or Medium), to help the user know how challenging the exercise is.
- **🎬 Video Tutorial**: An embedded video demonstrating how to perform the exercise correctly.

The interface is designed to be simple and user-friendly, with the most important information front and center. Each exercise is displayed in an individual card format with clear headings, making it easy for users to skim through and choose which exercise to follow next.

### **🚀 How It Works:**
1. **🔄 Initialization**:
   - When the app is opened, it loads the workout data from the `workouts.json` file. This JSON file stores all the information about the exercises grouped by muscle group.
   
2. **💪 Displaying Workouts**:
   - Based on the selected muscle group, the app dynamically filters and displays the relevant workouts. This is done using Python’s list filtering capabilities and the Streamlit framework for rendering the content.
   
3. **🎥 Displaying Videos**:
   - Each exercise includes a link to a YouTube video. These links are embedded within an `iframe` HTML tag, allowing the videos to play directly in the app.

4. **🖱️ User Interaction**:
   - Users can click on the buttons corresponding to the different muscle groups. As soon as a button is clicked, the app updates the display to show the exercises for that particular muscle group.
   
5. **🎨 Visual Styling**:
   - The app’s aesthetic is enhanced with custom CSS, which styles everything from the layout to the individual exercise cards. The video containers are styled to fit within the card, and the app also uses gradient text effects to make the titles stand out.

### **🏁 Conclusion:**
The **Digital Personal Trainer** is a comprehensive and interactive tool for anyone looking to improve their fitness. By offering detailed workout plans, tutorial videos, and a simple user interface, this app is perfect for individuals at any fitness level who want to achieve their goals in a safe, effective, and motivating way. Whether you're new to exercise or looking for fresh ideas for your workout routine, this app has everything you need to get started on your fitness journey.
