# image-puzzle-game-

# 🧩 Image Puzzle Game

A 2D image-based sliding puzzle game built using Python and Pygame. The goal is to rearrange scrambled image tiles using mouse input to recreate the original picture. Designed with an interactive interface, visual enhancements, and modular architecture, the game provides a fun and smooth user experience.

---

## 🎯 Project Overview

This puzzle game presents a 3x3 grid of image tiles where one tile is always blank. Players move adjacent tiles into the blank space to reconstruct the full image. The game includes a start menu, image selection, in-game UI, and smooth transitions between states. Built to meet graphical project requirements including 2D object rendering, geometric transformations, and user interaction.

---

## 🔧 Features

- 🧠 Classic Sliding Puzzle Logic – 3x3 tile grid with one blank tile
- 🖱️ Mouse Interaction – Click to move tiles and navigate menus
- 🎨 Dynamic Textures – Real images dynamically sliced into tiles
- 💡 Lighting & Visual Effects – Gradient backgrounds, hover effects, and anti-aliased text
- 📂 Multiple Images – Choose from 3 different images at the start
- 🔄 Modular Structure – Start menu and gameplay loop handled as separate game states

---

## 🧱 Technologies Used

- Language: Python  
- Library: Pygame  
- Concepts: 2D graphics, event handling, image processing, geometric transformations

---

## 🎮 Game Flow

1. Start at the Main Menu and choose one of the available images.
2. The chosen image is scrambled into 8 tiles + 1 blank space.
3. Use the mouse to click on tiles next to the blank space and slide them into place.
4. Press "Back to Menu" to restart with a different image.

---

## 📁 Program Structure

- `Start Menu`: Image selection UI  
- `Gameplay Loop`: Handles puzzle logic and rendering  
- `Tile Movement`: Implemented using translation (swapping positions in a 2D array)

---

## ✅ Requirements Met

- 2D object drawing and manipulation
- Interactive user input (mouse)
- Geometric transformations (tile translation)
---

## 📌 How to Run

Make sure you have Python 3 and Pygame installed:

```bash
pip install pygame
