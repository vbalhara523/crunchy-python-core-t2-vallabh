# File Organizer Tool

A command-line tool to organize messy folders by categorizing files into subdirectories based on their extensions.

## Usage Examples

### 1. Basic Run
Organize a folder directly. The tool will log information as files are moved:
\`\`\`bash
python main.py test_folder
\`\`\`

### 2. Dry Run
Simulate the process to safely see what would happen without actually moving any files:
\`\`\`bash
python main.py test_folder --dry-run
\`\`\`

### 3. Verbose Diagnostic Mode
Run the organizer with detailed debug logging to see exactly how files are evaluated and categorized under the hood:
\`\`\`bash
python main.py test_folder --verbose
\`\`\`

### Help Menu
View the full CLI argument details:
\`\`\`bash
python main.py --help
\`\`\`
