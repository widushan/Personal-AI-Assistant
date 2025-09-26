# Personal AI Assistant 🤖

Creating a Real Life Personal Ai Assistant | Python 🐍

A sophisticated AI-powered personal assistant built with Python, featuring voice recognition, text-to-speech, real-time search capabilities, and a modern GUI interface.

## 🌟 Features

- **Voice Recognition**: Real-time speech-to-text conversion
- **Text-to-Speech**: Natural voice responses
- **Real-time Search**: Web search capabilities for up-to-date information
- **Image Generation**: AI-powered image creation
- **Modern GUI**: Beautiful PyQt5-based interface with dark theme
- **Chat Interface**: Interactive conversation with message history
- **Automation**: Task automation capabilities
- **Multi-modal**: Support for text, voice, and image interactions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Windows 10/11 (recommended)
- Microphone and speakers

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Personal-AI-Assistant.git
   cd Personal-AI-Assistant
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your API keys and configuration:
   ```env
   Assistantname=Zyra
   # Add other API keys as needed
   ```

5. **Run the application**
   ```bash
   python Main.py
   ```

## Screenshots

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/815aa7e9-2609-4a3d-92be-dfa176e60ee1" />

<img width="1908" height="1040" alt="Image" src="https://github.com/user-attachments/assets/55197b03-2411-479b-90d0-f5b372b214f9" />

## 📁 Project Structure

```
Personal-AI-Assistant/
├── Backend/                 # Core AI functionality
│   ├── Chatbot.py          # Main chatbot logic
│   ├── SpeechToText.py     # Voice recognition
│   ├── TextToSpeech.py     # Voice synthesis
│   ├── ImageGeneration.py  # AI image creation
│   ├── RealtimeSearchEngine.py  # Web search
│   ├── Automation.py       # Task automation
│   └── Model.py            # AI model management
├── Frontend/               # User interface
│   ├── GUI.py             # PyQt5 GUI implementation
│   ├── Graphics/          # UI assets and icons
│   └── Files/             # Temporary data files
├── Data/                  # Application data
├── Main.py               # Application entry point
└── requirements.txt      # Python dependencies
```

## 🎯 Usage

### Voice Commands
- Click the microphone icon to start voice interaction
- Speak naturally - the assistant will process and respond
- Use voice commands for hands-free operation

### Chat Interface
- Switch to Chat tab for text-based conversations
- View conversation history
- Send messages and receive AI responses

### Features Available
- **General Questions**: Ask about any topic
- **Web Search**: Get real-time information
- **Image Generation**: Create AI-generated images
- **Task Automation**: Automate repetitive tasks
- **Voice Interaction**: Natural conversation

## 🛠️ Configuration

### Environment Variables
Create a `.env` file with the following variables:
```env
Assistantname=Zyra
# Add your API keys here
```

### Customization
- Modify `Assistantname` in `.env` to change the assistant's name
- Customize the GUI appearance in `Frontend/GUI.py`
- Add new features in the `Backend/` directory

## 📦 Dependencies

Key dependencies include:
- `PyQt5` - GUI framework
- `speech_recognition` - Voice recognition
- `pyttsx3` - Text-to-speech
- `requests` - Web requests
- `python-dotenv` - Environment variables

See `requirements.txt` for the complete list.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for AI capabilities
- PyQt5 community for GUI framework
- Python community for excellent libraries
- All contributors and testers

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/widushan/Personal-AI-Assistant/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## 🔗 Links

- **Repository**: [GitHub - Personal AI Assistant](https://github.com/widushan/Personal-AI-Assistant)
- **Documentation**: [Wiki](https://github.com/widushan/Personal-AI-Assistant/wiki)
- **Issues**: [Report Issues](https://github.com/widushan/Personal-AI-Assistant/issues)

---

**Made with ❤️ by [widushan]**

*Creating the future of personal AI assistance, one conversation at a time.*