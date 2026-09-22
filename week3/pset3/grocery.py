#mala kahich kalat nahi me madat gheun karat ahe
import sys

def main():
    items = []
    try:
        while True:
            item = input().strip().lower()
            items.append(item)
    except EOFError:
        pass

    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    sorted_items = sorted(item_counts.items())

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()