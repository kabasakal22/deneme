# Sample Shopping Application

This repository contains a minimal Flask application that implements a very
basic shopping cart. It exposes several endpoints:

- `/products` – list available products
- `/cart/add` – add a product to the cart via JSON payload
- `/cart` – view items currently in the cart
- `/checkout` – simulate checkout and clear the cart

Run the application in development mode with:

```bash
pip install -r requirements.txt
python app.py
```
