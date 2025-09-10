# DSA with Java - Daily Coding Streak 🚀

Welcome to the **DSA with Java** repository! This project is designed to help you build a consistent daily coding habit while learning Data Structures and Algorithms with Java.

## 🎯 Purpose

This repository maintains a daily coding streak by automatically generating educational Java programs that cover:
- Core Java programming concepts
- Data Structures and Algorithms (DSA)
- Problem-solving skills
- Best coding practices

## 🏗️ Repository Structure

```
DSA-with-java/
├── java-day1.iml          # IntelliJ project file for Day 1
├── java-day2.iml          # IntelliJ project file for Day 2  
├── java-day3/             # Day 3 Java program
│   ├── src/Main.java
│   └── README.md
├── src/Main.java          # Early Java program
├── daily_streak.py        # Automation script for daily programs
├── add_daily_program.sh   # Simple command interface
└── README.md              # This file
```

## 🚀 Quick Start - Daily Streak

To add a new Java program for your daily streak, simply run:

```bash
# Make sure you're in the repository root
./add_daily_program.sh
```

Or manually with Python:

```bash
python3 daily_streak.py
```

This will automatically:
1. 📊 Determine the next day number
2. 📝 Generate an educational Java program
3. 📁 Create proper folder structure
4. ✅ Test compilation
5. 📤 Commit changes to git

## 📚 Learning Path

The daily programs follow a structured learning path:

| Day | Topic | Concepts Covered |
|-----|-------|------------------|
| 1-3 | Basics | Input/Output, Basic syntax |
| 4 | Variables & Data Types | All Java data types, type casting |
| 5 | Conditional Statements | if-else, switch, ternary operator |
| 6 | Loops | for, while, do-while loops |
| 7 | Arrays | Array operations, searching, sorting |
| 8 | Methods | Functions, recursion, parameters |
| 9+ | Advanced Topics | OOP, Collections, DSA concepts |

## 🛠️ Manual Usage

If you prefer to create programs manually:

1. **Create a new day folder:**
   ```bash
   mkdir java-day{N}
   mkdir java-day{N}/src
   ```

2. **Write your Java program:**
   ```bash
   # Create src/Main.java with your code
   ```

3. **Test compilation:**
   ```bash
   cd java-day{N}/src
   javac Main.java
   java Main
   ```

4. **Commit your work:**
   ```bash
   git add java-day{N}
   git commit -m "Add Day {N}: Your Topic"
   git push origin main
   ```

## 📋 Requirements

- **Java JDK 8 or higher**
- **Python 3** (for automation script)
- **Git** (for version control)

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sudhanshukrsah/DSA-with-java.git
   cd DSA-with-java
   ```

2. **Make the script executable:**
   ```bash
   chmod +x add_daily_program.sh
   ```

3. **Start your daily streak:**
   ```bash
   ./add_daily_program.sh
   ```

## 🎮 How to Use the Automation

### Command: "Add one Java program and push code"

When you want to continue your streak, just run:

```bash
./add_daily_program.sh
```

The script will:
- Generate a new educational Java program
- Create appropriate folder structure
- Test that the code compiles
- Commit changes with a meaningful message
- Remind you to push to GitHub

### After running the automation:

1. **Review the generated code** to understand the concepts
2. **Push to GitHub** to maintain your streak:
   ```bash
   git push origin main
   ```
3. **Practice and modify** the code to reinforce learning

## 📊 Tracking Your Progress

- Each day's program is in its own folder (`java-day{N}`)
- Every folder has a README explaining the day's concepts
- Commit messages clearly indicate what was learned
- GitHub will show your green contribution squares! 🟢

## 🎨 Customization

You can customize the automation by editing `daily_streak.py`:

- **Add new topics** to the `_get_java_program_content()` method
- **Modify program templates** to match your learning style
- **Change folder structure** if needed
- **Add additional file types** (like test files)

## 🤝 Contributing

Feel free to:
- **Suggest new topics** for the daily programs
- **Improve the automation script**
- **Share your own Java programs**
- **Report bugs or issues**

## 📈 Benefits

✅ **Consistent coding practice** - Build the habit  
✅ **Structured learning** - Progressive difficulty  
✅ **GitHub streak** - Visual motivation  
✅ **Real projects** - Practical Java skills  
✅ **Automated workflow** - Focus on learning, not setup  

## 🏆 Goals

- 🎯 **100-day coding streak**
- 📚 **Master Java fundamentals**
- 🧠 **Learn core DSA concepts**
- 💼 **Build a strong GitHub portfolio**

## 📝 License

This project is for educational purposes. Feel free to use, modify, and share!

---

**Start your journey today!** 🌟

```bash
./add_daily_program.sh
```

*Happy coding and keep the streak alive!* 🔥
