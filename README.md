# SideProjects
A repository containing all my side projects, completed and uncompleted. To showcase my progress and experiences as I overcome old challenges in code

Here’s an expanded list of the projects with the languages, libraries, frameworks, and processes required to complete them for each programming language. 

---

### **Python**

#### Beginner
1. **To-Do List App**
   - **Languages/Tools**: Python, basic text files or SQLite.
   - **Process**:
     1. Take user input for tasks.
     2. Store tasks in a list or database.
     3. Provide options to add, remove, or mark tasks as done.
   - **Libraries/Frameworks**: `sqlite3` for database.

2. **Number Guessing Game**
   - **Languages/Tools**: Python.
   - **Process**:
     1. Generate a random number using `random`.
     2. Take user input and compare guesses.
     3. Provide hints (e.g., higher/lower).
   - **Libraries/Frameworks**: `random`.

#### Intermediate
3. **Web Scraper**
   - **Languages/Tools**: Python, HTML parsing.
   - **Process**:
     1. Identify a target website and inspect its HTML structure.
     2. Use `requests` to fetch the webpage and `BeautifulSoup` to parse the data.
     3. Save the extracted data to a file or database.
   - **Libraries/Frameworks**: `requests`, `BeautifulSoup`, `pandas`.

4. **Weather App**
   - **Languages/Tools**: Python, API integration.
   - **Process**:
     1. Get an API key from OpenWeatherMap.
     2. Fetch weather data using `requests`.
     3. Parse and display the data in a user-friendly way.
   - **Libraries/Frameworks**: `requests`, `json`.

#### Advanced
5. **Chatbot**
   - **Languages/Tools**: Python, AI/ML.
   - **Process**:
     1. Use a library like ChatterBot or integrate GPT models.
     2. Train or customize the chatbot with specific intents or datasets.
     3. Create a conversational interface.
   - **Libraries/Frameworks**: `ChatterBot`, `transformers`.

6. **Stock Market Analysis Tool**
   - **Languages/Tools**: Python, data visualization.
   - **Process**:
     1. Use an API like Yahoo Finance to fetch data.
     2. Perform data analysis (moving averages, trends).
     3. Visualize data using Matplotlib or Plotly.
   - **Libraries/Frameworks**: `yfinance`, `pandas`, `matplotlib`.

---

### **Rust**

#### Beginner
1. **Command-Line Calculator**
   - **Languages/Tools**: Rust.
   - **Process**:
     1. Accept user input using `std::io`.
     2. Parse the input and perform basic arithmetic operations.
   - **Libraries/Frameworks**: None (standard library).

2. **File Organizer**
   - **Languages/Tools**: Rust, filesystem handling.
   - **Process**:
     1. Use `std::fs` to read directory contents.
     2. Categorize files by extension.
     3. Move files into folders using `std::fs::rename`.
   - **Libraries/Frameworks**: None.

#### Intermediate
3. **HTTP Server**
   - **Languages/Tools**: Rust, networking.
   - **Process**:
     1. Use a library like `hyper` to handle HTTP requests.
     2. Parse incoming requests and send responses.
     3. Add routing for basic endpoints.
   - **Libraries/Frameworks**: `hyper`, `tokio`.

4. **Tic-Tac-Toe Game**
   - **Languages/Tools**: Rust.
   - **Process**:
     1. Create a 3x3 grid and update the game state.
     2. Implement a basic AI or two-player mode.
     3. Handle win/loss/draw conditions.
   - **Libraries/Frameworks**: None (standard library).

#### Advanced
5. **Web Crawler**
   - **Languages/Tools**: Rust, HTML parsing.
   - **Process**:
     1. Fetch web pages using `reqwest`.
     2. Parse HTML using `select.rs` or `html5ever`.
     3. Store or process extracted links and content.
   - **Libraries/Frameworks**: `reqwest`, `html5ever`.

6. **Database Engine**
   - **Languages/Tools**: Rust, data storage.
   - **Process**:
     1. Implement data structures to store records.
     2. Add support for basic queries (e.g., SELECT, INSERT).
     3. Optimize storage and retrieval mechanisms.
   - **Libraries/Frameworks**: None.

---

### **Java**

#### Beginner
1. **BMI Calculator**
   - **Languages/Tools**: Java.
   - **Process**:
     1. Accept height and weight as input.
     2. Calculate BMI using a formula.
     3. Display the result and categorize (underweight, normal, overweight).
   - **Libraries/Frameworks**: None.

