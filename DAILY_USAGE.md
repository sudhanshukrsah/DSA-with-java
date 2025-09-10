# 🚀 Daily Streak Quick Start Guide

## Simple Command for Daily Use

When you want to add a new Java program for your daily streak, just run:

```bash
./add_daily_program.sh
```

That's it! This command will:
- 📊 Find the next day number automatically
- 📝 Generate an educational Java program
- 📁 Create proper folder structure  
- ✅ Test that the code compiles
- 📤 Commit changes to git
- 🎉 Keep your GitHub streak alive!

## What Happens Next?

After running the command:

1. **Review** the generated program to learn new concepts
2. **Push to GitHub** to update your streak:
   ```bash
   git push origin main
   ```
3. **Practice** with the code to reinforce learning

## Example Daily Workflow

```bash
# Start your day
./add_daily_program.sh

# Review the code (it will be in java-dayN folder)
cd java-dayN/src
cat Main.java

# Run the program to see it work
java Main

# Push to GitHub to maintain streak
git push origin main
```

## Learning Progression

The system automatically progresses through:
- **Days 1-3**: Basic Java syntax and I/O
- **Day 4**: Variables and Data Types
- **Day 5**: Conditional Statements
- **Day 6**: Loops
- **Day 7**: Arrays
- **Day 8**: Methods and Functions
- **Day 9+**: Advanced DSA topics

## Troubleshooting

If you get any errors:

1. **Make sure you have Python 3**: `python3 --version`
2. **Make sure you have Java**: `javac -version`
3. **Check you're in the right directory**: `ls -la` should show the scripts
4. **Make the script executable**: `chmod +x add_daily_program.sh`

## Manual Alternative

If you prefer manual control:

```bash
python3 daily_streak.py        # Generate new program
python3 daily_streak.py help   # Show detailed help
```

---

**Happy coding! Keep that streak alive!** 🔥✨