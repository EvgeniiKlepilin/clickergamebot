# Holiday City: Reloaded Bot

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Game](https://img.shields.io/badge/game-Holiday%20City%3A%20Reloaded-orange.svg)

A Python automation bot for the idle clicker game "Holiday City: Reloaded" on Steam. This bot automates gameplay by purchasing businesses, upgrades, and city facilities to maximize your city's growth and earnings.

## Features

- **Automated Business Management**: Automatically purchases available businesses (boutique, cafe, burger house, night club, hotel, and resource buildings)
- **Smart Upgrades**: Automatically buys upgrades when available to boost efficiency
- **City Development**: Manages city facilities including material, energy, and food production
- **Advanced Features**: Handles atomic lab and port purchases for late-game progression
- **Screen Detection**: Uses pixel color detection to determine when purchases are available
- **Continuous Operation**: Runs indefinitely to maximize idle gains

## Requirements

- Python 3.6+
- Windows OS (uses win32api for mouse control)
- Steam with "Holiday City: Reloaded" installed
- Screen resolution: 1366x768 (configurable)

## Dependencies

```bash
pip install pillow numpy pywin32
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/clickergamebot.git
   cd clickergamebot
   ```

2. Install required dependencies:
   ```bash
   pip install pillow numpy pywin32
   ```

3. Launch "Holiday City: Reloaded" on Steam
4. Position the game window to take up half the screen (left side)

## Usage

### Running the Bot

```bash
python holiday_city_bot.py
```

The bot will automatically:
1. Start the game in muted mode
2. Skip offline earnings dialog
3. Set purchase mode to "buy max"
4. Begin the automated purchasing cycle

### Screenshot Tool

Use the screenshot tool to capture game states for debugging:

```bash
python game_screenshot_tool.pyw
```

### Configuration

The bot is configured for a specific screen resolution and game positioning:
- **Resolution**: 1366x768
- **Game Position**: Left half of screen
- **Padding**: x_pad = 7, y_pad = 186

To adjust for different setups, modify the `x_pad` and `y_pad` values in the script.

## How It Works

The bot uses computer vision techniques to:

1. **Screen Capture**: Takes screenshots of the game area using PIL's ImageGrab
2. **Color Detection**: Checks specific pixel colors to determine if purchases are available
3. **Mouse Automation**: Uses win32api to simulate mouse clicks at predetermined coordinates
4. **Automation Loop**: Continuously cycles through purchasing businesses, upgrades, and facilities

## Game Elements Automated

### Businesses
- Boutique
- Cafe
- Burger House
- Night Club
- Hotel
- Material Factory
- Energy Plant
- Food Factory
- Iron Mine
- Technology Center

### Management Areas
- Upgrades
- City Facilities (Material, Energy, Food)
- Atomic Lab
- Port
- Airport (coordinates available)
- Office (coordinates available)

## Disclaimer

This bot is for educational purposes and personal use only. Use at your own risk and in accordance with Steam's Terms of Service. The author is not responsible for any consequences of using this automation tool.

## Credits

This project is based on the excellent tutorial by Chris Kiehl: [How to Build a Python Bot That Can Play Web Games](https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