2. **Student Grading System**
   - **Languages/Tools**: Java.
   - **Process**:
     1. Accept student scores and calculate averages.
     2. Assign grades based on predefined ranges.
   - **Libraries/Frameworks**: None.

#### Intermediate
3. **Library Management System**
   - **Languages/Tools**: Java, database.
   - **Process**:
     1. Set up a database (e.g., MySQL).
     2. Create CRUD operations for books and users.
     3. Add borrowing/return functionality.
   - **Libraries/Frameworks**: JDBC, MySQL.

4. **Currency Converter**
   - **Languages/Tools**: Java, GUI.
   - **Process**:
     1. Use an API to fetch exchange rates.
     2. Build a GUI using JavaFX for input and output.
   - **Libraries/Frameworks**: JavaFX, `HttpURLConnection`.

#### Advanced
5. **Social Media App**
   - **Languages/Tools**: Java, backend.
   - **Process**:
     1. Implement user authentication and profiles.
     2. Enable posting, liking, and commenting.
     3. Use a database to store user data and posts.
   - **Libraries/Frameworks**: Spring Boot, Hibernate.

6. **E-commerce System**
   - **Languages/Tools**: Java, web development.
   - **Process**:
     1. Create a backend to handle products, users, and orders.
     2. Implement authentication and a shopping cart.
     3. Add a frontend or REST API.
   - **Libraries/Frameworks**: Spring Boot, Hibernate.

---

### **JavaScript**

#### Beginner
1. **Countdown Timer**
   - **Languages/Tools**: JavaScript, HTML, CSS.
   - **Process**:
     1. Create a simple HTML form for input.
     2. Use `setInterval` to update the countdown.
   - **Libraries/Frameworks**: None.

2. **Trivia Quiz**
   - **Languages/Tools**: JavaScript, HTML, CSS.
   - **Process**:
     1. Display questions and collect user input.
     2. Provide feedback for correct/incorrect answers.
   - **Libraries/Frameworks**: None.

#### Intermediate
3. **Weather Dashboard**
   - **Languages/Tools**: JavaScript, API.
   - **Process**:
     1. Fetch weather data using `fetch` and an API.
     2. Display data dynamically in the DOM.
   - **Libraries/Frameworks**: None.

4. **Personal Budget Tracker**
   - **Languages/Tools**: JavaScript.
   - **Process**:
     1. Collect income and expense data.
     2. Display totals and charts using a library.
   - **Libraries/Frameworks**: Chart.js.

#### Advanced
5. **Real-Time Chat App**
   - **Languages/Tools**: JavaScript, WebSocket.
   - **Process**:
     1. Set up a server using Node.js or Firebase.
     2. Enable real-time messaging with WebSocket.
   - **Libraries/Frameworks**: Socket.IO.

6. **Task Management Tool**
   - **Languages/Tools**: JavaScript, drag-and-drop.
   - **Process**:
     1. Create a drag-and-drop interface.
     2. Store tasks in local storage or a database.
   - **Libraries/Frameworks**: React, `react-beautiful-dnd`.

---

### **C++**

#### Beginner
1. **Banking Application**
   - **Languages/Tools**: C++.
   - **Process**:
     1. Store user accounts in a file or data structure.
     2. Add functionality for deposits, withdrawals, and balance checks.
   - **Libraries/Frameworks**: None.

2. **Maze Generator**
   - **Languages/Tools**: C++.
   - **Process**:
     1. Use algorithms like Depth-First Search to generate mazes.
     2. Display the maze using console graphics or ASCII art.
   - **Libraries/Frameworks**: None.

#### Intermediate
3. **Game: Snake**
   - **Languages/Tools**: C++, graphics library.
   - **Process**:
     1. Use a game loop to control movement.
     2. Handle collision detection and scorekeeping.
   - **Libraries/Frameworks**: SFML.

4. **Text-Based RPG**
   - **Languages/Tools**: C++.
   - **Process**:
     1. Implement characters and stats.
     2. Add combat mechanics with randomization.
   - **Libraries/Frameworks**: None.

#### Advanced
5. **Physics Simulation**
   - **Languages/Tools**: C++.
   - **Process**:
     1. Implement a physics engine for collisions and forces.
     2. Use a graphics library to visualize results.
   - **Libraries/Frameworks**: SFML, OpenGL.

6. **Compiler**
   - **Languages/Tools**: C++.
   - **Process**:
     1. Tokenize source code input.
     2. Parse tokens into an Abstract Syntax Tree (AST).
     3. Generate basic machine code or bytecode.
   - **Libraries/Frameworks**: None.

---

Let me know if you'd like a detailed explanation of any project!