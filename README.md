# 📈 Stock Ticker Game

A multiplayer stock market trading game built with Python and Pygame based on the classic stock ticker board game. Watch stock prices fluctuate in real-time, buy and sell shares, collect dividends, and compete with up to 10 players to build the highest net worth!

## ✨ Features

- **👥 Multiplayer Support**: Play with 2-10 players locally
- **📊 Dynamic Stock Market**: Six different stocks (Gold, Silver, Oil, Industrial, Bonds, Grain) with real-time price changes
- **📉 Live Price Charts**: Visual graph showing stock price movements over time
- **🎲 Market Events**:  
  - Stock splits when prices reach $200
  - Market crashes when prices hit $0
  - Dividend payments for profitable stocks
- **⚡ Trading Controls**: Quick buy/sell options for efficient trading
- **💾 Save/Load System**: Save your game progress and resume later
- **🔮 Futures Trading Mode**: Optional advanced mode allowing short selling
- **📰 Scrolling Ticker**: Classic stock ticker display showing market events

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Required Dependencies

Install the required packages using pip: 

```bash
pip install pygame
pip install pygame-menu
```

### Setup

1. Clone this repository: 
```bash
git clone https://github.com/OliverLazar/Stock-Ticker-Game.git
cd Stock-Ticker-Game
```

2. Run the game:
```bash
python Menu.py
```

## 🎮 How to Play

### Game Setup

1. Launch the game by running `Menu.py`
2. Configure your game settings: 
   - Set the number of players (1-10)
   - Customize player names
   - Enable/disable Futures Trading
3. Click "Play" to start a new game or "Load from Save" to continue a previous game

### Game Controls

#### Navigation
- **Arrow Keys (↑↓←→)**: Navigate through the trading grid
- Current selection is highlighted with a colored border

#### Trading Actions
- **= (Equals)**: Buy 500 shares of the selected stock
- **- (Minus)**: Sell 500 shares of the selected stock
- **[ (Left Bracket)**: Sell ALL shares of the selected stock
- **] (Right Bracket)**: Buy maximum possible shares (based on available cash)

#### Market Controls
- **SPACE**: Toggle market open/closed
  - Market CLOSED: Place trades, view prices
  - Market OPEN:  Watch prices change in real-time (no trading)

#### Game Management
- **ENTER**: Add a new player (up to 10 total)
- **TAB**: Confirm player name when adding new player
- **s**: Save the current game state

### Starting Conditions

Each player begins with:
- **$5,000 cash**
- **$5,000 net worth**
- **0 shares** of all stocks

All stocks start at **$100** per share. 

### Market Mechanics

#### Price Changes
When the market is open: 
- Random stock is selected
- Event occurs: Up, Down, or Dividend (Div)
- Change amount: 5, 10, or 20 points
- Prices update in real-time on the chart

#### Special Events

**Stock Split** (Price reaches $200):
- Price resets to $100
- All players' shares of that stock **double**
- Great opportunity if you bought low!

**Market Crash** (Price hits $0):
- Price resets to $100
- All shares of that stock become **worthless** (reset to 0)
- Devastating for heavily invested players

**Dividends** (Div event when price ≥ $100):
- Players receive cash based on shares owned
- Formula: (shares × dividend_amount / 100)
- Marked with circles on the price chart

### Winning the Game

- The player with the highest **net worth** wins
- Net worth = Cash + (Total value of all stock holdings)
- Net worth is calculated when market closes
- Players are automatically ranked by net worth

## 📁 File Structure

- **Menu.py**: Main menu interface and game launcher
- **Stockticker.py**: Core game logic and gameplay loop
- **player.py**: Player class definition
- **Stocks.py**: Stock-related utilities
- **Menu_old.py**: Previous version of menu (legacy)

## 🖥️ Game Interface

### Trading Grid
The bottom portion shows a table with:
- **Player names** (leftmost column)
- **Stock holdings** for each of 6 stocks
- **Cash** on hand
- **Net Worth** (total value)

### Price Chart
The upper portion displays:
- Real-time line graph of all 6 stock prices
- Different color for each stock
- White circles indicate dividend payments
- X-axis shows time progression

### Ticker Crawl
The middle section shows:
- Current market events scrolling right to left
- Stock prices when market is closed
- Instructions when market is closed
- Current time display

## 💾 Save System

### Saving a Game
1. Press **s** during gameplay
2. Choose save location via file dialog
3. Game saves as CSV file

### Loading a Game
1. Select "Load from Save" from main menu
2. Choose your CSV save file
3. Game state fully restored: 
   - All player data (cash, stocks, net worth)
   - Current stock prices
   - Player count and settings

## 🔮 Futures Trading Mode

When enabled in settings:
- Allows **short selling** (selling stocks you don't own)
- Players can have negative stock positions
- Risk:  Unlimited losses if price rises
- Reward: Profit when prices fall
- Advanced feature for experienced players
- **Manage risk**: Keep some cash on hand for opportunities

## 📄 License

This project is open source and available for personal and educational use.
