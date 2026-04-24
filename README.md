# AI Nutrition Coach

A smart, context-aware web application that acts as your personal nutrition coach, helping you make better food choices and build healthy eating habits. Built for the Prompt-a-thon Challenge.

## 🎯 Project Description
The AI Nutrition Coach doesn't just track your food; it understands context, identifies unhealthy patterns, and provides actionable, practical alternatives based on your personal profile (age, weight, goals, dietary preferences) and the time of day. 

For instance, if you log a burger late at night, the AI will not only point out the high calories but also recognize the context (late night) and suggest lighter alternatives like herbal tea or nuts, keeping in mind if you've already had junk food recently.

## ✨ Features
- **Smart Nutritional Analysis:** Leverages Google Gemini to evaluate the nutritional quality of your meals.
- **Context-Aware Recommendations:** Adjusts suggestions based on time of day (e.g., protein-rich for breakfast, light meals for dinner).
- **Behavior & Pattern Tracking:** Detects repeated junk food consumption and gently corrects course.
- **Personalized Coaching:** Tailors advice based on user goals (weight loss, muscle gain) and diet (veg, vegan, non-veg).
- **Health Score:** Quantifies each meal with a score from 0-10.
- **Beautiful UI:** A clean, responsive, professional interface that works on desktop and mobile.

## 🛠 Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (Custom Design System), Vanilla JS
- **AI Integration:** Google Gemini API (`google-generativeai`)
- **Storage:** Local JSON file for easy deployment (No external DB required)

## 🚀 How to Run

1. **Clone the repository** (or navigate to the project folder)

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Google Gemini API Key**
   - Windows (Command Prompt):
     ```cmd
     set GOOGLE_API_KEY=your_api_key_here
     ```
   - Windows (PowerShell):
     ```powershell
     $env:GOOGLE_API_KEY="your_api_key_here"
     ```
   - Mac/Linux:
     ```bash
     export GOOGLE_API_KEY="your_api_key_here"
     ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in Browser**
   Go to `http://127.0.0.1:5000`

## 🧠 Example Prompts & AI Reasoning

The system uses contextual prompting behind the scenes. Example prompt structure:
> "User Profile: Age 25, Weight 70kg, Goal: Weight Loss, Time: 22:00. Recent meals: Pizza (Score: 4). User ate: 'Burger and fries'. Analyze quality, detect patterns, provide score, and suggest context-aware alternatives."

**Sample Response:**
> "Since it's late and you already had pizza earlier today, a burger and fries is quite heavy and calorie-dense for your weight loss goals. Let's aim for something lighter before bed. If you're still hungry, try a lettuce wrap burger or just some herbal tea with a handful of nuts to settle your stomach."

## 📜 Assumptions & Constraints
- Assumes a local environment for ease of testing.
- Uses JSON storage to meet the criteria of "No external dependencies (or minimal)" and keeping it under 1MB.
- A fallback logic is provided just in case the Gemini API key is missing.