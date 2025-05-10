#EDIT

from PIL import Image, ImageDraw, ImageFont

def create_meme(image_path, top_text, bottom_text, output_path="meme_result.jpg"):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    font_size = int(height / 12)
    font = ImageFont.truetype("arial.ttf", font_size)

    def draw_text(text, y_pos):
        text = text.upper()
        text_width, _ = draw.textsize(text, font=font)
        x = (width - text_width) / 2
        draw.text((x, y_pos), text, font=font, fill="white", stroke_width=2, stroke_fill="black")

    draw_text(top_text, 10)
    draw_text(bottom_text, height - font_size - 20)

    img.save(output_path)
    print(f"✅ Мем сохранён как {output_path}")

# Пример использования
create_meme("D:\Archive\Photo_Pictures\zzAKgCYV5MU.jpg", "КОГДА ПИШЕШЬ НА PYTHON", "И ВСЁ РАБОТАЕТ СРАЗУ")
