# 📦 Smart Inventory Management System

This is a web-based inventory tracking system built with **Python (Flask)** and **Firebase Firestore**. It allows users to **add, edit, and delete** inventory products while tracking **available stock** and **minimum stock levels**.

---

## 🚀 Features

- ➕ Add new products to inventory  
- ✏️ Update existing product details  
- ❌ Delete products from inventory  
- ⚠️ Automatically highlights low-stock products  
- ☁️ Real-time storage and retrieval using Firebase Firestore  

---

## 🛠️ Technology Used

- 🎨 **Frontend**: HTML, CSS  
- 🐍 **Backend**: Python (Flask Framework)  
- 🔥 **Database**: Firebase Firestore  
- 🧠 **Editor**: Visual Studio Code (VS Code)  
- 🌐 **Hosting (optional)**: Localhost (Flask Dev Server)  

---

## ⚙️ How It Works

1. 📝 User enters product data using a web form.  
2. 🔁 Data is sent to the backend using Flask.  
3. 🗄 Data is stored and managed in Firebase Firestore.  
4. 📃 Product list is dynamically rendered on the webpage.  

---

## 📊 Data Collection

No external dataset is used.  
All data is **manually entered** by the user through the interface and stored in Firestore.

---
---

## 📁 Dataset (Optional)

Although the project works with real-time user input, a sample dataset is added for demonstration.

- **File Name**: `inventory_dataset.csv`
- **Purpose**: To simulate product entries for testing
- **Format**: CSV (Comma Separated Values)
- **Columns**:
  - `name` (Product name)
  - `available_stock`
  - `minimum_stock_required`

You can find it inside the root directory or `sample_data/`.

---

## 🎯 Objective

To build a **simple yet smart** inventory management system that can be extended for **retail**, **grocery**, or **warehouse** usage.

---

## 🖼 Output Screenshots

Check the `output_screenshots/` folder for interface and result images.

---

## ▶️ Demo

To run the project locally:

```bash
python app.py
