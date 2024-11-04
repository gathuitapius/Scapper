# Car Scraper & Viewer

A Flask application that scrapes car listings from Jiji Kenya, stores them in a MySQL database, and displays them on a web interface. The application provides an interface for viewing all car listings, filtering based on price, and viewing individual car details.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)

## Features
- Scrapes car listings from [Jiji Kenya](https://jiji.co.ke/)
- Stores car data (image, name, price) in a MySQL database
- Provides a web interface for viewing and filtering car listings
- Offers individual car detail pages
- Saves scraped data directly into a MySQL database, checking for duplicates

## Requirements
- Python 3.x
- Flask
- BeautifulSoup (bs4)
- Requests
- MySQL (MySQL Server and MySQL Connector for Python)

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/gathuitapius/Scraper.git
cd car-scraper-viewer
```

### 2. Install Dependencies
Use pip to install the necessary packages:
```bash
pip install -r requirements.txt
```

### 3. Configure MySQL Database
- Create a MySQL database named `cars_db` or configure your preferred database name in the `conn_db()` function within `app.py`.
- Update MySQL connection details (host, user, password) in `conn_db` within `app.py`.

### 4. Run the Application
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Home Page**: Displays a welcome message.
2. **Scrape Data**: Go to `/data` to scrape car data from Jiji Kenya and store it in the database.
3. **View Cars**: Access `/cars` to view all cars stored in the database, filtering for cars over 1,000,000 KES.
4. **Car Details**: Use `/cars/<car_id>` to view details for a specific car.

## Project Structure
```
car-scraper-viewer/
│
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── templates/
│   ├── cars.html           # Template to list all cars
│   └── single_car.html     # Template for individual car details
└── README.md               # Project documentation
```

## Routes

- `/`: Displays a welcome message
- `/data`: Scrapes car data from Jiji Kenya and stores it in the database
- `/cars`: Displays all cars with a filter for prices over 1,000,000 KES
- `/cars/<car_id>`: Shows details for a specific car based on ID

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the project.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.
