# WeatherVista

WeatherVista is a comprehensive weather dashboard application built using Python. It fetches weather data from the OpenWeatherMap API and displays it in a user-friendly graphical interface. The project aims to provide an educational tool for learning about APIs, data processing, and graphical user interfaces in Python.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Fetches current weather data, 3-hourly forecast, and 5-day forecast from OpenWeatherMap API.
- Displays data in a graphical user interface using Tkinter.
- Provides visualizations of weather data including temperature trends, humidity levels, and more.
- Step-by-step code and explanations in Jupyter notebooks for educational purposes.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/teaching-repositories/weathervista.git
    cd weathervista
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

2. Create a `.env` file in the root directory of the project and add your API key:
    ```plaintext
    OPENWEATHER_API_KEY=your_api_key_here
    ```

3. Run the application:
    ```bash
    python main.py
    ```

## Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
