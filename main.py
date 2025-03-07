
#### main.py

```python
#!/usr/bin/env python3
import random

empires = [
    "The Sapphire Throne – A civilization built on vast floating islands, lost when the skies burned.",
    "The Silent Dominion – Masters of alchemy, their city turned to glass in an unknown catastrophe.",
    "The Obsidian Order – Ruled by a council of seers, who vanished without a trace.",
    "The Ivory Bastion – A kingdom of scholars, whose final library was swallowed by the desert.",
    "The Ashen Legions – An empire of warriors, erased from history by an unknown force."
]

def get_random_empire():
    return random.choice(empires)

def main():
    print("Welcome to Lost Empire Chronicles!")
    print("Here is a randomly generated ancient empire and its fate:")
    print(get_random_empire())

if __name__ == "__main__":
    main()
